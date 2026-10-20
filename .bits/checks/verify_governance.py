# ─── CGRF Header ───────────────────────────────────────────────
# File:        .bits/checks/verify_governance.py
# Stage:       11_COMMIT
# SRS:         SRS-CN-COMMERCE-GOVERNANCE-001
# CAPS:        pending
# CK:          pending
# Dispatch:    DISP-GOVERNANCE-commerce
# Seat:        BITS-CODEGEN
# Owner:       Citadel Nexus Inc.
# Created:     2026-10-20
# Depends:     .github/workflows/provenance.yml, .github/CODEOWNERS, .bits/out/DISP-GOVERNANCE-commerce/memory.json
# EnumType:    Test
# EnumEdges:   VALIDATES .github/workflows/provenance.yml; VALIDATES .github/CODEOWNERS; VALIDATES .bits/out/DISP-GOVERNANCE-commerce/memory.json
# DAG Node:    none
# Intent:      Test the provenance trust boundary and governance record consistency.
# ───────────────────────────────────────────────────────────────

"""Validate Commerce governance and its artifact trust boundary."""

from __future__ import annotations

import json
import os
from pathlib import Path
import re
import subprocess
import tarfile
import tempfile
import unittest
from typing import Any, cast

# PyYAML is a runtime-only CI dependency; validate parsed shapes in the tests.
import yaml  # type: ignore[import-untyped]

ROOT = Path(__file__).resolve().parents[2]
SRS = 'SRS-CN-COMMERCE-GOVERNANCE-001'
DISPATCH = 'DISP-GOVERNANCE-commerce'
OUT = ROOT / '.bits/out' / DISPATCH


def workflow() -> dict[str, Any]:
    """Load the workflow without YAML 1.1 boolean coercion of on."""
    return cast(dict[str, Any], yaml.load((ROOT / '.github/workflows/provenance.yml').read_text(), Loader=yaml.BaseLoader))


def permits_signing(condition: str, event: str, ref: str, repo: str) -> bool:
    """Evaluate the deliberately restricted signing guard grammar."""
    context = {'event_name': event, 'ref': ref, 'repository': repo}
    result = True
    for clause in condition.split('&&'):
        match = re.fullmatch(r"\s*github\.(event_name|ref|repository)\s*==\s*'([^']+)'\s*", clause)
        if match is None:
            raise ValueError('Unsupported signing condition')
        result = result and context[match[1]] == match[2]
    return result


class RecordsTests(unittest.TestCase):
    def test_authorization_and_scope(self) -> None:
        registry = yaml.safe_load((ROOT / '.bits/srs_registry.yml').read_text())
        self.assertIn('SRS-CN-COMMERCE-LIVINGWORLD-001', registry)
        self.assertEqual(registry[SRS]['dispatch'], DISPATCH)
        self.assertEqual(registry[SRS]['status'], 'in_progress')
        queue = (ROOT / '.bits/queue' / f'{DISPATCH}.md').read_text()
        for value in ('status: in_progress', 'mr.nobody@citadel-nexus.com', '"create those"', 'mode: staging'):
            self.assertIn(value, queue)
        for path in ('AGENTS.md', 'CLAUDE.md', '.bits/context.md', f'.bits/srs/{SRS}.md'):
            self.assertIn(SRS if path != 'CLAUDE.md' else 'Commerce', (ROOT / path).read_text())

    def test_registered_paths_have_headers(self) -> None:
        memory = json.loads((OUT / 'memory.json').read_text())
        for entry in memory['entries']:
            if entry['type'] != 'A':
                continue
            path = ROOT / entry['file_path']
            header_path = path.with_suffix('.cgrf.yaml') if path.suffix == '.json' else path
            header = header_path.read_text().split('# ───────────────────────────────────────────────────────────────', 1)[0]
            for field, value in (('SRS', SRS), ('Dispatch', DISPATCH), ('Owner', 'Citadel Nexus Inc.'),
                                 ('CK', 'pending'), ('CAPS', 'pending')):
                self.assertRegex(header, rf'# {field}:\s+{re.escape(value)}')
            self.assertIn(entry['cket_stage'], header)


