<!--
# ─── CGRF Header ───────────────────────────────────────────────
# File:        .github/BUILD.md
# Stage:       11_COMMIT
# SRS:         SRS-CN-COMMERCE-BUILD-001
# CAPS:        pending
# CK:          pending
# Dispatch:    DISP-BUILD-commerce
# Seat:        BITS-CODEGEN
# Owner:       Citadel Nexus Inc.
# Created:     2026-10-20
# Depends:     .github/workflows/lockfile-refresh.yml, GOVERNANCE.md
# EnumType:    Doc
# EnumEdges:   DEPENDS_ON .github/workflows/lockfile-refresh.yml; DEPENDS_ON GOVERNANCE.md
# DAG Node:    none
# Intent:      Explain authenticated lockfile generation and the remaining administrator gates.
# ───────────────────────────────────────────────────────────────
-->

# Commerce build and lockfile refresh

SRS: SRS-CN-COMMERCE-BUILD-001. Dispatch: DISP-BUILD-commerce.

## Manual lockfile flow

After this workflow is merged, open Actions → Refresh Commerce lockfile → Run
workflow and select the default branch. It has only `workflow_dispatch`; selecting
another branch skips validation and publication. `.nvmrc` selects Node 20, matching
existing CI. No schedule, push or PR event generates a lockfile automatically.

The validation job checks out the dispatched SHA, configures setup-node for
`@citadel-guilds` on `https://npm.pkg.github.com`, and supplies the ephemeral
GITHUB_TOKEN as NODE_AUTH_TOKEN. It has only contents:read and packages:read.
The SDK must actually be published as `@citadel-guilds/sdk` in that registry;
permission alone cannot create or rename a package. Confirm the scope/owner and
package availability with its maintainer before dispatching. Other scopes use
the normal npm registry. Do not commit an auth-bearing .npmrc or a token.

It runs `npm install --package-lock-only --ignore-scripts`, followed by:

```bash
npm ci && npm run lint && npm run typecheck && npm test && npm run build
```

A failure stops publication. The repository's existing tests and coverage gates
remain required. The workflow records the successful run and transfers only the
real lockfile and its report/memory evidence by immutable artifact ID. There is
no fabricated lockfile in this change; package-lock.cgrf.yaml describes the
future generated file without substituting for it.

A separate job has contents:write and pull-requests:write, with no package
permission or dependency execution. It commits only the downloaded lockfile and
evidence on `bits/lockfile-refresh`, then opens a PR against the default branch.
If the tracked lockfile is unchanged, it skips the commit/PR.
It never pushes to the default branch, never force-pushes, never merges, and
refuses an existing branch. Review an existing refresh PR before rerunning;
a maintainer can remove the fixed branch after merge/closure. If PR creation
fails after the branch push, open a PR from that branch manually rather than
rerunning or deleting unreviewed work. Runs are serialized by concurrency.

Every action in lockfile-refresh.yml is pinned to a full commit SHA. The npm
validation job never receives write permissions. The workflow does not publish
an npm package, build/push a container, deploy, sign artifacts, or change settings.

## Administrator prerequisites

- Enable Actions and allow the pinned checkout/setup-node/upload/download actions.
  Enable the repository option allowing Actions to create pull requests, subject
  to organization policy. The workflow's two jobs request only the permissions
  needed for reading packages and proposing a branch/PR.
- Grant this repository's GITHUB_TOKEN read access in the SDK package's **Manage
  Actions access** settings. `packages: read` does not grant access to a package
  that has not authorized this repository. SDK maintainers must verify the
  `@citadel-guilds` package scope; it is not inferred from the repo organization.
- TODO only if package policy cannot use GITHUB_TOKEN: an admin may provision an
  approved `SDK_PACKAGES_READ_TOKEN` secret with package-read access, then update
  the two NODE_AUTH_TOKEN bindings in a separately reviewed change. This workflow
  does not read that TODO secret, create secrets, or request a token from users.
- Configure the default-branch ruleset: PR/code-owner approval, signed commits,
  successful required checks, conversation resolution, no force pushes or
  deletion, and no unapproved bypasses. The refresh bot commit is unsigned;
  arrange an approved signing integration or a human signed replacement before
  merge when signing is required. Do not disable signing to make this flow pass.
- GITHUB_TOKEN-created PR/push events do not trigger other workflows. The five
  checks in the manual run are evidence, not automatic satisfaction of required
  PR check contexts. Arrange a trusted human-authored follow-up commit or a
  separately approved App-token integration to trigger PR CI before merge.
- The existing CI/provenance npm-install steps do not yet configure scoped SDK
  authentication. Apply the same package-read authorization and setup-node/
  NODE_AUTH_TOKEN configuration to those jobs in a reviewed follow-up before
  requiring them for private-SDK builds. This manual workflow validates its own
  install; a generated lockfile does not itself authenticate other workflows.
- For the separate provenance workflow, allow Actions artifact attestations and
  id-token OIDC (`attestations: write`, `id-token: write` on its signer). The
  refresh workflow has neither signing permission. Keep those changes admin-only.

GitHub CODEOWNERS remains `@citadel-nexus/guild-commerce`, with Alex's automation
identity `alex-commerce-guildmaster`. No ownership confirmation is outstanding.
No settings or secrets were changed by this session.

## Provenance and local evidence

The existing provenance workflow attests only successful real main-build output.
Its read-only verification job uses `gh attestation verify` and tests rejection
of tampered bytes, wrong commit and wrong workflow identity. See GOVERNANCE.md
for exact verification flags. A successful lockfile refresh does not prove live
attestation issuance; that requires a successful main push and admin enablement.

Offline sandbox checks cannot resolve the uncached SDK or generate a real npm
lockfile. The current results and exact limitations are in
.bits/out/DISP-BUILD-commerce/report.md. No workflow was dispatched here.

## Session publication

PR #19 already merged the previous build-repair commit. The session's UI-bound
branch was fast-forwarded to current main at
5dc37392985348cfb1749dbd70175699e1738967, preserving all published history.
Only the lockfile-refresh follow-up is new relative to that base. No duplicate
replay/rebase of already merged commits is necessary. The coding UI controls
creation of the next PR and may adapt the published branch name; local Git and
PR metadata preparation cannot guarantee that external UI action or publish refs.
