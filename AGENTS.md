<!--
# ─── CGRF Header ───────────────────────────────────────────────
# File:        AGENTS.md
# Stage:       04_HYPOTHESIZE
# SRS:         SRS-CN-COMMERCE-BUILD-001
# CAPS:        pending
# CK:          pending
# Dispatch:    DISP-BUILD-commerce
# Seat:        BITS-CODEGEN
# Owner:       Citadel Nexus Inc.
# Created:     2026-10-20
# Depends:     .bits/queue/DISP-BUILD-commerce.md
# EnumType:    ConfigDoc
# EnumEdges:   DEPENDS_ON .bits/queue/DISP-BUILD-commerce.md
# DAG Node:    none
# Intent:      Keep Commerce build repair within the active operator authorization.
# ───────────────────────────────────────────────────────────────
-->

# Commerce Guild agent guidance

Owner: Citadel Nexus Inc. Seat: BITS-CODEGEN. Mode: staging.
This is the public TypeScript repository `citadel-nexus/guild-commerce`.

Read AGENTS.md, CLAUDE.md, .bits/context.md, .bits/srs_registry.yml, the active
SRS and queue record before changes. The current authorization is
SRS-CN-COMMERCE-BUILD-001 / DISP-BUILD-commerce. The authenticated operator
Dmitry Richard authorized the build-repair follow-up separately from merged
PR #18. Preserve the governance and living-world records as historical scopes.

- Scope: reproducible dependencies/lockfile, TypeScript, ESLint, Vitest, Docker
  CI expressions, retained CodeQL/secret scanning and real-build provenance
  verification. Preserve runtime behavior and existing tests; do not hide build
  failures with stubs, exclusions or relaxed coverage thresholds.
- No production/deploy, push to main, GitHub settings or secrets changes.
  Branch protection and OIDC/attestation permissions remain admin actions.
- Alex (GitLab `alex`) is guildmaster. The operator confirmed GitHub owner team
  `@citadel-nexus/guild-commerce` and GitHub App `alex-commerce-guildmaster` as
  his automation identity. Apps cannot be CODEOWNERS or bypass rules by default.
- Use one new branch/PR for this SRS. Conventional commits include Phase, Files,
  Smoke, SRS, Dispatch and CK: pending. Publication is through the coding UI.
- Keep CGRF headers and JSON companions. Logical stages at repo-native paths:
  guidance/specs 04_HYPOTHESIZE, governance docs 06_PLAN, build/test/CI and .bits
  records 11_COMMIT. This operator-authorized repair includes build configuration
  and tests; it does not authorize private-stack or production code work.
- Do not read/change protected CNWB paths, secrets, signing-key logic or canary
  memory. Keep CK/CAPS/CKS pending. No notify-citadel.yml changes.
- Follow CONTRIBUTING.md. Never invent SDK implementations, dependency integrity
  hashes, lockfiles or successful results. Preserve previous dispatch memory;
  write current evidence under .bits/out/DISP-BUILD-commerce/.
- Run the dispatch gates and report npm ci/lint/typecheck/test/build results
  separately. Record dependency/network blockers and keep CI failing closed.
