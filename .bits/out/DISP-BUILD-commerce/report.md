<!--
# ─── CGRF Header ───────────────────────────────────────────────
# File:        .bits/out/DISP-BUILD-commerce/report.md
# Stage:       11_COMMIT
# SRS:         SRS-CN-COMMERCE-BUILD-001
# CAPS:        pending
# CK:          pending
# Dispatch:    DISP-BUILD-commerce
# Seat:        BITS-CODEGEN
# Owner:       Citadel Nexus Inc.
# Created:     2026-10-20
# Depends:     .bits/queue/DISP-BUILD-commerce.md, .bits/out/DISP-BUILD-commerce/memory.json
# EnumType:    Doc
# EnumEdges:   VALIDATES .bits/queue/DISP-BUILD-commerce.md; DEPENDS_ON .bits/out/DISP-BUILD-commerce/memory.json
# DAG Node:    none
# Intent:      Record completed build repair and unresolved dependency and admin acceptance.
# ───────────────────────────────────────────────────────────────
-->

# §15 Report Template

## §1 SUMMARY

Status: PARTIAL — configuration/CI implemented; real dependency resolution blocked.
Dispatch: DISP-BUILD-commerce
Seat: BITS-CODEGEN
SRS: SRS-CN-COMMERCE-BUILD-001
Branch: bits/SRS-CN-COMMERCE-BUILD-001-repair
Base: 15c62810b6baf379b54d850cac9210f39719b92f (origin/main, includes PRs #18 and #16)
Tasks: A/C implemented, B partial, D recorded; application acceptance incomplete.
Smoke: 5/5 governance/build-policy gates, 17/17 Python checks;
application commands 1/5 passed with caveats.
CKS Gate: B+/75; CKS: pending; CAPS: pending; CAPS minimum: pending; CK: pending.
Commits: inspect `git log --oneline 15c62810b6baf379b54d850cac9210f39719b92f..HEAD`.

## §2 TASK RESULTS

Task A — Authorization: PASS. Registered SRS/dispatch and updated active seat
context under the authenticated operator's staging directive. Previous SRS
records and governance memory retained.
Verify: `python .bits/checks/verify_governance.py RecordsTests`.
Files: AGENTS.md, CLAUDE.md, .bits/context.md, .bits/srs_registry.yml,
.bits/srs/SRS-CN-COMMERCE-BUILD-001.md, .bits/queue/DISP-BUILD-commerce.md.
CKET: 04_HYPOTHESIZE / 11_COMMIT.

Task B — Toolchain and tests: PARTIAL. Declared compiler/linter/test dependencies,
strict source and test typechecking, source-only output and 80% coverage gates.
Added ten Vitest tests covering startup, health, NATS messages/connections,
CML completion/publication failures/malformed JSON. No existing test removed.
No runtime source modified; no SDK substituted. No generated lockfile is included
because real registry metadata is unavailable; no fake hashes or resolutions.
Verify: `npm ci`; `npm run lint`; `npm run typecheck`; `npm test`; `npm run build`.
Files: package.json, tsconfig*.json, eslint.config.js, vitest.config.ts,
tests/commerce.test.ts, JSON CGRF companions, .gitignore, .dockerignore.
CKET: 11_COMMIT (build/test configuration and fixtures).

Task C — CI and signed output: PASS for local checks, PARTIAL for live acceptance.
Added typecheck gates and PR security coverage while preserving CodeQL/TruffleHog.
PR #16 already fixed Docker login expressions; this branch preserves and tests
them. The new read-only verification job downloads the same run's archive/bundle
by immutable IDs and runs gh attestation verify with identity constraints, then
rejects altered bytes, wrong commit and wrong workflow. Existing signer still
has no repository checkout or shell execution. Workflow packs real compiled
dist only after all npm gates pass; fixture archives are never signed.
Verify: `python .bits/checks/verify_governance.py WorkflowTests BuildTests`.
Files: .github/workflows/{ci,security-scan,provenance}.yml,
.bits/checks/verify_governance.py, GOVERNANCE.md. CKET: 11_COMMIT / 06_PLAN.

Task D — Evidence: PASS. Final MemoryTests pass. Current metadata is scoped
to the new build dispatch; old governance memory is historical and unchanged.
Verify: `python .bits/checks/verify_governance.py MemoryTests`.
Files: .bits/out/DISP-BUILD-commerce/{report.md,memory.json,memory.cgrf.yaml}.
CKET: 11_COMMIT.

## §3 SMOKE TEST RESULTS

Node v24.13.0 / npm 11.6.2 locally; CI retains Node 20. npm registry operations
used npm_config_offline=true because shell internet access is unavailable.
The SDK is not in the cache; no outbound fetch or credentials were attempted.
Lockfile generation with `npm install --package-lock-only --ignore-scripts
--no-audit --no-fund` failed ENOTCACHED for @citadel-guilds/sdk on registry.npmjs.org.
This does not establish whether the SDK is published there. Operator registry
clarification was requested; do not infer a private registry or add credentials.

| Command | Expected | Observed | Result |
| --- | --- | --- | --- |
| npm ci | reproducible install | EUSAGE, missing lockfile | BLOCKED |
| npm run lint | lint clean | exit 0 | PASS, preinstalled tools only |
| npm run typecheck | source and test types clean | TS2688, @types/node missing | BLOCKED |
| npm test | tests and >=80% coverage pass | vitest not found | BLOCKED |
| npm run build | real dist/index.js | missing Node types, NATS and SDK | BLOCKED |

Lint used real preinstalled ESLint 9.16.0, typescript-eslint 8.18.0 and TypeScript
5.7.3 via ignored local symlinks. This is not npm ci success or proof that the
full selected dependency graph resolves. TS emitted no dist on failure.
No Vitest test or coverage execution is claimed. Dependency package names/ranges
are declared, but only a registry-generated lockfile can establish exact
transitive resolutions. No weakening or deleting tests to bypass these failures.

All 17 governance/build-policy tests passed, including current-dispatch headers
and memory integrity; strict mypy passed. Verification orchestration fixtures prove the shell rejects
missing artifacts, rejects a verifier that accepts everything, and stops when
the original fails verification. They do not prove cryptographic issuance.
Run the queue smoke block for all retained governance plus new build checks.
Actionlint/pytest are unavailable. CI still requires real npm success.

## §4 MEMORY INGEST

Payload: .bits/out/DISP-BUILD-commerce/memory.json.
Type A: 25; Type B: 41; Type C: 3. IOO compliance: true; DKG orphans: 0.
Validate with MemoryTests. Each file has a
substantive intent and at least one Type B edge. IOO fields are non-null;
CK/CAPS pending. No direct memory ingestion or remote VCC update.

## §5 CKET FILING

04_HYPOTHESIZE: AGENTS.md, CLAUDE.md, new build SRS.
06_PLAN: GOVERNANCE.md.
11_COMMIT: build/test configuration, tests, CI, active .bits records and output.
13_SAVE: none. CGRF coverage is checked by RecordsTests; JSON has companions.
These logical repo-native locations are explicitly authorized build-repair scope.
REFLEX: deferred to private post-merge validation; not run locally.

## §6 GOVERNANCE

Entity: Citadel Nexus Inc. License posture unchanged. No new runtime modules,
so application SAKE stubs are not applicable. Existing runtime sources, source
subjects, release publishing and the old governance payload were not changed.
No production/deploy, remote push, GitHub settings or secrets changes.
GitHub owner team/app remain operator-confirmed; no mapping follow-up reopened.
Secret-prefix scan: all 25 touched files passed. Stripe: not applicable; no checkout code.
Verify scope: `git diff --name-only 15c62810b6baf379b54d850cac9210f39719b92f HEAD`.

## §7 NEXT ACTIONS

- BLOCKER: obtain the approved SDK registry location and package access, resolve
  the real graph and generate/review package-lock.json. Re-run all five npm
  commands and coverage in Node 20; fix any resulting errors without weakening
  checks. No lockfile is fabricated or silently omitted from acceptance.
- Admin-only pending: branch protection, code-owner approval, signed commits,
  required checks and Actions attestation/OIDC permissions. Confirm security
  contexts on PRs before requiring them; push-only signing/verification jobs
  are not PR requirements. No settings were changed here.
- After a successful main build, validate real positive and negative attestation
  verification in the new Verify build provenance job. Live issuance untested.
- Operator: CAPS minimum remains pending. No private-stack handoff requested.
- PR: new BUILD SRS branch/PR only; do not update merged governance PR #18.
  Suggested labels: bits:codegen, srs:srs-cn-commerce-build-001,
  dispatch:disp-build-commerce, verified:manual-review. No tests-pass label.
