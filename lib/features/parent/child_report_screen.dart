import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../core/providers.dart';
import '../../core/utils/date_keys.dart';
import '../../learning/content/content_provider.dart';
import '../../learning/engine/rewards.dart';
import '../../models/child_profile.dart';
import '../../models/subject.dart';
import '../../theme/app_colors.dart';
import '../../widgets/profile_photo.dart';
import '../profiles/profiles_controller.dart';
import '../session/progress_controller.dart';
import 'child_report.dart';
import 'week_bars.dart';

/// Ota-ona uchun batafsil hisobot: vaqt, aniqlik, fanlar va mavzular bo'yicha egallash (%),
/// takrorlash navbati, kuchli tomonlar va e'tibor kerak bo'lgan mavzular, tavsiyalar.
///
/// Foizlar faqat shu yerda (ota-ona panelida) ko'rsatiladi — bola ekranida faqat yulduzlar.
class ChildReportScreen extends ConsumerWidget {
  const ChildReportScreen({super.key, required this.childId});

  final String childId;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    ChildProfile? profile;
    for (final p in ref.watch(profilesProvider)) {
      if (p.id == childId) profile = p;
    }
    final current = profile;
    if (current == null) {
      return Scaffold(appBar: AppBar(), body: const Center(child: Text('Profil topilmadi')));
    }
    final progress = ref.watch(childProgressProvider(childId));
    final content = ref.watch(contentProvider);
    final now = ref.read(clockProvider)();

    return Scaffold(
      appBar: AppBar(title: Text('Hisobot: ${current.name}')),
      body: SafeArea(
        child: content.when(
          loading: () => const Center(child: CircularProgressIndicator()),
          error: (e, _) => const Center(child: Text('Dastur ma’lumotlarini o‘qib bo‘lmadi.')),
          data: (repo) {
            final report = ChildReport.build(profile: current, progress: progress, content: repo, now: now);
            return ListView(
              key: const Key('report_list'),
              padding: const EdgeInsets.all(16),
              children: [
                _Header(report: report, now: now),
                const SizedBox(height: 12),
                _TipsCard(report: report),
                const SizedBox(height: 12),
                _ReviewsCard(report: report),
                const SizedBox(height: 12),
                _HighlightsCard(report: report),
                const SizedBox(height: 16),
                Text('Fanlar bo‘yicha', style: Theme.of(context).textTheme.titleLarge),
                const SizedBox(height: 4),
                const Text(
                  'Foiz — yoshga mos dasturdagi barcha mavzular bo‘yicha o‘rtacha egallash. '
                  'Mavzu 85% dan oshsa — egallangan hisoblanadi.',
                  style: TextStyle(color: AppColors.textSoft),
                ),
                const SizedBox(height: 8),
                for (final s in report.subjects) _SubjectTile(report: s),
                const SizedBox(height: 16),
                const Text(
                  'Barcha hisob-kitoblar faqat shu qurilmada bajariladi. Ma’lumotlar hech qayerga yuborilmaydi.',
                  style: TextStyle(color: AppColors.textSoft),
                ),
              ],
            );
          },
        ),
      ),
    );
  }
}

class _Card extends StatelessWidget {
  const _Card({required this.child, this.title, this.cardKey});

  final String? title;
  final Widget child;
  final Key? cardKey;

  @override
  Widget build(BuildContext context) {
    return Card(
      key: cardKey,
      margin: EdgeInsets.zero,
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            if (title != null) ...[
              Text(title!, style: Theme.of(context).textTheme.titleMedium?.copyWith(fontWeight: FontWeight.w800)),
              const SizedBox(height: 8),
            ],
            child,
          ],
        ),
      ),
    );
  }
}

class _Metric extends StatelessWidget {
  const _Metric(this.icon, this.value, this.label);

  final String icon;
  final String value;
  final String label;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 104,
      padding: const EdgeInsets.symmetric(vertical: 10, horizontal: 8),
      decoration: BoxDecoration(color: const Color(0xFFF5F6FA), borderRadius: BorderRadius.circular(14)),
      child: Column(
        children: [
          Text(icon, style: const TextStyle(fontSize: 20)),
          Text(value, style: const TextStyle(fontSize: 18, fontWeight: FontWeight.w900)),
          Text(label, textAlign: TextAlign.center, style: const TextStyle(fontSize: 12, color: AppColors.textSoft)),
        ],
      ),
    );
  }
}

class _Header extends StatelessWidget {
  const _Header({required this.report, required this.now});

  final ChildReport report;
  final DateTime now;

