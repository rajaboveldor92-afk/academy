import '../../core/utils/date_keys.dart';
import '../../l10n/tr.dart';
import '../../learning/content/content_repository.dart';
import '../../learning/engine/mastery.dart';
import '../../learning/engine/rewards.dart';
import '../../learning/engine/spaced_repetition.dart';
import '../../learning/models/topic.dart';
import '../../models/child_profile.dart';
import '../../models/child_progress.dart';
import '../../models/subject.dart';

/// Mavzu holati (ota-ona paneli uchun).
enum TopicStatus { notStarted, learning, needsHelp, mastered }

/// Bitta mavzu bo'yicha hisobot qatori.
class TopicReport {
  const TopicReport({required this.topic, required this.stat});

  final Topic topic;
  final SkillStat stat;

  int get mastery => stat.mastery(topic.maxLevel);

  TopicStatus get status {
    if (!stat.started) return TopicStatus.notStarted;
    if (mastery >= ChildReport.masteredAt) return TopicStatus.mastered;
    if (stat.lastAccuracy < AdaptiveRule.stayThreshold) return TopicStatus.needsHelp;
    return TopicStatus.learning;
  }
}

/// Bitta fan bo'yicha hisobot: dastur bo'yicha umumiy egallash, aniqlik, mavzular.
class SubjectReport {
  const SubjectReport({
    required this.subject,
    required this.topics,
    required this.correct,
    required this.total,
    required this.cup,
  });

  final Subject subject;
  final List<TopicReport> topics;

  /// Birinchi urinishdagi to'g'ri javoblar / jami javoblar.
  final int correct;
  final int total;
  final CupTier cup;

  /// Yoshga mos dastur bo'yicha umumiy egallash (barcha mavzular, boshlanmaganlari 0%).
  int get mastery {
    if (topics.isEmpty) return 0;
    final sum = topics.fold<int>(0, (s, t) => s + t.mastery);
    return (sum / topics.length).round();
  }

  /// Aniqlik foizi (javob bo'lmasa `null`).
  int? get accuracy => total == 0 ? null : (correct * 100 / total).round();

  int get started => topics.where((t) => t.stat.started).length;
  int get mastered => topics.where((t) => t.status == TopicStatus.mastered).length;
  bool get untouched => started == 0 && total == 0;

  /// Bola hozir o'rganayotgan mavzu (boshlangan, lekin egallanmagan) yoki birinchi boshlanmagani.
  TopicReport? get current {
    for (final t in topics) {
      if (t.stat.started && t.status != TopicStatus.mastered) return t;
    }
    for (final t in topics) {
      if (!t.stat.started) return t;
    }
    return null;
  }
}

/// Ota-ona uchun to'liq hisobot (faqat qurilmadagi ma'lumotlardan hisoblanadi).
class ChildReport {
  const ChildReport({
    required this.profile,
    required this.progress,
    required this.subjects,
    required this.reviewsDue,
    required this.reviewsWeek,
    required this.reviewsTotal,
    required this.todayMinutes,
    required this.weekMinutes,
    required this.weekDaysActive,
    required this.tips,
  });

  static const int masteredAt = 85;

  final ChildProfile profile;
  final ChildProgress progress;
  final List<SubjectReport> subjects;

  /// Bugun takrorlanishi kerak bo'lgan tushunchalar.
  final int reviewsDue;

  /// Keyingi 7 kun ichida takrorlanadiganlar (bugungilardan tashqari).
  final int reviewsWeek;
  final int reviewsTotal;
  final int todayMinutes;
  final int weekMinutes;

  /// Oxirgi 7 kundan nechtasida o'ynagan.
  final int weekDaysActive;

  /// Ota-onaga qisqa tavsiyalar.
  final List<String> tips;

  /// Umumiy aniqlik (birinchi urinishda), javob bo'lmasa `null`.
  int? get accuracy {
    final total = progress.correctAnswers + progress.wrongAnswers;
    return total == 0 ? null : (progress.correctAnswers * 100 / total).round();
  }

  /// Egallangan mavzular (eng yuqori foizdan) — kuchli tomonlar.
  List<TopicReport> get strengths {
    final all = [for (final s in subjects) ...s.topics.where((t) => t.status == TopicStatus.mastered)];
    all.sort((a, b) => b.mastery.compareTo(a.mastery));
    return all.take(5).toList();
  }

