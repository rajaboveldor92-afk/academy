"""Offline structural and answer checks, independent of the Flutter runtime."""
import json
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]/'assets/data/school'

def validate():
    total, workshops = 0, 0
    for grade in (3, 5):
        curriculum = json.loads((BASE/f'technology_g{grade}.json').read_text())
        topics = {t['id']: t for t in curriculum['topics']}
        assert len(topics) == len(curriculum['topics']) == (20 if grade == 3 else 23)
        banks = defaultdict(list)
        ids = set()
        for item in json.loads((BASE/f'bank_technology_g{grade}.json').read_text())['items']:
            assert item['topic'] in topics and item['id'] not in ids
            ids.add(item['id']); total += 1
            assert item['q'].strip() and item['x'].strip() and item['h'].strip()
            assert 'Tasodifiy javob' not in json.dumps(item, ensure_ascii=False)
            banks[item['topic']].append(item)
            kind = item['t']
            if kind == 'choice':
                assert item['a'] not in item['w'] and len(set(item['w'])) == 3
            elif kind == 'order':
                assert len(item['parts']) >= 4 and len(set(item['parts'])) == len(item['parts'])
            elif kind == 'match':
                assert len(item['pairs']) >= 4
                for side in (0,1):
                    assert len({p[side] for p in item['pairs']}) == len(item['pairs'])
            elif kind == 'sort':
                assert len(item['items']) == 6 and len(item['bins']) == 2
                assert len({p[0] for p in item['items']}) == 6
                assert {p[1] for p in item['items']} == {0,1}
            elif kind == 'circuit':
                initial = item['wireA'] and item['wireB'] and item['switchClosed']
                assert initial != item['targetLit']
            else:
                raise AssertionError(kind)
        for t in topics.values():
            if t['generator'] == 'test':
                for level in t['levels']:
                    assert all(ref in topics and topics[ref]['generator'] != 'test' for ref in level['topics'])
                    for tag in t.get('tags', []):
                        if tag.startswith('track:'):
                            assert all(not topics[ref].get('tags') or tag in topics[ref]['tags'] for ref in level['topics'])
            elif t['generator'] == 'workshop':
                workshops += 1
                for level in t['levels']:
                    source = banks[level['source']]
                    assert sum(i['t'] in ('order','match','sort','circuit') for i in source) >= 8
            else:
                assert len(banks[t['id']]) >= 16
                assert len({i['q'] for i in banks[t['id']] if i['t'] != 'circuit'}) == sum(i['t'] != 'circuit' for i in banks[t['id']])
    assert workshops == 13 and total == 213
    print(f'PASS: {workshops} workshops, {total} items; answers, group targets, steps, pairs and circuit states validated')

if __name__ == '__main__':
    validate()
