# Yozish (tracing) uchun harf, raqam va chiziqlar: `python3 tool/content/glyphs_src.py`
# -> assets/data/glyphs.json. Koordinatalar 0..1 kvadratda (y pastga), har bir
# chiziq (stroke) — nuqtalar ketma-ketligi, yozish yo'nalishi bo'yicha.
import json, math, os

def line(x1, y1, x2, y2, n=None):
    d = math.hypot(x2 - x1, y2 - y1)
    n = n or max(2, int(d / 0.05) + 1)
    return [(x1 + (x2 - x1) * i / (n - 1), y1 + (y2 - y1) * i / (n - 1)) for i in range(n)]

def arc(cx, cy, rx, ry, a0, a1):
    n = max(6, int(abs(a1 - a0) / 12) + 1)
    return [(cx + rx * math.cos(math.radians(a0 + (a1 - a0) * i / (n - 1))),
             cy + ry * math.sin(math.radians(a0 + (a1 - a0) * i / (n - 1)))) for i in range(n)]

def path(*parts):
    pts = []
    for p in parts:
        if pts and abs(pts[-1][0] - p[0][0]) < 1e-6 and abs(pts[-1][1] - p[0][1]) < 1e-6:
            pts.extend(p[1:])
        else:
            pts.extend(p)
    return pts

G = {}
# ---------------------------------------------------------------- bosh harflar
G["A"] = [line(.18,.9,.5,.1), line(.5,.1,.82,.9), line(.3,.6,.7,.6)]
G["B"] = [line(.28,.1,.28,.9), path(line(.28,.1,.55,.1), arc(.55,.3,.2,.2,-90,90), line(.55,.5,.28,.5)),
          path(line(.28,.5,.58,.5), arc(.58,.7,.22,.2,-90,90), line(.58,.9,.28,.9))]
