<!--
# ─── CGRF Header ───────────────────────────────────────────────
# File:        .bits/context.md
# Stage:       11_COMMIT
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
# Intent:      Identify the separate authorized build repair and its baseline.
# ───────────────────────────────────────────────────────────────
-->

# Active staging context

- SRS: SRS-CN-COMMERCE-BUILD-001
- Dispatch: DISP-BUILD-commerce (`in_progress`)
- Operator: Dmitry Richard, mr.nobody@citadel-nexus.com; seat BITS-CODEGEN.
- Branch: bits/SRS-CN-COMMERCE-BUILD-001-repair
- Base: 15c62810b6baf379b54d850cac9210f39719b92f (verified origin/main).
- Scope: lockfile, TypeScript, ESLint, Vitest, CI and real-build provenance verification.
- CKS gate: B+/75; CKS/CAPS/CK and CAPS minimum: pending.

PR #18 merged governance. PR #16 subsequently repaired the TypeScript syntax
and Docker login expressions. Preserve those fixes; do not duplicate them.
Living-world work remains outside this dispatch. Previous governance memory is
historical; validate current-file metadata through this dispatch's payload.

No production/deploy, push to main, GitHub settings or secrets changes.
Branch protection and OIDC/attestation permissions are admin-only pending actions.
No new issue Memory Brief was supplied; the operator's directive is recorded in
the queue. Dependency resolution must use real registry data, not a guessed SDK.
