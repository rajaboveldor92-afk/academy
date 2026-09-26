import 'package:academy/learning/engine/mastery.dart';
import 'package:academy/learning/models/exercise.dart';
import 'package:academy/learning/content/instructions.dart';
import 'package:academy/learning/content/uz_numbers.dart';
import 'package:academy/models/child_progress.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  final now = DateTime(2026, 9, 27, 10);

  group('Adaptiv qoida (25-band)', () {
    test('≥85% — keyingi daraja', () {
      final r = AdaptiveRule.apply(const SkillStat(), correctFirstTry: 9, total: 10, maxLevel: 3, now: now);
      expect(r.decision, LevelDecision.up);
      expect(r.stat.level, 2);
      expect(r.stat.lessons, 1);
      expect(r.stat.lastPracticed, now);
    });

    test('60–84% — shu daraja', () {
      final r = AdaptiveRule.apply(const SkillStat(level: 2, ema: 70, lessons: 3), correctFirstTry: 7, total: 10, maxLevel: 3, now: now);
      expect(r.decision, LevelDecision.stay);
      expect(r.stat.level, 2);
    });

    test('<60% — osonroq daraja, lekin 1 dan past emas', () {
      final down = AdaptiveRule.apply(const SkillStat(level: 3, ema: 50, lessons: 2), correctFirstTry: 2, total: 10, maxLevel: 3, now: now);
      expect(down.decision, LevelDecision.down);
      expect(down.stat.level, 2);
      final floor = AdaptiveRule.apply(const SkillStat(), correctFirstTry: 1, total: 6, maxLevel: 3, now: now);
      expect(floor.stat.level, 1);
    });

    test('eng yuqori darajadan oshmaydi, mastery 0..100', () {
      var s = const SkillStat();
      for (var i = 0; i < 10; i++) {
        s = AdaptiveRule.apply(s, correctFirstTry: 10, total: 10, maxLevel: 3, now: now).stat;
      }
      expect(s.level, 3);
      expect(s.mastery(3), inInclusiveRange(95, 100));
      expect(const SkillStat().mastery(3), 0);
    });

    test('progress bilan birga saqlanadi', () {
      final r = AdaptiveRule.apply(const SkillStat(), correctFirstTry: 5, total: 6, maxLevel: 3, now: now);
      final p = ChildProgress.empty('a').withSkill('math4.count_1_3', r.stat).addRecent('math4.count_1_3', [1, 2, 3]);
      final restored = ChildProgress.fromMap(p.toMap());
      expect(restored.skillOf('math4.count_1_3').level, r.stat.level);
      expect(restored.recentOf('math4.count_1_3'), [1, 2, 3]);
      final many = p.addRecent('t', List<int>.generate(100, (i) => i));
      expect(many.recentOf('t').length, ChildProgress.recentLimit);
    });
  });

  group('O‘zbekcha sonlar va ovoz', () {
    test('son so‘z bilan', () {
      expect(UzNumbers.word(0), 'nol');
      expect(UzNumbers.word(7), 'yetti');
      expect(UzNumbers.word(10), 'o‘n');
      expect(UzNumbers.word(37), 'o‘ttiz yetti');
      expect(UzNumbers.word(100), 'yuz');
      expect(UzNumbers.ordinal(3), 'uchinchi');
      expect(UzNumbers.ordinal(2), 'ikkinchi');
    });

    test('ovoz uchun matn: raqam va belgilar so‘zga aylanadi', () {
      expect(InstructionBank.toSpeech('7 + 3 = ?'), 'yetti qo‘shuv uch teng ?');
      expect(InstructionBank.uzSuffix('suyak', 'ga'), 'suyakka');
      expect(InstructionBank.uzSuffix('baliq', 'ga'), 'baliqqa');
      expect(InstructionBank.uzSuffix('gul', 'ga'), 'gulga');
    });

    test('ko‘rsatma shabloni parametrlar bilan', () {
      final bank = InstructionBank({
        'x': {'uz': '{n} dan keyin {item:ga} qara', 'en': 'After {n} look at {item}', 'ru': 'После {n} смотри: {item}'},
      });
      final r = bank.render('x', {'n': 7, 'item': const Localized(uz: 'suyak', en: 'bone', ru: 'кость')});
      expect(r.text.uz, '7 dan keyin suyakka qara');
      expect(r.text.en, 'After 7 look at bone');
      expect(r.speech, 'Yetti dan keyin suyakka qara');
    });
  });
}
