<!--
# ─── CGRF Header ───────────────────────────────────────────────
# File:        GOVERNANCE.md
# Stage:       06_PLAN
# SRS:         SRS-CN-COMMERCE-GOVERNANCE-001
# CAPS:        pending
# CK:          pending
# Dispatch:    DISP-GOVERNANCE-commerce
# Seat:        BITS-CODEGEN
# Owner:       Citadel Nexus Inc.
# Created:     2026-10-20
# Depends:     .github/CODEOWNERS, .github/workflows/provenance.yml
# EnumType:    Doc
# EnumEdges:   DEPENDS_ON .github/CODEOWNERS; DEPENDS_ON .github/workflows/provenance.yml
# DAG Node:    none
# Intent:      Make Commerce approval authority and artifact trust requirements explicit.
# ───────────────────────────────────────────────────────────────
-->

# Commerce Guild governance

Owner: Citadel Nexus Inc.
Guildmaster: **Alex**, GitLab user `alex`.
Datadog team: **guild-commerce**.

## Charter and decisions

Commerce owns sales and onboarding: **Scope Sheet Pro, leads, walk-in, CTA and
provisioning**. The guildmaster is accountable for priorities, public contracts,
review delegation and acceptance. Scope changes and cross-guild interfaces need
an explicit decision in the PR or linked issue before implementation.

Every change uses a PR with an SRS reference, passing required checks and at
least one independent code-owner approval. Authors cannot approve their own
changes. Alex approves governance/ownership/provenance policy changes; a
recorded Commerce delegate may approve routine work. For `src/index.ts` public
interface changes, obtain both Commerce and SDK review. GitHub CODEOWNERS treats
owners on a line as alternatives, so requiring both is a policy reviewers must
check; a single required code-owner review cannot enforce both approvals.

Escalate unresolved disagreement, guildmaster unavailability, cross-guild scope,
and exceptions to the **guildmasters group** through a linked issue/PR decision.
Record the decision, approver and affected SRS. Do not invent a GitHub group
handle. Security reports follow SECURITY.md, not a public issue. Exceptions
require an explicit decision and audit trail; they do not authorize bypassing
repository protections. A rollback is a reviewed revert subject to the same
rules. Policy changes require Alex or a documented guildmasters-group delegate.

## GitHub ownership mapping

`.github/CODEOWNERS` names Alex as accountable guildmaster and uses the existing
`@citadel-nexus/guild-commerce-leads` team for GitHub routing. Alex's GitLab login
does not establish his GitHub login. Before enabling required owner reviews,
an admin must confirm the team exists, is visible, has explicit write access,
and contains Alex's verified GitHub account. Preserve `sdk-core` access for SDK
review. Confirm GitHub reports no CODEOWNERS errors and actually requests review
on a test PR. Do not replace the team with an unverified `@alex` account.

## Default-branch protection: administrator action required

The verified default branch is `main`. There is no repository settings/ruleset
manager in this repo; this document specifies the configuration an admin must
apply in **Settings → Rules → Rulesets**. Committing these files does not enable
GitHub protections or change organization settings.

Create an active branch ruleset targeting the **default branch**:

- Require a pull request, at least one approving review, and code-owner review.
- Dismiss stale approvals after new commits, require approval of the most recent
  reviewable push by someone other than its pusher, and resolve conversations.
- Require signed commits. Contributors need a GitHub-verified signing identity;
  choose merge methods that preserve compliance and check the bot/UI path too.
- Require status checks and branches up to date before merging. Select the
  actual GitHub Actions check contexts after they have run: existing CI `build`,
  security `codeql` and `secret-scan`, and new `Governance policy` and
  `Provenance build`. Bind to the GitHub Actions integration. Confirm displayed
  names in a PR; do not guess workflow-prefixed context names.
- Block force pushes and deletion. Apply to admins as well; leave the bypass
  list empty unless the guildmasters group explicitly approves a recorded
  exception. Do not enable merge queue without adding `merge_group` CI support.

The existing security workflow does not run on PRs. Before requiring its
`codeql` and `secret-scan` contexts, an admin/maintainer must arrange PR coverage
in a separately authorized change and verify the contexts on a PR head. Likewise,
repair the missing package lockfile, TypeScript configuration and lint/test
setup before activating build requirements. These prerequisites are not waived;
activating checks prematurely will block merges. Do not require the push-only
`docker`, `release` or `Sign build provenance` jobs as PR checks.

