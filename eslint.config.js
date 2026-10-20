// ─── CGRF Header ───────────────────────────────────────────────
// File:        eslint.config.js
// Stage:       11_COMMIT
// SRS:         SRS-CN-COMMERCE-BUILD-001
// CAPS:        pending
// CK:          pending
// Dispatch:    DISP-BUILD-commerce
// Seat:        BITS-CODEGEN
// Owner:       Citadel Nexus Inc.
// Created:     2026-10-20
// Depends:     src/index.ts, tests/commerce.test.ts
// EnumType:    ConfigDoc
// EnumEdges:   VALIDATES src/index.ts; VALIDATES tests/commerce.test.ts
// DAG Node:    none
// Intent:      Lint TypeScript source and tests without suppressing unused values.
// ───────────────────────────────────────────────────────────────

import tsParser from '@typescript-eslint/parser';
import tsPlugin from '@typescript-eslint/eslint-plugin';

export default [
  { ignores: ['dist/**', 'coverage/**', 'node_modules/**'] },
  {
    files: ['**/*.ts', '**/*.js'],
    languageOptions: {
      parser: tsParser,
      ecmaVersion: 'latest',
      sourceType: 'module',
      globals: { console: 'readonly', process: 'readonly', TextEncoder: 'readonly', TextDecoder: 'readonly' },
    },
    plugins: { '@typescript-eslint': tsPlugin },
    rules: { ...tsPlugin.configs.recommended.rules },
  },
];
