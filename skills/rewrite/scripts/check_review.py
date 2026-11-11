#!/usr/bin/env python3
"""Check review provenance, not scientific correctness or readability."""
import hashlib
import json
import sys
from pathlib import Path


def check(path):
    data = json.loads(path.read_text())
    draft = (path.parent / data['draft_file']).read_text()
    final_path = path.parent / data['final_file']
    final = final_path.read_text()
    errors = []
    if hashlib.sha256(final_path.read_bytes()).hexdigest() != data['final_sha256']:
        errors.append('Final file hash does not match reviewed version')
    for field in ('content_judgment', 'reviewer'):
        if not isinstance(data.get(field), str) or not data[field].strip():
            errors.append('Missing ' + field)
    if not isinstance(data.get('unresolved'), list) or data['unresolved']:
        errors.append('Unresolved items are missing or nonempty')
    if not isinstance(data.get('repairs'), list):
        errors.append('Missing repair records')
    for item in data.get('repairs', []):
        if not item.get('before') or item['before'] not in draft:
            errors.append('Before quote not found in draft')
        if not item.get('gap', '').strip():
            errors.append('Missing explanation of gap')
        if not item.get('after') or item['after'] not in final:
            errors.append('After quote not found in final')
    if not isinstance(data.get('reader_traces'), list) or not data['reader_traces']:
        errors.append('Missing reader traces')
    for item in data.get('reader_traces', []):
        if not item.get('question', '').strip() or not item.get('answer', '').strip():
            errors.append('Missing trace question or answer')
        quotes = item.get('evidence')
        if not isinstance(quotes, list) or not quotes or any(not q or q not in final for q in quotes):
            errors.append('Trace evidence not found in final')
    if errors:
        raise ValueError('\n'.join(errors))
    print(f"Verified version and quoted evidence: {len(data['repairs'])} repairs, "
          f"{len(data['reader_traces'])} traces. Readability still requires semantic review.")


if __name__ == '__main__':
    try:
        check(Path(sys.argv[1]).resolve())
    except (IndexError, KeyError, OSError, ValueError, TypeError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
