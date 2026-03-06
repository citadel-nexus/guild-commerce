export function healthCheck() {
  return {
    guild: 'commerce',
    status: 'healthy',
    version: '0.1.0',
    nats_prefix: 'citadel.commerce.*',
    timestamp: new Date().toISOString(),
  };
}
