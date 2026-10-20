<!--
# ─── CGRF Header ───────────────────────────────────────────────
# File:        .bits/context.md
# Stage:       11_COMMIT
# SRS:         SRS-CN-COMMERCE-GOVERNANCE-001
# CAPS:        pending
# CK:          pending
# Dispatch:    DISP-GOVERNANCE-commerce
# Seat:        BITS-CODEGEN
# Owner:       Citadel Nexus Inc.
# Created:     2026-10-20
# Depends:     .bits/queue/DISP-GOVERNANCE-commerce.md
# EnumType:    ConfigDoc
# EnumEdges:   DEPENDS_ON .bits/queue/DISP-GOVERNANCE-commerce.md
# DAG Node:    none
# Intent:      Identify the active staging dispatch without authorizing unrelated work.
# ───────────────────────────────────────────────────────────────
-->

# Active staging context

- SRS: SRS-CN-COMMERCE-GOVERNANCE-001
- Dispatch: DISP-GOVERNANCE-commerce (`in_progress`)
- Authorization: authenticated operator directive in the queue record.
- Guildmaster: Alex (GitLab `alex`); Datadog team: `guild-commerce`.
- Target: default branch `main`, through one reviewable PR only.
- CKS gate: B+/75; CKS, CAPS and CK: pending. CAPS minimum has not been
  supplied by the operator; do not invent a numeric threshold.

The living-world SRS remains planned and its dispatch queued. Do not execute it.
Keep existing application behavior and release publishing unchanged. Missing
lockfile/compiler/test/lint setup is an application prerequisite for provenance
builds, not authorization to expand this governance dispatch.

No issue-specific Memory Brief was supplied. The linked Bits conversation
contains the request for guild governance/provenance, not prior governance
implementation details. Sibling conventions could not be checked: the managed
attachment of the README-referenced guild-sdk repository was rejected by the
public/private session boundary. Use this repository's existing flat SRS
registry and queue conventions and record that limitation.
