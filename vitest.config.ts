// ─── CGRF Header ───────────────────────────────────────────────
// File:        vitest.config.ts
// Stage:       11_COMMIT
// SRS:         SRS-CN-COMMERCE-BUILD-001
// CAPS:        pending
// CK:          pending
// Dispatch:    DISP-BUILD-commerce
// Seat:        BITS-CODEGEN
// Owner:       Citadel Nexus Inc.
// Created:     2026-10-20
// Depends:     tests/commerce.test.ts
// EnumType:    ConfigDoc
// EnumEdges:   VALIDATES tests/commerce.test.ts
// DAG Node:    none
// Intent:      Require meaningful source coverage and fail when application tests are absent.
// ───────────────────────────────────────────────────────────────

import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    environment: 'node',
    include: ['tests/**/*.test.ts'],
    coverage: {
      provider: 'v8',
      include: ['src/**/*.ts'],
      thresholds: { lines: 80, branches: 80, functions: 80, statements: 80 },
    },
  },
});
