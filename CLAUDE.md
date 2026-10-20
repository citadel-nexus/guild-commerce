<!--
# ─── CGRF Header ───────────────────────────────────────────────
# File:        CLAUDE.md
# Stage:       04_HYPOTHESIZE
# SRS:         SRS-CN-COMMERCE-BUILD-001
# CAPS:        pending
# CK:          pending
# Dispatch:    DISP-BUILD-commerce
# Seat:        BITS-CODEGEN
# Owner:       Citadel Nexus Inc.
# Created:     2026-10-20
# Depends:     AGENTS.md, GOVERNANCE.md
# EnumType:    ConfigDoc
# EnumEdges:   DEPENDS_ON AGENTS.md; DEPENDS_ON GOVERNANCE.md
# DAG Node:    none
# Intent:      Give seats the authorized Commerce build-repair scope.
# ───────────────────────────────────────────────────────────────
-->

# Commerce Guild seat context

Commerce owns sales/onboarding: Scope Sheet Pro, leads, walk-in, CTA and
provisioning. Alex (GitLab `alex`) is guildmaster. GitHub team
`@citadel-nexus/guild-commerce` owns reviews; GitHub App
`alex-commerce-guildmaster` is his automation identity. Datadog: `guild-commerce`.

SRS-CN-COMMERCE-BUILD-001 and DISP-BUILD-commerce authorize the staging build
repair after governance PR #18. Read AGENTS.md and .bits/context.md. Restore the
real package toolchain and signed-artifact verification without deployments,
settings changes or fabricated SDKs. Escalate cross-guild decisions to the
guildmasters group. The charter and pending admin requirements are in GOVERNANCE.md.
