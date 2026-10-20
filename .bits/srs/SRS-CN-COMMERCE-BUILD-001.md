<!--
# ─── CGRF Header ───────────────────────────────────────────────
# File:        .bits/srs/SRS-CN-COMMERCE-BUILD-001.md
# Stage:       04_HYPOTHESIZE
# SRS:         SRS-CN-COMMERCE-BUILD-001
# CAPS:        pending
# CK:          pending
# Dispatch:    DISP-BUILD-commerce
# Seat:        BITS-CODEGEN
# Owner:       Citadel Nexus Inc.
# Created:     2026-10-20
# Depends:     package.json, .github/workflows/provenance.yml
# EnumType:    Doc
# EnumEdges:   GATES package.json; GATES .github/workflows/provenance.yml
# DAG Node:    none
# Intent:      Define build repair without weakening application or provenance checks.
# ───────────────────────────────────────────────────────────────
-->

# Commerce build repair and provenance verification

SRS: SRS-CN-COMMERCE-BUILD-001. Dispatch: DISP-BUILD-commerce.

Restore reproducible installation, compilation, lint and tests for the existing
Commerce application. The operator authorized this as a new branch/PR after
merged governance PR #18. No deployment, settings or secret changes are allowed.

## Acceptance

1. Resolve real SDK/runtime/tooling dependencies and generate a real npm lockfile.
   If registry access or SDK availability blocks this, report it; never fabricate
   a lockfile, integrity hash or SDK replacement.
2. Configure strict TS source/test typechecking and a build emitting only source
   distribution files; lint source/tests; run Vitest with >=80% coverage gates.
   Do not weaken or delete existing tests to obtain a green result.
3. Retain CodeQL and secret scanning, enable their PR coverage, and preserve the
   corrected Docker login expressions already merged in PR #16.
4. Attest only real successful build output. Verify the downloaded archive and
   bundle with gh attestation verify, constrained to repo, ref, SHA and workflow.
   Reject tampering and incorrect source/workflow identities.
5. Report npm ci, lint, typecheck, test and build independently. Keep branch
   protection and OIDC/attestation enablement as pending admin actions.

No runtime behavior change is proposed. Application tests use mocked network
boundaries; live cryptographic issuance/verification requires a successful
GitHub run and administrator enablement. Gate: B+/75, grades/minimum CAPS pending.