  @override
  Widget build(BuildContext context) {
    final p = report.profile;
    final g = report.progress;
    final color = AppColors.profileColor(p.colorIndex);
    final limit = p.dailyLimitMinutes == 0 ? '' : ' / ${p.dailyLimitMinutes}';
    final medals = Rewards.medals.where((m) => g.medals.contains(m.id)).length;
    return _Card(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              ProfilePhoto(profile: p, size: 56, showBadge: false),
              const SizedBox(width: 12),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(p.displayFullName, style: Theme.of(context).textTheme.titleLarge),
                    Text('${p.age} yosh', style: const TextStyle(color: AppColors.textSoft)),
                  ],
                ),
              ),
            ],
          ),
          const SizedBox(height: 12),
          Wrap(
            spacing: 8,
            runSpacing: 8,
            children: [
              _Metric('⏱️', '${report.todayMinutes}$limit', 'bugun, daq'),
              _Metric('📅', '${report.weekMinutes}', 'hafta, daq'),
              _Metric('🗓️', '${report.weekDaysActive}/7', 'faol kunlar'),
              _Metric('🔥', '${g.streak}', 'ketma-ket kun'),
              _Metric('📚', '${g.completedLessons}', 'dars'),
              _Metric('▶️', '${g.dailyLessons}', 'bugungi dars'),
              _Metric('🎯', report.accuracy == null ? '—' : '${report.accuracy}%', '1-urinishda to‘g‘ri'),
              _Metric('⭐', '${g.stars}', 'yulduz'),
              _Metric('🏅', '$medals/${Rewards.medals.length}', 'medal'),
            ],
          ),
          const SizedBox(height: 12),
          const Text('Oxirgi 7 kun (daqiqa)', style: TextStyle(fontWeight: FontWeight.w700)),
          const SizedBox(height: 6),
          WeekBars(values: g.weeklyMinutes(now), days: DateKeys.lastDays(now), color: color),
          const SizedBox(height: 8),
          const Text('Oxirgi 7 kun (to‘g‘ri javoblar)', style: TextStyle(fontWeight: FontWeight.w700)),
          const SizedBox(height: 6),
          WeekBars(values: g.weeklyCorrect(now), days: DateKeys.lastDays(now), color: AppColors.success),
        ],
      ),
    );
  }
}

class _TipsCard extends StatelessWidget {
  const _TipsCard({required this.report});

  final ChildReport report;

  @override
  Widget build(BuildContext context) {
    return _Card(
      cardKey: const Key('report_tips'),
      title: 'Tavsiyalar',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          for (final t in report.tips)
            Padding(
              padding: const EdgeInsets.only(bottom: 6),
              child: Text(t, style: const TextStyle(fontSize: 15, height: 1.3)),
            ),
        ],
      ),
    );
  }
}

class _ReviewsCard extends StatelessWidget {
  const _ReviewsCard({required this.report});

  final ChildReport report;

  @override
  Widget build(BuildContext context) {
    return _Card(
      cardKey: const Key('report_reviews'),
      title: '🔁 Takrorlash navbati',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Wrap(
            spacing: 8,
            runSpacing: 8,
            children: [
              _Metric('📌', '${report.reviewsDue}', 'bugun'),
              _Metric('📆', '${report.reviewsWeek}', 'keyingi 7 kun'),
              _Metric('🗂️', '${report.reviewsTotal}', 'jami navbatda'),
            ],
          ),
          const SizedBox(height: 8),
          const Text(
            'Xato qilingan tushuncha ertaga, keyin 3 va 7 kundan so‘ng boshqa ko‘rinishda qayta so‘raladi. '
            '7 kunlik takrorlashda ham to‘g‘ri topsa — navbatdan chiqadi.',
            style: TextStyle(color: AppColors.textSoft),
          ),
        ],
      ),
    );
  }
}

class _HighlightsCard extends StatelessWidget {
  const _HighlightsCard({required this.report});

  final ChildReport report;

  @override
  Widget build(BuildContext context) {
    final strong = report.strengths;
    final help = report.needsHelp;
    return _Card(
      title: 'Kuchli tomonlar va e’tibor kerak',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text('💪 Egallangan', style: TextStyle(fontWeight: FontWeight.w800)),
          if (strong.isEmpty)
            const Text('Hali egallangan mavzu yo‘q — darslar davom etmoqda.', style: TextStyle(color: AppColors.textSoft))
          else
            for (final t in strong) _TopicLine(topic: t, showSubject: true),
          const SizedBox(height: 10),
          const Text('🤝 E’tibor kerak (oxirgi natija 60% dan past)', style: TextStyle(fontWeight: FontWeight.w800)),
          if (help.isEmpty)
            const Text('Qiynalayotgan mavzu yo‘q.', style: TextStyle(color: AppColors.textSoft))
          else
            for (final t in help) _TopicLine(topic: t, showSubject: true),
        ],
      ),
    );
  }
}

