#!/usr/bin/env python3
"""Validate this repository's established task-module architecture (not per-book files).
Usage: python3 fidelity-ledger/check_module_layout.py REPOSITORY --metatool BOOKS_REPO
This checks structure, not behavioral quality or source fidelity.
"""
import argparse
import hashlib
import json
import re
import sys
import subprocess
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('repository', type=Path)
p.add_argument('--metatool', type=Path, required=True)
a = p.parse_args()
sys.path.insert(0, str(a.metatool))
from bookrefs.tokens import estimate_tokens
root = a.repository.resolve()
# In a checkout validate the publication index; unrelated untracked personal files
# belong to the local workspace, not to the distributed skill. Stage intended
# changes before running this check. A staging directory has no such exclusions.
if (root / '.git').exists():
    published = set(subprocess.check_output(['git', '-C', str(root), 'ls-files', '-z']).decode().split('\0')) - {''}
else:
    published = {str(f.relative_to(root)) for f in root.rglob('*') if f.is_file() or f.is_symlink()}
errors = []
checks = []
def check(condition, label):
    (checks if condition else errors).append(label)

required = ['SKILL.md', 'README.md', 'AGENTS.md', 'LICENSE', 'NOTICE.md', '.gitignore', 'CHANGELOG.md', 'fidelity-ledger/provenance.md']
for rel in required:
    check((root / rel).is_file(), f'present: {rel}')
core = (root / 'SKILL.md').read_text()
front = re.match(r'^---\n(.*?)\n---\n', core, re.S)
check(front is not None, 'front matter exists')
name = re.search(r'^name: ([a-z0-9-]+)$', front[1], re.M)[1]
check(name == 'us-study-to-career-advisor-for-law-students', 'correct renamed slug')
alias = root / '.agents/skills' / name
check(alias.is_symlink() and str(alias.readlink()) == '../..' and alias.resolve() == root, 'one relative discovery alias resolves to canonical root')
check(len(list((root / '.agents/skills').iterdir())) == 1, 'no duplicate discovery entries')
expected = {'calibration.md', 'toolbox.md', 'llm-pathway.md', 'legal-writing.md', 'personal-statements.md', 'humanizer.md', 'institutions.md', 'roles-and-organizations.md', 'recruitment-and-selection.md', 'fit-and-gatekeeping.md', 'career-transition-and-search.md', 'analytic-production.md'}
actual = {Path(f).name for f in published if f.startswith('references/') and f.endswith('.md')}
check(actual == expected, 'exactly 12 intended runtime modules; no maintainer or private files')
router = core.split('## Loading depth (host-agent note)')[-1]
for module in sorted(expected):
    check(f'(references/{module})' in router, f'core routes to {module}')
    text = (root / 'references' / module).read_text()
    if module in {'roles-and-organizations.md','recruitment-and-selection.md','fit-and-gatekeeping.md','career-transition-and-search.md','analytic-production.md'}:
        for term in ['**Sources:**','**Trigger:**','**What this file is:**','Vintage','## Decision rules']:
            check(term in text, f'{module} contains {term}')
        check(not re.search(r'^I (help|am|will|start|ask)\b',text,re.M), f'{module} has no duplicate expert voice')
        check(estimate_tokens(text) <= 8000, f'{module} below 8000-token module ceiling')
body = core[front.end():]
check(estimate_tokens(body) <= 4500, 'core body below 4500-token ceiling')
check('Default language:' in core and 'English' in core and 'explicitly requests' in core, 'core language rule is explicit')
check('Use English' in (root/'AGENTS.md').read_text(), 'project language agrees with core')
for f in [root/'README.md',root/'SKILL.md',root/'AGENTS.md'] + [root/'references'/m for m in sorted(expected)]:
    for link in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', f.read_text()):
        target=link.split('#')[0].strip('<>')
        if not target or re.match(r'^[a-zA-Z][\w+.-]*:',target): continue
        check((f.parent/target).exists(), f'local link resolves: {f.relative_to(root)} -> {target}')
readme=(root/'README.md').read_text()
headings=['## How it works','## Use it for','## Installation','## Example requests','## Repository layout','## Sources and their responsibilities','## Coverage and validation','## Limits','## License']
check(all(h in readme for h in headings) and [readme.index(h) for h in headings] == sorted(readme.index(h) for h in headings), 'README section order')
check(readme.split('\n\n')[1].startswith('I help'), 'README first-person introduction immediately below title')
check('23 source entries' in readme and '12 integrated modules' in readme, 'README counts match source/module architecture')
lic=(root/'LICENSE').read_text()
check('Copyright (c) 2026 Ariel Lee' in lic and lic.startswith('MIT License\n'), 'authorship and license title')
check('source books' not in lic.lower(), 'license scope prose stays outside LICENSE')
suite=json.loads((root/'fidelity-ledger/acceptance-suite.json').read_text())
check(len(suite['tasks']) == 17, '17 preserved and supplemental acceptance cases')
for part in ['development','final']:
    check({'apply','inapplicable','disagreement','unsupported'} <= {t['kind'] for t in suite['tasks'] if t['partition']==part},f'{part} covers all required scenario kinds')
check(json.loads((root/'fidelity-ledger/acceptance-status.json').read_text())['status']=='unrun','behavioral results not fabricated')
manifest=json.loads((root/'fidelity-ledger/source-manifest.json').read_text())
check(len(manifest['sources'])==11,'11 new source records')
check(all((root/'references'/m).exists() for s in manifest['sources'] for m in s['module']), 'source records point to real modules')
for glob in ['*.pdf','*.epub','full_text.txt','metadata.json','*.docx']:
    check(not any(Path(f).match(glob) for f in published),f'no published raw source or extraction artifacts: {glob}')
files=[root/'SKILL.md']+[root/'references'/m for m in sorted(expected)]
report={'status':'pass' if not errors else 'fail','file_scope':'git index' if (root/'.git').exists() else 'staging directory','checks_passed':len(checks),'errors':errors,'core_body_tokens':estimate_tokens(body),'module_tokens':{f.name:estimate_tokens(f.read_text()) for f in files[1:]},'runtime_sha256':{str(f.relative_to(root)):hashlib.sha256(f.read_bytes()).hexdigest() for f in files},'limitations':['Structural check only; does not establish source completeness or behavioral acceptance.','Generic per-book reference naming is deliberately inapplicable to this existing module architecture.']}
print(json.dumps(report,indent=2))
raise SystemExit(bool(errors))
