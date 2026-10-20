<!--
# ─── CGRF Header ───────────────────────────────────────────────
# File:        .bits/queue/DISP-BUILD-commerce.md
# Stage:       11_COMMIT
# SRS:         SRS-CN-COMMERCE-BUILD-001
# CAPS:        pending
# CK:          pending
# Dispatch:    DISP-BUILD-commerce
# Seat:        BITS-CODEGEN
# Owner:       Citadel Nexus Inc.
# Created:     2026-10-20
# Depends:     .bits/srs/SRS-CN-COMMERCE-BUILD-001.md, .bits/checks/verify_governance.py
# EnumType:    Doc
# EnumEdges:   GATES .bits/srs/SRS-CN-COMMERCE-BUILD-001.md; VERIFIED_BY .bits/checks/verify_governance.py
# DAG Node:    none
# Intent:      Bind build-repair work and validation to the operator directive.
# ───────────────────────────────────────────────────────────────
-->

# DISP-BUILD-commerce

- srs: SRS-CN-COMMERCE-BUILD-001
- status: in_progress
- mode: staging
- seat: BITS-CODEGEN
- operator: Dmitry Richard, mr.nobody@citadel-nexus.com
- branch: bits/SRS-CN-COMMERCE-BUILD-001-repair
- brief: .bits/srs/SRS-CN-COMMERCE-BUILD-001.md
- authorization_source: authenticated operator directive through Bits AI

## Authorization

The operator explicitly directed: "AUTHORIZED. Create SRS-CN-COMMERCE-BUILD-001
and DISP-BUILD-commerce (status in_progress)" and authorized lockfile, TS config,
ESLint, Vitest, Docker CI expressions, retained CodeQL/secret scan, real-build
attestations and end-to-end gh attestation verify. Bounds: new branch and one
PR separate from governance; no prod/deploy, push to main, settings or secrets
changes. Do not weaken or delete tests. Record blockers and all five npm results.
This is a local staging record, not a claim of a remote VCC database update.

## Tasks and gates

| Phase | Task | Gate |
| --- | --- | --- |
| A | Registry, SRS, dispatch and context | RecordsTests |
| B | Toolchain, lockfile and application tests | five npm commands below |
| C | Preserve security/CI; verify real signed output | WorkflowTests, BuildTests |
| D | Report and memory | MemoryTests |

```bash
set -euo pipefail
for phase in RecordsTests OwnershipTests WorkflowTests BuildTests MemoryTests; do
  if python .bits/checks/verify_governance.py "$phase"; then
    echo "PASS: $phase"
  else
    echo "FAIL: $phase"
    exit 1
  fi
done
```

Record independently (do not short-circuit the result table): `npm ci`,
`npm run lint`, `npm run typecheck`, `npm test`, `npm run build`.
Python checks require PyYAML 6.0.3. Dependency failures block application
acceptance, not independent authorized CI/documentation work. No Memory Brief
was supplied beyond the operator conversation. Grade fields remain pending.