Enable Actions and allow checkout/setup-node/upload/download-artifact plus
`actions/attest-build-provenance@v3`. Review action version updates; version tags
follow the repository convention and are not immutable SHA pins. Permit the
signing job's `id-token: write` and `attestations: write` permissions; do not
broadly grant write access to PR workflows. This public repo can use GitHub
artifact attestations with Sigstore's public transparency service; build
identity/provenance metadata is public. No stored signing key or new secret is
needed. Confirm any organization Actions/attestation policy permits this.

## Signed build artifacts

`.github/workflows/provenance.yml` runs governance validation and the existing
Node 20 install/lint/test/build sequence on PRs and pushes to `main`. Its build
job has read-only repository access and uploads only an npm `.tgz` assembled
from compiled `dist/` and `package.json`. It does not run package lifecycle
scripts during packing or include the checkout, `.env`, governance records,
credentials, or `node_modules`. `dist/index.js` must exist and be nonempty.

A separate signing job runs only for a successful push build on `refs/heads/main`
in `citadel-nexus/guild-commerce`. It downloads the immutable artifact ID from
that build in the same run, without checking out or executing repository code.
GitHub's attest-build-provenance action creates a SLSA provenance v1 statement
whose subject is the archive SHA-256, signed using a short-lived Sigstore
certificate bound to GitHub Actions OIDC. This signed attestation supplies
artifact signing and provenance together; a separate long-lived key or detached
cosign signature is unnecessary. The bundle is retained as a second workflow
artifact, and the attestation is registered with GitHub.

PR artifacts are unsigned. The signer has no PR, tag or manual trigger. Artifact
retention is 30 days, so consumers needing longer retention must retain the exact
archive and its bundle. Build/signing does not publish a package, container or
release. Existing npm releases and Docker outputs are **not covered** by this
workflow's attestation; do not infer their provenance from this archive.

This is build provenance, not a certified SLSA level or proof of safe code.
Same-repository workflow changes are within the trust boundary. Required owner
review and protected signed history must be enabled to enforce that boundary.
The repository currently lacks build prerequisites; signing fails closed until
a separately authorized change repairs them and all build checks succeed.

## Verify before using an artifact

Use a recent GitHub CLI with `gh attestation verify`. Independently obtain the
expected 40-character commit SHA from the reviewed main-branch change and choose
its successful **Build provenance — guild-commerce** push run. Authenticate the
CLI normally for Actions downloads; no credential belongs in this repo.

```bash
REPO=citadel-nexus/guild-commerce
# Set RUN_ID and COMMIT_SHA to the reviewed run and expected source commit.
: "${RUN_ID:?Set the successful main push run ID}"
: "${COMMIT_SHA:?Set the independently reviewed source commit SHA}"
gh run view "$RUN_ID" --repo "$REPO" \
  --json event,headBranch,headSha,conclusion,workflowName
# Confirm event=push, headBranch=main, headSha=$COMMIT_SHA and conclusion=success.
gh run download "$RUN_ID" --repo "$REPO" \
  --name "commerce-build-$COMMIT_SHA" --dir ./commerce-build
gh run download "$RUN_ID" --repo "$REPO" \
  --name "commerce-provenance-$COMMIT_SHA" --dir ./commerce-provenance

gh attestation verify ./commerce-build/citadel-guilds-commerce-*.tgz \
  --repo "$REPO" \
  --signer-workflow "$REPO/.github/workflows/provenance.yml" \
  --source-ref refs/heads/main \
  --source-digest "$COMMIT_SHA" \
  --predicate-type https://slsa.dev/provenance/v1 \
  --deny-self-hosted-runners
```

Use a fresh download directory containing exactly one archive. Verification must
exit zero and report the expected repository, source commit, predicate and
workflow identity; otherwise reject the artifact. A checksum alone does not
prove its origin. Verify the stored bundle using the same policy flags plus
`--bundle ./commerce-provenance/attestation.jsonl` when needed. Bundle retention
does not imply all trust-root material for fully offline verification is cached.

After the first real signed run, test verification on an unchanged archive,
then on a copy with one byte appended; the latter must fail. Also verify the
original with a different expected source SHA and a different signer-workflow;
both must fail. Do not deploy or execute an artifact as part of these tests.
These live OIDC/transparency/verification tests must run on GitHub after merge;
local static checks cannot demonstrate issuance or signature verification.
