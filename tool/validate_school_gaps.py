"""Check every added course and bank without requiring Flutter."""
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT/'assets/data/school'
MISSING = {'english':[7,8], 'russian':[2,7,8], 'onatili':[7,8],
 'reading':[2,7,8], 'informatics':[1,2,7,8], 'geography':[7,8],
 'biology':[7,8], 'physics':[7,8], 'chemistry':[7,8]}


def validate():
    index = json.loads((BASE/'index.json').read_text())
    count = 0
    for subject, grades in MISSING.items():
        for grade in grades:
            name = f'{subject}_g{grade}'
            assert name in index['curricula'] and 'bank_'+name in index['banks']
            course = json.loads((BASE/(name+'.json')).read_text())
            assert course['subject'] == subject and course['ageGroup'] == f'g{grade}'
            topics = {t['id']:t for t in course['topics']}
            assert len(topics) == 9
            banks = defaultdict(list)
            ids = set()
            for it in json.loads((BASE/('bank_'+name+'.json')).read_text())['items']:
                assert it['topic'] in topics and it['id'] not in ids
                ids.add(it['id']); banks[it['topic']].append(it); count += 1
                assert it['q'].strip() and it['x'].strip()
                if it['t'] == 'choice':
                    assert len(set(it['w'])) == 3 and it['a'] not in it['w']
                elif it['t'] == 'match':
                    assert all(len({p[side] for p in it['pairs']}) == len(it['pairs']) for side in (0,1))
                elif it['t'] == 'tf':
                    assert type(it['a']) is bool
                else:
                    raise AssertionError(it['t'])
                if subject == 'reading':
                    assert len(it['text']) > 200 and it['text'] in topics[it['topic']]['theory']['uz']
            for t in topics.values():
                if t['generator'] == 'test':
                    assert all(ref in topics and topics[ref]['generator'] == 'bank' for lv in t['levels'] for ref in lv['topics'])
                else:
                    pool = banks[t['id']]
                    assert t['theory']['uz'] and t['chapter']
                    assert len(pool) >= 15 and sum(it['d'] <= 1 for it in pool) >= 8
                    assert len({it['q'] for it in pool}) == len(pool)
    assert count == 1560
    print(f'PASS: 22 courses, 88 authored units, {count} tasks, 110 tests/reviews; references and answer structures verified')


if __name__ == '__main__':
    validate()
