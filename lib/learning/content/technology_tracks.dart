import '../../models/child_profile.dart';
import '../models/topic.dart';

/// Common topics always remain available; the parent controls the selected track.
class TechnologyTracks {
  TechnologyTracks._();
  static bool includes(Topic topic, String track) => topic.subject != 'technology' || track == 'both'
    || !topic.tags.any((t) => t.startsWith('track:')) || topic.tags.contains('track:$track');

  static Curriculum forProfile(Curriculum curriculum, ChildProfile profile) {
    if (curriculum.subject != 'technology') return curriculum;
    return Curriculum(subject: curriculum.subject, ageSuffix: curriculum.ageSuffix,
      title: curriculum.title, model: curriculum.model, lessonSize: curriculum.lessonSize,
      topics: curriculum.topics.where((t) => includes(t, profile.effectiveTechnologyTrack)).toList());
  }

  static String title(String track, String lang) => switch ((track, lang)) {
    ('service', 'ru') => 'Сервис и рукоделие', ('service', 'en') => 'Service and crafts',
    ('service', _) => 'Servis va hunarmandchilik',
    ('technical', 'ru') => 'Техническое проектирование', ('technical', 'en') => 'Technical design',
    ('technical', _) => 'Texnik loyihalash',
    (_, 'ru') => 'Оба направления', (_, 'en') => 'Both tracks', _ => 'Ikkala yo‘nalish',
  };
}