# "C" alohida harf emas, lekin "Ch" uchun kerak.
G["C"] = [arc(.56,.5,.34,.4,-40,-320)]
G["D"] = [line(.26,.1,.26,.9), path(line(.26,.1,.45,.1), arc(.45,.5,.32,.4,-90,90), line(.45,.9,.26,.9))]
G["E"] = [line(.3,.1,.3,.9), line(.3,.1,.74,.1), line(.3,.5,.66,.5), line(.3,.9,.74,.9)]
G["F"] = [line(.3,.1,.3,.9), line(.3,.1,.74,.1), line(.3,.5,.66,.5)]
G["G"] = [path(arc(.52,.5,.34,.4,-35,-320)), path(line(.86,.52,.56,.52), line(.56,.52,.86,.52), line(.86,.52,.86,.84))]
G["G"][1] = path(line(.56,.55,.86,.55), line(.86,.55,.86,.84))
G["H"] = [line(.24,.1,.24,.9), line(.76,.1,.76,.9), line(.24,.5,.76,.5)]
G["I"] = [line(.5,.1,.5,.9)]
G["J"] = [path(line(.66,.1,.66,.68), arc(.46,.68,.2,.22,0,180))]
G["K"] = [line(.28,.1,.28,.9), line(.74,.1,.28,.56), line(.42,.44,.78,.9)]
G["L"] = [path(line(.3,.1,.3,.9), line(.3,.9,.74,.9))]
G["M"] = [path(line(.16,.9,.16,.1), line(.16,.1,.5,.62), line(.5,.62,.84,.1), line(.84,.1,.84,.9))]
G["N"] = [path(line(.22,.9,.22,.1), line(.22,.1,.78,.9), line(.78,.9,.78,.1))]
G["O"] = [arc(.5,.5,.34,.4,-90,-450)]
G["P"] = [line(.28,.1,.28,.9), path(line(.28,.1,.55,.1), arc(.55,.31,.22,.21,-90,90), line(.55,.52,.28,.52))]
G["Q"] = [arc(.5,.5,.34,.4,-90,-450), line(.6,.7,.86,.95)]
G["R"] = [line(.28,.1,.28,.9), path(line(.28,.1,.55,.1), arc(.55,.31,.22,.21,-90,90), line(.55,.52,.28,.52)), line(.48,.52,.78,.9)]
G["S"] = [path(arc(.5,.3,.27,.2,-15,-270), arc(.5,.7,.29,.2,-90,160))]
G["T"] = [line(.18,.1,.82,.1), line(.5,.1,.5,.9)]
G["U"] = [path(line(.22,.1,.22,.6), arc(.5,.6,.28,.3,180,0), line(.78,.6,.78,.1))]
G["V"] = [path(line(.16,.1,.5,.9), line(.5,.9,.84,.1))]
G["X"] = [line(.2,.1,.8,.9), line(.8,.1,.2,.9)]
G["Y"] = [line(.2,.1,.5,.5), line(.8,.1,.5,.5), line(.5,.5,.5,.9)]
G["Z"] = [path(line(.2,.1,.8,.1), line(.8,.1,.2,.9), line(.2,.9,.8,.9))]
# ---------------------------------------------------------------- raqamlar
G["0"] = [arc(.5,.5,.3,.4,-90,-450)]
G["1"] = [path(line(.34,.26,.56,.1), line(.56,.1,.56,.9))]
G["2"] = [path(arc(.5,.32,.26,.22,-170,20), line(.74,.38,.22,.9), line(.22,.9,.8,.9))]
G["3"] = [path(arc(.5,.3,.25,.2,-160,90), arc(.5,.7,.28,.2,-90,160))]
G["4"] = [path(line(.62,.1,.18,.66), line(.18,.66,.84,.66)), line(.64,.36,.64,.9)]
G["5"] = [path(line(.74,.1,.32,.1), line(.32,.1,.3,.46), arc(.5,.66,.27,.24,-130,150))]
G["6"] = [path(arc(.52,.52,.3,.4,-60,-270), arc(.5,.7,.24,.2,90,-270))]
G["7"] = [path(line(.2,.1,.8,.1), line(.8,.1,.42,.9))]
G["8"] = [arc(.5,.3,.21,.2,90,-270), arc(.5,.7,.25,.2,-90,270)]
G["9"] = [arc(.5,.34,.25,.24,0,-360), line(.75,.34,.7,.9)]
# ---------------------------------------------------------------- yozuvdan oldingi chiziqlar (4 yosh)
def zigzag(n=4):
    pts = []
    for i in range(n * 2 + 1):
        pts.append((.1 + .8 * i / (n * 2), .35 if i % 2 == 0 else .65))
    return path(*[line(pts[i][0], pts[i][1], pts[i+1][0], pts[i+1][1]) for i in range(len(pts) - 1)])

def wave(n=2):
    return [(.08 + .84 * i / 60, .5 + .18 * math.sin(i / 60 * n * 2 * math.pi)) for i in range(61)]

def spiral(turns=2):
    # Halqalar orasi ~0.18 — barmoq bilan aniq yurish mumkin bo'lsin.
    return [(.5 + (.05 + .36 * t / 100) * math.cos(t / 100 * turns * 2 * math.pi),
             .5 + (.05 + .36 * t / 100) * math.sin(t / 100 * turns * 2 * math.pi)) for t in range(101)]

def loops(n=3):
    pts = []
    for i in range(121):
        t = i / 120 * n * 2 * math.pi
        pts.append((.12 + .76 * i / 120 + .07 * math.cos(t + math.pi), .5 - .2 * math.sin(t)))
    return pts

