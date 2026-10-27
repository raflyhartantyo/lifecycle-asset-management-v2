"""Validate release structure, source hashes, JSON contracts and local links."""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[2]
EXPECTED_FOLDERS = {'Power Apps', 'Power Automate', 'Others'}
folders = {p.name for p in ROOT.iterdir() if p.is_dir() and p.name != '.git'}
assert folders == EXPECTED_FOLDERS, ('Unexpected main folders', folders)
manifest = json.loads((ROOT / 'Others/releases/baseline-001/SOURCE-MANIFEST.json').read_text())
assert len(manifest['files']) == 88
assert len({f['destination'] for f in manifest['files']}) == 88
for item in manifest['files']:
    path = ROOT / item['destination']
    assert path.is_file(), ('Missing source', item['destination'])
    assert hashlib.sha256(path.read_bytes()).hexdigest() == item['sha256'], ('Changed baseline source', item['destination'])
json_files = list(ROOT.rglob('*.json'))
for path in json_files:
    json.loads(path.read_text(encoding='utf-8'))
apps = [p for p in (ROOT / 'Power Apps').iterdir() if p.is_dir()]
assert len(apps) == 1
app = apps[0]
screens = list((app / 'screens').glob('*.pa.yaml'))
assert len(screens) == 30
for screen in screens:
    assert (app / 'screen-guidance' / screen.name.replace('.pa.yaml', '.md')).is_file()
for name in ('IMPLEMENTATION.md', 'CLAUDE-HANDOVER.md', 'VALIDATION.md', 'SCREEN-INDEX.md'):
    assert (app / name).is_file()
flows = [p for p in (ROOT / 'Power Automate').iterdir() if p.is_dir()]
assert len(flows) == 15
count_actions = 0
for flow in flows:
    for name in ('definition.json', 'TRIGGER-CONTRACT.json', 'CONFIGURATION.json', 'ACTION-MAP.md', 'IMPLEMENTATION.md', 'CLAUDE-HANDOVER.md', 'VALIDATION.md'):
        assert (flow / name).is_file(), (flow.name, name)
    definition = json.loads((flow / 'definition.json').read_text())['properties']['definition']
    contract = json.loads((flow / 'TRIGGER-CONTRACT.json').read_text())
    assert contract['triggers'] == definition['triggers'], ('Trigger contract differs', flow.name)
    action_map = (flow / 'ACTION-MAP.md').read_text()
    def walk(actions, base):
        global count_actions
        for name, action in actions.items():
            ptr = base + '/' + name.replace('~', '~0').replace('/', '~1')
            assert ('`' + ptr + '`') in action_map or ptr.replace('|', '\\|') in action_map, ('Missing action pointer', flow.name, ptr)
            count_actions += 1
            walk(action.get('actions', {}), ptr + '/actions')
            walk(action.get('else', {}).get('actions', {}), ptr + '/else/actions')
            for case_name, case in action.get('cases', {}).items():
                walk(case.get('actions', {}), ptr + '/cases/' + case_name.replace('~', '~0').replace('/', '~1') + '/actions')
            walk(action.get('default', {}).get('actions', {}), ptr + '/default/actions')
    walk(definition.get('actions', {}), '/properties/definition/actions')
assert count_actions == 403, count_actions
bad_links = []
for path in ROOT.rglob('*.md'):
    text = path.read_text(encoding='utf-8')
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
        target = target.strip('<>')
        url = urlparse(target)
        if url.scheme or target.startswith('#'):
            continue
        relative = unquote(target.split('#', 1)[0])
        if relative and not (path.parent / relative).exists():
            bad_links.append((str(path.relative_to(ROOT)), target))
assert not bad_links, ('Broken local links', bad_links)
print('PASS: exactly 3 main folders; 88 preserved sources; 1 app / 30 YAML guides; 15 flow handovers; 403 action references; all JSON and local Markdown links valid.')
