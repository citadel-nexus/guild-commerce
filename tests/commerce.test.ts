// ─── CGRF Header ───────────────────────────────────────────────
// File:        tests/commerce.test.ts
// Stage:       11_COMMIT
// SRS:         SRS-CN-COMMERCE-BUILD-001
// CAPS:        pending
// CK:          pending
// Dispatch:    DISP-BUILD-commerce
// Seat:        BITS-CODEGEN
// Owner:       Citadel Nexus Inc.
// Created:     2026-10-20
// Depends:     src/index.ts, src/routes/health.ts, src/automation/nats-listener.ts, src/automation/cml-bridge.ts
// EnumType:    Test
// EnumEdges:   VALIDATES src/index.ts; VALIDATES src/routes/health.ts; VALIDATES src/automation/nats-listener.ts; VALIDATES src/automation/cml-bridge.ts
// DAG Node:    none
// Intent:      Verify startup and message contracts without production connections.
// ───────────────────────────────────────────────────────────────

import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { healthCheck } from '../src/routes/health.js';
import { startListener } from '../src/automation/nats-listener.js';
import { startCmlBridge } from '../src/automation/cml-bridge.js';

const mocks = vi.hoisted(() => ({
  connect: vi.fn(), subscribe: vi.fn(), publish: vi.fn(),
  GuildClient: vi.fn(), start: vi.fn(),
}));

vi.mock('@citadel-guilds/sdk', () => ({ GuildClient: mocks.GuildClient }));
vi.mock('nats', () => ({
  connect: mocks.connect,
  StringCodec: () => ({
    encode: (value: string): Uint8Array => new TextEncoder().encode(value),
    decode: (value: Uint8Array): string => new TextDecoder().decode(value),
  }),
}));

async function* messages(payloads: string[]) {
  for (const data of payloads) {
    yield { subject: 'fixture.subject', data: new TextEncoder().encode(data) };
  }
}

beforeEach(() => {
  vi.resetAllMocks();
  vi.stubEnv('NATS_URL', 'nats://127.0.0.1:4222');
  vi.spyOn(console, 'log').mockImplementation(() => undefined);
  mocks.connect.mockResolvedValue({ subscribe: mocks.subscribe, publish: mocks.publish });
  mocks.subscribe.mockReturnValue(messages([]));
  mocks.GuildClient.mockImplementation(function () { return { start: mocks.start }; });
});

afterEach(() => {
  vi.useRealTimers();
  vi.unstubAllEnvs();
  vi.restoreAllMocks();
});

describe('guild startup', () => {
  it('starts the configured Commerce client without contacting the SDK backend', async () => {
    vi.resetModules();
    await import('../src/index.js');
    expect(mocks.GuildClient).toHaveBeenCalledExactlyOnceWith({
      name: 'commerce', natsPrefix: 'citadel.commerce', port: 8422,
    });
    expect(mocks.start).toHaveBeenCalledOnce();
    expect(mocks.connect).not.toHaveBeenCalled();
  });
});

describe('health contract', () => {
  it('reports the guild identity and current UTC timestamp', () => {
    vi.useFakeTimers();
    vi.setSystemTime(new Date('2026-10-20T12:00:00Z'));
    expect(healthCheck()).toEqual({
      guild: 'commerce', status: 'healthy', version: '0.1.0',
      nats_prefix: 'citadel.commerce.*', timestamp: '2026-10-20T12:00:00.000Z',
    });
    vi.advanceTimersByTime(1000);
    expect(healthCheck().timestamp).toBe('2026-10-20T12:00:01.000Z');
  });
});

describe('NATS listener boundary', () => {
  it('uses configured servers, consumes messages and decodes Unicode', async () => {
    mocks.subscribe.mockReturnValue(messages(['first', 'café']));
    await startListener();
    expect(mocks.connect).toHaveBeenCalledExactlyOnceWith({ servers: 'nats://127.0.0.1:4222' });
    expect(mocks.subscribe).toHaveBeenCalledExactlyOnceWith('citadel.commerce.>');
    expect(console.log).toHaveBeenCalledWith('[commerce] fixture.subject: first');
    expect(console.log).toHaveBeenCalledWith('[commerce] fixture.subject: café');
    expect(mocks.publish).not.toHaveBeenCalled();
  });

  it('allows an empty subscription to finish', async () => {
    await expect(startListener()).resolves.toBeUndefined();
    expect(mocks.publish).not.toHaveBeenCalled();
  });

  it('propagates connection failures without subscribing', async () => {
    const failure = new Error('fixture connection refused');
    mocks.connect.mockRejectedValue(failure);
    await expect(startListener()).rejects.toBe(failure);
    expect(mocks.subscribe).not.toHaveBeenCalled();
  });
});

describe('CML bridge boundary', () => {
  it('publishes one encoded completion per received task', async () => {
    mocks.subscribe.mockReturnValue(messages(['{"task_id":"task-1"}', '{"task_id":"task-2"}']));
    await startCmlBridge();
    expect(mocks.connect).toHaveBeenCalledExactlyOnceWith({ servers: 'nats://127.0.0.1:4222' });
    expect(mocks.subscribe).toHaveBeenCalledExactlyOnceWith('citadel.commerce.cml.task');
    expect(mocks.publish).toHaveBeenCalledTimes(2);
    for (const [index, taskId] of ['task-1', 'task-2'].entries()) {
      expect(mocks.publish).toHaveBeenNthCalledWith(index + 1, 'citadel.commerce.cml.result',
        new TextEncoder().encode(JSON.stringify({ task_id: taskId, status: 'done', output: 'ok' })));
    }
  });

  it('reports a failed publication with the same task identity', async () => {
    mocks.subscribe.mockReturnValue(messages(['{"task_id":"task-1"}']));
    mocks.publish.mockImplementationOnce(() => { throw new Error('fixture publish failed'); });
    await startCmlBridge();
    expect(mocks.publish).toHaveBeenNthCalledWith(2, 'citadel.commerce.cml.result',
      new TextEncoder().encode(JSON.stringify({
        task_id: 'task-1', status: 'failed', error: 'Error: fixture publish failed',
      })));
  });

  it('propagates malformed JSON without publishing a false success', async () => {
    mocks.subscribe.mockReturnValue(messages(['invalid json']));
    await expect(startCmlBridge()).rejects.toBeInstanceOf(SyntaxError);
    expect(mocks.publish).not.toHaveBeenCalled();
  });

  it('propagates connection failures', async () => {
    const failure = new Error('fixture connection refused');
    mocks.connect.mockRejectedValue(failure);
    await expect(startCmlBridge()).rejects.toBe(failure);
    expect(mocks.subscribe).not.toHaveBeenCalled();
  });

  it('does not publish when there are no tasks', async () => {
    await expect(startCmlBridge()).resolves.toBeUndefined();
    expect(mocks.publish).not.toHaveBeenCalled();
  });
});