  /// Qiynalayotgan mavzular (oxirgi natija < 60%).
  List<TopicReport> get needsHelp {
    final all = [for (final s in subjects) ...s.topics.where((t) => t.status == TopicStatus.needsHelp)];
    all.sort((a, b) => a.stat.lastAccuracy.compareTo(b.stat.lastAccuracy));
    return all.take(5).toList();
  }

  static ChildReport build({
    required ChildProfile profile,
    required ChildProgress progress,
    required ContentRepository content,
    required DateTime now,
    String lang = 'uz',
  }) {
    final suffix = profile.age <= 5 ? '4' : '6';
    final subjects = <SubjectReport>[];
    for (final s in Subject.values) {
      if (!profile.isSubjectEnabled(s.id)) continue;
      final c = content.curriculum(s.id, suffix);
      if (c == null || c.topics.isEmpty) continue;
      final score = progress.scoreOf(s.id);
      subjects.add(SubjectReport(
        subject: s,
        topics: [for (final t in c.topics) TopicReport(topic: t, stat: progress.skillOf(t.id))],
        correct: score.correct,
        total: score.total,
        cup: Rewards.cup(progress, content, s.id, profile.age),
      ));
    }

    final due = SpacedRepetition.due(progress.reviews, now).length;
    final week = progress.reviews.values.where((r) {
      final d = DateKeys.daysBetween(now, r.due);
      return d >= 1 && d <= 7;
    }).length;
    final weekly = progress.weeklyMinutes(now);
    final activeDays = [
      for (final k in DateKeys.lastDays(now))
        if ((progress.dailySeconds[k] ?? 0) > 0 || (progress.dailyCorrect[k] ?? 0) > 0) k,
    ].length;

    final base = ChildReport(
      profile: profile,
      progress: progress,
      subjects: subjects,
      reviewsDue: due,
      reviewsWeek: week,
      reviewsTotal: progress.reviews.length,
      todayMinutes: progress.minutesOn(now),
      weekMinutes: weekly.fold<int>(0, (a, b) => a + b),
      weekDaysActive: activeDays,
      tips: const [],
    );
    return base._withTips(_tips(base, now, Tr(lang)));
  }

  ChildReport _withTips(List<String> value) => ChildReport(
        profile: profile,
        progress: progress,
        subjects: subjects,
        reviewsDue: reviewsDue,
        reviewsWeek: reviewsWeek,
        reviewsTotal: reviewsTotal,
        todayMinutes: todayMinutes,
        weekMinutes: weekMinutes,
        weekDaysActive: weekDaysActive,
        tips: value,
      );

  static List<String> _tips(ChildReport r, DateTime now, Tr tr) {
    final tips = <String>[];
    final name = r.profile.name;
    if (!r.progress.dailyDoneOn(now)) {
      tips.add(tr.tipDaily(name, r.profile.age <= 5));
    }
    if (r.reviewsDue > 0) {
      tips.add(tr.tipReviews(r.reviewsDue));
    }
    final help = r.needsHelp;
    if (help.isNotEmpty) {
      final t = help.first.topic;
      final subject = Subject.fromId(t.subject)?.titleIn(tr.lang) ?? t.subject;
      tips.add(tr.tipHelp(t.title.of(tr.lang), subject));
    }
    final untouched = [
      for (final s in r.subjects)
        if (s.untouched && s.subject.id != 'family') s.subject.titleIn(tr.lang),
    ];
    if (untouched.isNotEmpty && r.progress.completedLessons >= 3) {
      tips.add(tr.tipUntouched('${untouched.take(4).join(', ')}${untouched.length > 4 ? '…' : ''}'));
    }
    final family = r.subjects.where((s) => s.subject.id == 'family').toList();
    if (family.isNotEmpty && family.first.total < 3) {
      tips.add(tr.tipFamily);
    }
    if (r.weekDaysActive <= 2 && r.progress.completedLessons > 0) {
      tips.add(tr.tipWeek(r.weekDaysActive));
    }
    if (tips.isEmpty) {
      tips.add(tr.tipAllGood(name));
    }
    return tips;
  }
}