class _SubjectTile extends StatelessWidget {
  const _SubjectTile({required this.report});

  final SubjectReport report;

  @override
  Widget build(BuildContext context) {
    final s = report.subject;
    final acc = report.accuracy;
    return Card(
      key: ValueKey('report_subject_${s.id}'),
      margin: const EdgeInsets.only(bottom: 8),
      child: ExpansionTile(
        shape: const Border(),
        leading: Text(s.emoji, style: const TextStyle(fontSize: 28)),
        title: Row(
          children: [
            Expanded(child: Text(s.title, style: const TextStyle(fontWeight: FontWeight.w800))),
            Text(Rewards.cupEmoji(report.cup), style: const TextStyle(fontSize: 18)),
          ],
        ),
        subtitle: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const SizedBox(height: 4),
            ClipRRect(
              borderRadius: BorderRadius.circular(6),
              child: LinearProgressIndicator(
                value: report.mastery / 100,
                minHeight: 10,
                color: s.color,
                backgroundColor: s.color.withAlpha(40),
              ),
            ),
            const SizedBox(height: 4),
            Text(
              '${report.mastery}% · mavzular: ${report.mastered}/${report.topics.length} egallangan, '
              '${report.started} boshlangan${acc == null ? '' : ' · aniqlik $acc%'}',
              key: ValueKey('report_subject_line_${s.id}'),
              style: const TextStyle(fontSize: 13),
            ),
            if (report.current != null)
              Text('Hozir: ${report.current!.topic.title.uz}',
                  style: const TextStyle(fontSize: 13, color: AppColors.textSoft)),
          ],
        ),
        childrenPadding: const EdgeInsets.fromLTRB(12, 0, 12, 12),
        children: [for (final t in report.topics) _TopicLine(topic: t)],
      ),
    );
  }
}

class _TopicLine extends StatelessWidget {
  const _TopicLine({required this.topic, this.showSubject = false});

  final TopicReport topic;
  final bool showSubject;

  static String _status(TopicStatus s) => switch (s) {
        TopicStatus.notStarted => 'boshlanmagan',
        TopicStatus.learning => 'o‘rganmoqda',
        TopicStatus.needsHelp => 'qiynalmoqda',
        TopicStatus.mastered => 'egallangan',
      };

  static Color _color(TopicStatus s) => switch (s) {
        TopicStatus.notStarted => const Color(0xFFBDBDC7),
        TopicStatus.learning => AppColors.primary,
        TopicStatus.needsHelp => AppColors.gentle,
        TopicStatus.mastered => AppColors.success,
      };

  @override
  Widget build(BuildContext context) {
    final t = topic.topic;
    final st = topic.stat;
    final status = topic.status;
    final last = st.lastPracticed;
    final details = [
      if (st.started) 'daraja ${st.level}/${t.maxLevel}',
      if (st.started) '${st.lessons} dars',
      if (last != null) '${last.day.toString().padLeft(2, '0')}.${last.month.toString().padLeft(2, '0')}',
    ].join(' · ');
    final subject = showSubject ? '${Subject.fromId(t.subject)?.title ?? t.subject} · ' : '';
    return Padding(
      key: ValueKey('report_topic_${t.id}'),
      padding: const EdgeInsets.symmetric(vertical: 4),
      child: Row(
        children: [
          SizedBox(width: 34, child: Text(t.code, style: const TextStyle(fontSize: 12, fontWeight: FontWeight.w700, color: AppColors.textSoft))),
          Text(t.emoji, style: const TextStyle(fontSize: 18)),
          const SizedBox(width: 6),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(t.title.uz, style: const TextStyle(fontWeight: FontWeight.w700)),
                Text(
                  '$subject${_status(status)}${details.isEmpty ? '' : ' · $details'}',
                  style: TextStyle(fontSize: 12, color: _color(status)),
                ),
              ],
            ),
          ),
          SizedBox(
            width: 44,
            child: Text(
              st.started ? '${topic.mastery}%' : '—',
              textAlign: TextAlign.right,
              style: const TextStyle(fontWeight: FontWeight.w800),
            ),
          ),
        ],
      ),
    );
  }
}
