import 'package:academy/learning/engine/spaced_repetition.dart';
import 'package:academy/models/child_progress.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  final day1 = DateTime(2026, 9, 26, 10);

  group('Streak (ketma-ket kunlar)', () {
    test('birinchi tashrif — 1', () {
      final p = ChildProgress.empty('a').registerVisit(day1);
      expect(p.streak, 1);
      expect(p.lastPlayed, day1);
    });

    test('shu kuni qayta kirish streakni oshirmaydi', () {
      final p = ChildProgress.empty('a')
          .registerVisit(day1)
          .registerVisit(day1.add(const Duration(hours: 5)));
      expect(p.streak, 1);
    });

    test('ertasi kuni — +1, oraliq kun o\'tsa — 1 dan', () {
      var p = ChildProgress.empty('a').registerVisit(day1);
      p = p.registerVisit(DateTime(2026, 9, 27, 8));
      expect(p.streak, 2);
      p = p.registerVisit(DateTime(2026, 9, 28, 23, 59));
      expect(p.streak, 3);
      p = p.registerVisit(DateTime(2026, 9, 30, 9));
      expect(p.streak, 1);
    });
  });

  group('Vaqt hisobi', () {
    test('soniyalar kunlar bo\'yicha yig\'iladi', () {
      var p = ChildProgress.empty('a');
      p = p.addSeconds(day1, 90).addSeconds(day1, 45);
      p = p.addSeconds(DateTime(2026, 9, 27, 9), 600);
      expect(p.secondsOn(day1), 135);
      expect(p.minutesOn(day1), 2);
      expect(p.minutesOn(DateTime(2026, 9, 27)), 10);
    });

    test('haftalik progress 7 ta qiymat, oxirgisi bugun', () {
      final p = ChildProgress.empty('a')
          .addSeconds(DateTime(2026, 9, 20, 9), 300)
          .addSeconds(day1, 1200);
      final week = p.weeklyMinutes(day1);
      expect(week.length, 7);
      expect(week.last, 20);
      expect(week.first, 5);
    });
  });

  group('Javoblar va yulduzlar', () {
    test('to\'g\'ri javob yulduz beradi, noto\'g\'risi bermaydi', () {
      var p = ChildProgress.empty('a');
      p = p.recordAnswer(subjectId: 'math', isCorrect: true, now: day1, rewardStars: 2);
      p = p.recordAnswer(subjectId: 'math', isCorrect: false, now: day1, rewardStars: 2);
      expect(p.stars, 2);
      expect(p.correctAnswers, 1);
      expect(p.wrongAnswers, 1);
      expect(p.scoreOf('math').correct, 1);
      expect(p.scoreOf('math').total, 2);
      expect(p.scoreOf('math').ratio, 0.5);
      expect(p.weeklyCorrect(day1).last, 1);
    });

    test('daraja va medal', () {
      var p = ChildProgress.empty('a');
      expect(p.levelOf('math'), 1);
      p = p.setLevel('math', 3).addMedal('first_star').addMedal('first_star');
      expect(p.levelOf('math'), 3);
      expect(p.medals, ['first_star']);
      expect(p.setLevel('math', 0).levelOf('math'), 1);
    });

    test('toMap/fromMap aylanishi', () {
      final p = ChildProgress.empty('a')
          .registerVisit(day1)
          .addSeconds(day1, 100)
          .recordAnswer(subjectId: 'logic', isCorrect: true, now: day1, rewardStars: 1)
          .setLevel('logic', 2)
          .addMedal('m1')
          .completeLesson();
      final r = ChildProgress.fromMap(p.toMap());
      expect(r.childId, 'a');
      expect(r.stars, 1);
      expect(r.streak, 1);
      expect(r.secondsOn(day1), 100);
      expect(r.levelOf('logic'), 2);
      expect(r.scoreOf('logic').total, 1);
      expect(r.medals, ['m1']);
      expect(r.completedLessons, 1);
      expect(r.lastPlayed, day1);
    });

    test('toMap/fromMap: takrorlash navbati, kunlik dars, sovg‘alar, hisoblagichlar', () {
      final queue = SpacedRepetition.record(const {}, topicId: 'math4.count', concept: 'n:3', firstTry: false, now: day1);
      final p = ChildProgress.empty('a')
          .withReviews(queue)
          .completeDaily(day1)
          .openGift()
          .addCounter('chess_win')
          .addCounter('chess_win')
          .addCounter('puzzle_9');
      final r = ChildProgress.fromMap(p.toMap());
      expect(r.reviews.length, 1);
      final item = r.reviews.values.single;
      expect(item.topicId, 'math4.count');
      expect(item.concept, 'n:3');
      expect(item.stage, 0);
      expect(item.due, DateTime(2026, 9, 27));
      expect(r.dailyLessons, 1);
      expect(r.lastDailyLesson, day1);
      expect(r.dailyDoneOn(DateTime(2026, 9, 26, 22)), isTrue);
      expect(r.dailyDoneOn(DateTime(2026, 9, 27, 7)), isFalse);
      expect(r.giftsOpened, 1);
      expect(r.counter('chess_win'), 2);
      expect(r.counter('puzzle_9'), 1);
      expect(r.counter('yoq'), 0);
    });

    test('eski formatdagi yozuv (yangi maydonlarsiz) xatosiz o‘qiladi', () {
      final r = ChildProgress.fromMap({'childId': 'a', 'stars': 5});
      expect(r.stars, 5);
      expect(r.reviews, isEmpty);
      expect(r.dailyLessons, 0);
      expect(r.lastDailyLesson, isNull);
      expect(r.giftsOpened, 0);
      expect(r.counters, isEmpty);
    });
  });
}
