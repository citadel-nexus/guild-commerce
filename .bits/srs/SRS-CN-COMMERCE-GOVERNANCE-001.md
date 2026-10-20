<!--
# ─── CGRF Header ───────────────────────────────────────────────
# File:        .bits/srs/SRS-CN-COMMERCE-GOVERNANCE-001.md
# Stage:       04_HYPOTHESIZE
# SRS:         SRS-CN-COMMERCE-GOVERNANCE-001
# CAPS:        pending
# CK:          pending
# Dispatch:    DISP-GOVERNANCE-commerce
# Seat:        BITS-CODEGEN
# Owner:       Citadel Nexus Inc.
# Created:     2026-10-20
# Depends:     GOVERNANCE.md, .github/workflows/provenance.yml
# EnumType:    Doc
# EnumEdges:   GATES GOVERNANCE.md; GATES .github/workflows/provenance.yml
# DAG Node:    none
# Intent:      Define reviewable ownership and provenance acceptance criteria for Commerce.
# ───────────────────────────────────────────────────────────────
-->

# Commerce Guild ownership governance and signed build provenance

SRS: SRS-CN-COMMERCE-GOVERNANCE-001
Dispatch: DISP-GOVERNANCE-commerce
Guildmaster: Alex (GitLab `alex`). Datadog team: `guild-commerce`.

## Motivation

Commerce needs explicit approval responsibility and verifiable provenance for
its build artifacts. Reviewers and consumers must be able to distinguish an
unsigned PR build from a signed artifact built from the protected default branch.

## Acceptance criteria

1. Bootstrap missing agent/context/registry/queue records under the operator's
   directive, preserving existing unrelated SRS records.
2. Name Alex as accountable guildmaster in CODEOWNERS and the charter without
   inventing a GitHub identity. Preserve SDK review responsibility.
3. Define sales/onboarding scope, decision/approval rules, and escalation to
   the guildmasters group. Document enforceable branch protections and their
   limits, including code-owner reviews, signed commits and status checks.
4. Build a distribution archive from compiled output after install, lint,
   tests and build succeed. Attest that exact archive digest using GitHub's
   Sigstore-backed keyless SLSA provenance. Do not sign PR artifacts or deploy.
5. Document artifact verification including repository, signer workflow,
   default-branch source ref and expected commit. Explain unsigned legacy
   release/container outputs and the trust limits of same-repository workflows.
6. Include runnable governance checks, smoke evidence, report and three-type
   memory payload. Do not claim a live attestation until GitHub executes it.

## Boundaries and dependencies

No application implementation, dependency repair, GitHub administration or
remote publication. Existing CI/release workflows remain unchanged. The missing
package lockfile, TypeScript config and test/lint tools must be repaired under
a separate dispatch before build/signing can succeed. No certified SLSA level
is claimed. CK/CAPS/CKS remain pending; gate target B+/75 and CAPS minimum pending.
