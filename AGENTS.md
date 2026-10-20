<!--
# ─── CGRF Header ───────────────────────────────────────────────
# File:        AGENTS.md
# Stage:       04_HYPOTHESIZE
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
# Intent:      Constrain Commerce governance work to the authorized public staging scope.
# ───────────────────────────────────────────────────────────────
-->

# Commerce Guild agent guidance

Owner: Citadel Nexus Inc. Seat: BITS-CODEGEN. Mode: staging.
This repository is `citadel-nexus/guild-commerce`, a public TypeScript guild
package; it is not the CNWB monorepo or `cnwb-mirror`.

Read this file, CLAUDE.md, .bits/context.md, .bits/srs_registry.yml, the active
SRS document, and its queue record before changes. The authenticated operator
Dmitry Richard (mr.nobody@citadel-nexus.com) authorized the governance bootstrap
and creation of these records. The exact authorization is recorded in
.bits/queue/DISP-GOVERNANCE-commerce.md. It does not grant production access.

- Work only on SRS-CN-COMMERCE-GOVERNANCE-001 in this dispatch. Preserve the
  separate living-world registry entry and queued dispatch.
- Guildmaster: Alex (GitLab `alex`). Datadog team: `guild-commerce`. The operator
  confirmed GitHub owner team `@citadel-nexus/guild-commerce` and automation
  identity GitHub App `alex-commerce-guildmaster` through the Datadog team links.
  GitHub Apps cannot be code owners; use the team for review ownership.
- Scope: governance, ownership, branch protection documentation, build
  attestations, verification and associated dispatch/report/memory records.
- No deploys, production changes, GitHub settings writes, secret handling,
  direct pushes, runtime changes, or private-stack work. Preserve existing
  release and CI workflows. Do not modify notify-citadel.yml.
- Use one SRS branch/PR. Conventional commits include Phase, Files, Smoke,
  SRS, Dispatch and CK: pending footers. The publishing UI controls the final
  branch name and PR creation.
- New files have CGRF headers; JSON uses a sibling .cgrf.yaml. Markdown headers
  are HTML comments. Stages are logical classifications at the repo-native
  paths explicitly requested by the operator: governance/CODEOWNERS are
  06_PLAN; agent/SRS documents 04_HYPOTHESIZE; .bits operational records and
  GitHub workflows 11_COMMIT. Do not move GitHub-recognized paths into stage
  directories or create application code as part of this bootstrap.
- Do not read or change protected CNWB paths, third-party CGRF files, secrets,
  signing-key logic, or canary memory. Emit CK/CAPS/CKS as pending only.
- Follow CONTRIBUTING.md for package conventions. Do not invent dependency
  versions, a lockfile, a GitHub account mapping, or successful checks.
- Run the dispatch smoke block. Record pre-existing application test failures
  separately from governance checks; request a follow-up dispatch for them.
- Governance and provenance acceptance criteria are in the SRS. No new
  runtime module is introduced, so SAKE module stubs are not applicable.
