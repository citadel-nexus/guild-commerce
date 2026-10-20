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
Branch: dd/bits/SRS-CN-COMMERCE-GOVERNANCE-001-bootstrap (UI-bound, operator-authorized)
Base: 5dc37392985348cfb1749dbd70175699e1738967 (origin/main, includes merged build PR #19)
Tasks: A/C implemented, B partial, D recorded; application acceptance incomplete.
Smoke: 6/6 continuation gates; 22/22 Python policy checks;
application commands 1/5 passed with caveats.
CKS Gate: B+/75; CKS: pending; CAPS: pending; CAPS minimum: pending; CK: pending.
Commits: inspect `git log --oneline 5dc37392985348cfb1749dbd70175699e1738967..HEAD`.
Previously merged build commit ce8a7ed is preserved; no published commit was rebased.

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
Current Type A/B/C counts are in the payload summary. IOO compliance: true; DKG orphans: 0.
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
Secret-prefix scan: continuation changed-file scan passed; no lockfile or dist exists locally. Stripe: not applicable; no checkout code.
Verify scope: `git diff --name-only 5dc37392985348cfb1749dbd70175699e1738967 HEAD`.

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
- PR: new BUILD follow-up diff on the current-main UI-bound branch; PRs #18/#19 are merged.
  Suggested labels: bits:codegen, srs:srs-cn-commerce-build-001,
  dispatch:disp-build-commerce, verified:manual-review. No tests-pass label.


## Lockfile-refresh continuation (same dispatch)

The operator authorized a workflow_dispatch-only flow, its build guide, and
alignment of the bound branch with current main. GitHub confirms PR #19 already
merged ce8a7ed. The bound branch was a main ancestor and fast-forwarded to
5dc37392985348cfb1749dbd70175699e1738967. Replaying/rebasing that published build
commit would duplicate merged work. The next PR diff contains only this follow-up.
Publication itself remains an external UI action; no refs were pushed here.

Added .github/workflows/lockfile-refresh.yml and .github/BUILD.md, .nvmrc (Node 20)
and parser-safe governance companions. Every action in the new workflow is pinned
to a full SHA. The validation job has contents:read/packages:read, authenticates
GitHub Packages using GITHUB_TOKEN, generates the real lockfile and runs all five
npm gates. Only after success does a separate contents:write/pull-requests:write
job download its immutable artifact, commit the allowlisted lockfile/evidence and
open a PR on bits/lockfile-refresh. It refuses existing branches and never pushes
to main or force-pushes. No workflow was dispatched, and no local lockfile exists.

New LockfileTests cover the dispatch/default-ref restriction, SHA pins, scoped
registry auth, permission separation, all five gate failures, fixed-branch
publication, shell/Python syntax and refusal to overwrite an existing branch.
The first run had one false-positive assertion: the phrase 'npm gates' inside a
commit message matched a no-npm-command check. The assertion now matches actual
shell command positions, retaining the no-dependency-execution requirement for
the write-enabled job. All five LockfileTests then passed; strict mypy passed.
Verify: `python .bits/checks/verify_governance.py LockfileTests`.

All requested npm commands were rerun with npm_config_offline=true:

| Command | Latest result |
| --- | --- |
| npm ci | BLOCKED: no package-lock.json (EUSAGE) |
| npm run lint | PASS using preinstalled ESLint/parser tools via ignored local symlinks |
| npm run typecheck | BLOCKED: missing @types/node (TS2688) |
| npm test | BLOCKED: Vitest not installed |
| npm run build | BLOCKED: missing Node types, NATS and SDK; no dist emitted |

No application tests or live cryptographic verification are claimed to pass.
No sandbox lockfile generation was attempted in this continuation. The registry
scope/package availability and GITHUB_TOKEN package read grant need admin/package
maintainer validation. No new tokens or secrets were created or printed.

Admin prerequisites are in .github/BUILD.md: package access, Actions PR creation,
branch rules, required checks and approved commit signing, plus separate signer
OIDC/attestation permissions. GITHUB_TOKEN-created PRs do not trigger other
workflows, and this refresh bot commit is unsigned: a trusted check-triggering
and signing path is required before merge. Existing CI/provenance install jobs
also need reviewed private-SDK auth configuration; the manual flow does not
silently change them. No ruleset bypass or settings changes were performed.

Final continuation verification: 22/22 policy checks, all six phase gates and
strict mypy passed. The five requested npm outcomes remain as recorded above.