P = {
 "vertical": [line(.3,.15,.3,.85), line(.5,.15,.5,.85), line(.7,.15,.7,.85)],
 "horizontal": [line(.15,.3,.85,.3), line(.15,.5,.85,.5), line(.15,.7,.85,.7)],
 "diagonal": [line(.2,.2,.8,.8), line(.2,.8,.8,.2)],
 "curve": [arc(.5,.75,.35,.45,180,360)],
 "zigzag": [zigzag()],
 "wave": [wave()],
 "circle": [arc(.5,.5,.35,.35,-90,-450)],
 "spiral": [spiral()],
 "loops": [loops()],
 "square": [path(line(.2,.2,.8,.2), line(.8,.2,.8,.8), line(.8,.8,.2,.8), line(.2,.8,.2,.2))],
 "triangle": [path(line(.5,.15,.85,.82), line(.85,.82,.15,.82), line(.15,.82,.5,.15))],
 "rainbow": [arc(.5,.8,.4,.5,180,360), arc(.5,.8,.25,.33,180,360)],
 "steps": [path(line(.1,.8,.3,.8), line(.3,.8,.3,.6), line(.3,.6,.5,.6), line(.5,.6,.5,.4), line(.5,.4,.7,.4), line(.7,.4,.7,.2), line(.7,.2,.9,.2))],
 "waves2": [wave(3)],
 "zigzag2": [zigzag(6)],
}
# Nuqtalarni birlashtirish uchun shakllar (raqamlangan nuqtalar).
DOTS = {
 "star": [(.5,.08),(.62,.38),(.94,.38),(.68,.58),(.78,.9),(.5,.7),(.22,.9),(.32,.58),(.06,.38),(.38,.38),(.5,.08)],
 "house": [(.2,.9),(.2,.45),(.5,.12),(.8,.45),(.8,.9),(.2,.9)],
 "fish": [(.1,.5),(.3,.3),(.6,.3),(.8,.5),(.95,.3),(.95,.7),(.8,.5),(.6,.7),(.3,.7),(.1,.5)],
 "boat": [(.1,.6),(.9,.6),(.75,.85),(.25,.85),(.1,.6)],
 "heart": [(.5,.88),(.12,.48),(.18,.2),(.38,.14),(.5,.3),(.62,.14),(.82,.2),(.88,.48),(.5,.88)],
 "kite": [(.5,.08),(.82,.4),(.5,.92),(.18,.4),(.5,.08)],
 "diamond": [(.5,.1),(.9,.5),(.5,.9),(.1,.5),(.5,.1)],
 "tent": [(.1,.85),(.5,.15),(.9,.85),(.1,.85)],
 "arrow": [(.1,.5),(.7,.5),(.7,.3),(.95,.55),(.7,.8),(.7,.6),(.1,.6)],
 "crown": [(.1,.85),(.1,.3),(.3,.55),(.5,.2),(.7,.55),(.9,.3),(.9,.85),(.1,.85)],
}

def rnd(strokes):
    return [[[round(x, 3), round(y, 3)] for x, y in s] for s in strokes]

out = {
 "schemaVersion": 1,
 "note": "Yozish mashqlari uchun chiziq yo‘nalishlari (original). 0..1 koordinatalar, y pastga.",
 "glyphs": {k: rnd(v) for k, v in G.items()},
 "prewriting": {k: rnd(v) for k, v in P.items()},
 "dots": {k: [[round(x, 3), round(y, 3)] for x, y in v] for k, v in DOTS.items()},
}
# O'zbek alifbosidagi har bir harf (Sh, Ch, Ng — ikki belgidan) yozilishi mumkin bo'lsin.
for ch in "ABCDEFGHIJKLMNOPQRSTUVXYZ0123456789":
    assert ch in G, ch
for group in ("glyphs", "prewriting"):
    for k, strokes in out[group].items():
        for s in strokes:
            for x, y in s:
                assert -0.02 <= x <= 1.02 and -0.02 <= y <= 1.02, (k, x, y)
json.dump(out, open(os.path.join(os.path.dirname(__file__), "..", "..", "assets", "data", "glyphs.json"), "w"), indent=0)
print(len(G), "glyphs,", len(P), "prewriting,", len(DOTS), "dot shapes")