class OwnershipTests(unittest.TestCase):
    def test_guildmaster_and_sdk_stewardship(self) -> None:
        owners = (ROOT / '.github/CODEOWNERS').read_text()
        rules = [line.split() for line in owners.splitlines() if line.strip() and not line.startswith('#')]
        self.assertIn(['*', '@citadel-nexus/guild-commerce'], rules)
        interface = next(rule for rule in rules if rule[0] == 'src/index.ts')
        self.assertIn('@citadel-nexus/guild-commerce', interface)
        self.assertIn('@citadel-nexus/sdk-core', interface)
        self.assertIn('Alex (GitLab: alex)', owners)
        rule_owners = [owner for rule in rules for owner in rule[1:]]
        self.assertNotIn('@alex', rule_owners)
        self.assertFalse(any('alex-commerce-guildmaster' in owner for owner in rule_owners))

    def test_charter_and_verification_policy(self) -> None:
        charter = (ROOT / 'GOVERNANCE.md').read_text()
        for value in ('Scope Sheet Pro', 'leads', 'walk-in', 'CTA', 'provisioning', 'guildmasters group',
                      'Require signed commits', 'code-owner review', 'Require status checks',
                      '@citadel-nexus/guild-commerce', 'alex-commerce-guildmaster',
                      'Expected automation actor', 'GitHub Apps cannot be code owners',
                      '--source-digest', '--source-ref refs/heads/main', '--signer-workflow',
                      '--deny-self-hosted-runners', '--predicate-type https://slsa.dev/provenance/v1'):
            self.assertIn(value, charter)


