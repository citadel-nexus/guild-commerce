<!--
# ─── CGRF Header ───────────────────────────────────────────────
# File:        .bits/queue/DISP-GOVERNANCE-commerce.md
# Stage:       11_COMMIT
# SRS:         SRS-CN-COMMERCE-GOVERNANCE-001
# CAPS:        pending
# CK:          pending
# Dispatch:    DISP-GOVERNANCE-commerce
# Seat:        BITS-CODEGEN
# Owner:       Citadel Nexus Inc.
# Created:     2026-10-20
# Depends:     .bits/srs/SRS-CN-COMMERCE-GOVERNANCE-001.md, .bits/checks/verify_governance.py
# EnumType:    Doc
# EnumEdges:   GATES .bits/srs/SRS-CN-COMMERCE-GOVERNANCE-001.md; VERIFIED_BY .bits/checks/verify_governance.py
# DAG Node:    none
# Intent:      Bind staging governance tasks to the authenticated operator directive.
# ───────────────────────────────────────────────────────────────
-->

# DISP-GOVERNANCE-commerce

- srs: SRS-CN-COMMERCE-GOVERNANCE-001
- guild: commerce
- champion: Alex
- seat: BITS-CODEGEN
- mode: staging
- branch: bits/SRS-CN-COMMERCE-GOVERNANCE-001-bootstrap
- status: in_progress
- brief: .bits/srs/SRS-CN-COMMERCE-GOVERNANCE-001.md
- authorization_source: authenticated operator directive through Bits AI
- operator: Dmitry Richard, mr.nobody@citadel-nexus.com

## Authorization source

The operator explicitly directed: "create those" and authorized creating missing
AGENTS.md, CLAUDE.md, context, registry, SRS and queue prerequisites. The directive
names SRS-CN-COMMERCE-GOVERNANCE-001 and DISP-GOVERNANCE-commerce with status
`in_progress`, and covers CODEOWNERS, GOVERNANCE.md, branch protection/ruleset
documentation or config, SLSA build provenance, artifact signing and verification.
Bounds: one branch and PR for this SRS; no production, deploy, push to main,
GitHub settings changes, or secrets. These are local staging authorization
records, not a claim that a remote VCC database row was created or verified.

## Task table

| Phase | Task | Gate |
| --- | --- | --- |
| A | Bootstrap authorized records and register SRS | `python .bits/checks/verify_governance.py RecordsTests` |
| B | Add ownership, charter and admin requirements | `python .bits/checks/verify_governance.py OwnershipTests` |
| C | Add restricted build/sign workflow and verification | `python .bits/checks/verify_governance.py WorkflowTests` |
| D | Record validation, report and memory for review | `python .bits/checks/verify_governance.py MemoryTests` |

## Smoke block

Prerequisite: Python 3.11+ and PyYAML 6.0.3 (the governance CI job installs it).
Each phase prints PASS or FAIL and stops the smoke run on failure.

```bash
set -euo pipefail
for phase in RecordsTests OwnershipTests WorkflowTests MemoryTests; do
  if python .bits/checks/verify_governance.py "$phase"; then
    echo "PASS: $phase"
  else
    echo "FAIL: $phase"
    exit 1
  fi
done
```

Application baseline commands: `npm ci --offline --ignore-scripts`, `npm test`,
`npm run lint`, `npm run build`. Record failures separately; they are prerequisites
for a live signed artifact and are not waived in the new workflow.

## Memory Brief

No issue-specific Memory Brief was provided. The source Bits conversation
requested governance/provenance for guildmasters. No prior memory was ingested.
