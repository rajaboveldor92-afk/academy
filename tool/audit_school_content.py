"""Audit current declared grade coverage without equating files to a complete textbook."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def audit():
    source = (ROOT/'lib/models/subject.dart').read_text()
    rows, missing = [], []
    for name, body in re.findall(r'  (\w+)\(\n(.*?)\n  \)[,;]', source, re.S):
        match = re.search(r'grades: \[(.*?)\]', body)
        if match is None:
            continue
        grades = [int(n) for n in re.findall(r'\d+', match[1])]
        if not grades:
            continue
        suffix = re.search(r"schoolSuffix: '(.*?)'", body)
        cells = []
        for grade in range(1, 9):
            if grade not in grades:
                cells.append('—'); continue
            path = ROOT/'assets/data'/((name+'_'+suffix[1] if suffix else 'school/'+name+'_g'+str(grade))+'.json')
            if path.exists():
                data = json.loads(path.read_text())
                count = sum(t.get('generator') != 'test' for t in data['topics'])
                cells.append(str(count))
            else:
                missing.append((name, grade)); cells.append('yo‘q')
        rows.append('| '+name+' | '+' | '.join(cells)+' |')
    text = '''# Academy Maktab: sinf va fan qamrovi

Koddagi joriy qamrov. Raqam — fayldagi asosiy/amaliy mavzular soni; nazorat ishlari hisoblanmagan.
`yo‘q` — fan shu sinf uchun e’lon qilingan, ammo kontent fayli yo‘q; `—` — shu sinf uchun e’lon qilinmagan.
Fayl mavjudligi darslik yoki davlat o‘quv dasturi 100% qamralganini anglatmaydi.

| Fan | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
'''+ '\n'.join(rows)+f'''\n
Hali kontent fayli bo‘lmagan sinf–fan juftliklari: **{len(missing)}**.

Texnologiya: 3- va 5-sinfda har biri 4 asosiy mavzu + 4 amaliy ustaxona + 5 nazorat/takrorlash mavzusi.
Asosiy mavzulardagi eski takroriy banklar mavzuga mos 128 ta original mashq va 5 ta virtual zanjir topshirig‘i bilan almashtirildi.
Ustaxona har safar 6 ta interaktiv mashq beradi; tanlash testi bu mashg‘ulotga kirmaydi.
Saralash va ketma-ketlik kartalari telefonda o‘qiladigan matn bilan ko‘rsatiladi.
Virtual zanjir ideal batareya–kalit–lampochka modelidir: qarshilik yoki tok miqdori hisoblanmaydi.
Elektr xavfsizligi haqidagi amaliy ma’lumotlar virtual mashq bilan cheklangan.
Tarix fan menyusida o‘chirilgan; eski fayllar texnik moslik uchun qolgan.
Texnologiya boshqa sinflar uchun hali e’lon qilinmagan.

Qamrovdagi qolgan bo‘shliqlar quyidagicha:
'''+ '\n'.join(f'- {subject}: {", ".join(str(g) for s,g in missing if s==subject)}-sinf' for subject in dict.fromkeys(s for s,_ in missing))+ '\n'
    target = ROOT/'docs/school-content-audit.md'
    target.parent.mkdir(exist_ok=True)
    target.write_text(text)
    print(f'Audit: {len(rows)} subjects, {len(missing)} missing declared grade/subject files')
    return missing

if __name__ == '__main__':
    audit()