class WorkflowTests(unittest.TestCase):
    def test_trigger_and_signer_trust_matrix(self) -> None:
        config = workflow()
        self.assertEqual(set(config['on']), {'push', 'pull_request'})
        for trigger in config['on'].values():
            self.assertEqual(trigger['branches'], ['main'])
        guard = config['jobs']['attest']['if']
        for event in ('push', 'pull_request', 'pull_request_target', 'workflow_dispatch', 'workflow_run'):
            for ref in ('refs/heads/main', 'refs/heads/feature', 'refs/tags/v1.0.0', 'refs/pull/1/merge'):
                for repo in ('citadel-nexus/guild-commerce', 'fork/guild-commerce'):
                    with self.subTest(event=event, ref=ref, repo=repo):
                        expected = event == 'push' and ref == 'refs/heads/main' and repo == 'citadel-nexus/guild-commerce'
                        self.assertEqual(permits_signing(guard, event, ref, repo), expected)

    def test_guard_rejects_unreviewed_expression_forms(self) -> None:
        with self.assertRaises(ValueError):
            permits_signing("always() || github.event_name == 'push'", 'pull_request', 'refs/heads/main', 'fork/guild-commerce')

    def test_builds_cannot_issue_signatures(self) -> None:
        config = workflow()
        self.assertEqual(config['permissions'], {'contents': 'read'})
        jobs = config['jobs']
        for name in ('build', 'governance'):
            effective = jobs[name].get('permissions', config['permissions'])
            self.assertFalse(any(value == 'write' for value in effective.values()))
            for step in jobs[name]['steps']:
                if step.get('uses', '').startswith('actions/checkout@'):
                    self.assertEqual(step['with']['persist-credentials'], 'false')
        self.assertEqual(jobs['attest']['permissions'], {
            'contents': 'read', 'actions': 'read', 'id-token': 'write', 'attestations': 'write'})

    def test_signer_requires_success_and_executes_no_repo_code(self) -> None:
        jobs = workflow()['jobs']
        self.assertEqual(jobs['build']['needs'], 'governance')
        self.assertEqual(jobs['attest']['needs'], 'build')
        self.assertNotIn('continue-on-error', jobs['build'])
        for job in jobs.values():
            self.assertEqual(job['runs-on'], 'ubuntu-latest')
            for step in job['steps']:
                self.assertNotIn('continue-on-error', step)
        for step in jobs['attest']['steps']:
            self.assertNotIn('run', step)
            self.assertFalse(step['uses'].startswith('actions/checkout@'))
        commands = [step['run'] for step in jobs['build']['steps'] if 'run' in step]
        self.assertEqual(commands[:4], ['npm ci', 'npm run lint', 'npm test', 'npm run build'])

    def test_signer_downloads_exact_same_run_artifact(self) -> None:
        jobs = workflow()['jobs']
        download = next(step for step in jobs['attest']['steps'] if step['uses'].startswith('actions/download-artifact@'))
        self.assertEqual(download['with']['artifact-ids'], '${{ needs.build.outputs.artifact-id }}')
        self.assertNotIn('run-id', download['with'])
        self.assertNotIn('repository', download['with'])
        self.assertNotIn('name', download['with'])
        self.assertEqual(jobs['build']['outputs']['artifact-id'], '${{ steps.upload.outputs.artifact-id }}')
        attest = next(step for step in jobs['attest']['steps'] if step['uses'].startswith('actions/attest-build-provenance@'))
        self.assertEqual(attest['with']['subject-path'], download['with']['path'] + '/*.tgz')
        uploads = [step for job in jobs.values() for step in job['steps'] if step.get('uses', '').startswith('actions/upload-artifact@')]
        self.assertEqual(len(uploads), 2)
        for upload in uploads:
            self.assertEqual(upload['with']['if-no-files-found'], 'error')

    def test_pack_excludes_checkout_and_disables_lifecycle_scripts(self) -> None:
        command = next(step['run'] for step in workflow()['jobs']['build']['steps'] if step.get('name') == 'Pack compiled distribution')
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            checkout, runner = root / 'checkout', root / 'runner'
            checkout.mkdir()
            runner.mkdir()
            (checkout / 'dist').mkdir()
            (checkout / 'dist/index.js').write_text('export const fixture = true;\n')
            (checkout / '.env').write_text('FIXTURE=must-not-ship\n')
            (checkout / 'source.ts').write_text('not compiled\n')
            (checkout / 'package.json').write_text(json.dumps({
                'name': '@citadel-guilds/commerce', 'version': '0.1.0', 'main': 'dist/index.js',
                'scripts': {'prepack': 'exit 99', 'prepare': 'exit 99', 'postpack': 'exit 99'},
            }))
            result = subprocess.run(['bash', '-c', command], cwd=checkout, env={**os.environ, 'RUNNER_TEMP': str(runner), 'npm_config_offline': 'true'}, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            archives = list((runner / 'commerce-artifacts').glob('*.tgz'))
            self.assertEqual(len(archives), 1)
            with tarfile.open(archives[0]) as archive:
                files = {member.name for member in archive if member.isfile()}
            self.assertEqual(files, {'package/dist/index.js', 'package/package.json'})

    def test_missing_compiled_output_cannot_be_packaged(self) -> None:
        command = next(step['run'] for step in workflow()['jobs']['build']['steps'] if step.get('name') == 'Pack compiled distribution')
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(['bash', '-c', command], cwd=directory, env={**os.environ, 'RUNNER_TEMP': directory}, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(list(Path(directory).rglob('*.tgz')))


class MemoryTests(unittest.TestCase):
    def test_counts_ioo_and_no_orphans(self) -> None:
        payload = json.loads((OUT / 'memory.json').read_text())
        entries, summary = payload['entries'], payload['summary']
        self.assertEqual(list(payload)[-1], 'summary')
        self.assertEqual(summary['dispatch_id'], DISPATCH)
        for kind in ('A', 'B', 'C'):
            self.assertEqual(summary[f'type_{kind.lower()}_count'], sum(entry['type'] == kind for entry in entries))
        edges = [entry for entry in entries if entry['type'] == 'B']
        connected = {entry[key] for entry in edges for key in ('source', 'target')}
        for entry in entries:
            self.assertEqual(entry['dispatch_id'], DISPATCH)
            if entry['type'] == 'A':
                for key in ('intent_statement', 'objective_id', 'outcome'):
                    self.assertTrue(entry[key])
                self.assertIsNotNone(entry['supersedes'])
                self.assertIn(entry['file_path'], connected)
                self.assertEqual(entry['lines'], len((ROOT / entry['file_path']).read_text().splitlines()))
            elif entry['type'] == 'C':
                from datetime import datetime
                self.assertIsNotNone(datetime.fromisoformat(entry['timestamp']).tzinfo)
        self.assertTrue(summary['ioo_compliance'])
        self.assertEqual(summary['dkg_orphans'], 0)

    def test_header_edges_match_memory(self) -> None:
        entries = json.loads((OUT / 'memory.json').read_text())['entries']
        actual = {(entry['source'], entry['edge_type'], entry['target']) for entry in entries if entry['type'] == 'B'}
        expected = set()
        for entry in entries:
            if entry['type'] != 'A':
                continue
            path = ROOT / entry['file_path']
            if path.suffix == '.json':
                companion = yaml.safe_load(path.with_suffix('.cgrf.yaml').read_text())
                declarations = companion['enum_edges']
            else:
                match = re.search(r'^# EnumEdges:\s+(.+)$', path.read_text(), re.MULTILINE)
                assert match is not None, f'Missing EnumEdges: {path}'
                declarations = match[1]
            for declaration in declarations.split(';'):
                verb, target = declaration.strip().split(' ', 1)
                expected.add((entry['file_path'], verb, target))
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
