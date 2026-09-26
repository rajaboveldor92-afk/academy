import '../core/utils/map_utils.dart';

/// Savol turlari. JSON'dagi `questionType` qiymatlari.
enum QuestionType {
  /// Bir nechta variantdan bittasini tanlash.
  choice,

  /// Rasm/emoji variantlaridan tanlash.
  imageChoice,

  /// Ovozni eshitib, mos rasmni tanlash.
  listenChoice,

  /// Rost / yolg'on.
  trueFalse;

  static QuestionType fromName(String? name) {
    for (final t in QuestionType.values) {
      if (t.name == name) return t;
    }
    return QuestionType.choice;
  }
}

/// JSON kontent faylidagi bitta topshiriq (spetsifikatsiyaning 28-bandi).
///
/// Misol:
/// ```json
/// {
///   "id": "math4_count_001",
///   "subject": "math",
///   "topic": "counting",
///   "ageMin": 3, "ageMax": 5,
///   "difficulty": 1,
///   "questionType": "choice",
///   "question": "Nechta olma bor?",
///   "image": "🍎🍎🍎",
///   "options": ["2", "3", "4"],
///   "correctAnswer": "3",
///   "audio": "uz/q_how_many_apples",
///   "explanation": "Sanaymiz: bir, ikki, uch.",
///   "rewardStars": 1
/// }
/// ```
class Question {
  const Question({
    required this.id,
    required this.subject,
    required this.topic,
    required this.ageMin,
    required this.ageMax,
    required this.difficulty,
    required this.questionType,
    required this.question,
    required this.options,
    required this.correctAnswer,
    this.image,
    this.audio,
    this.explanation,
    this.rewardStars = 1,
  });

  final String id;
  final String subject;
  final String topic;
  final int ageMin;
  final int ageMax;

  /// 1 (eng oson) … 5.
  final int difficulty;
  final QuestionType questionType;
  final String question;
  final List<String> options;
  final String correctAnswer;

  /// Emoji matni yoki `assets/images/...` yo'li.
  final String? image;

  /// `assets/audio/` ichidagi kalit (kengaytmasiz), masalan `uz/olma`.
  final String? audio;
  final String? explanation;
  final int rewardStars;

  bool isCorrect(String answer) => answer.trim() == correctAnswer.trim();

  bool fitsAge(int age) => age >= ageMin && age <= ageMax;

  /// Kontent to'g'riligini tekshiradi: to'g'ri javob variantlar ichida bo'lishi shart.
  bool get isValid =>
      id.isNotEmpty && options.length >= 2 && options.contains(correctAnswer);

  Map<String, dynamic> toMap() => {
        'id': id,
        'subject': subject,
        'topic': topic,
        'ageMin': ageMin,
        'ageMax': ageMax,
        'difficulty': difficulty,
        'questionType': questionType.name,
        'question': question,
        'options': options,
        'correctAnswer': correctAnswer,
        if (image != null) 'image': image,
        if (audio != null) 'audio': audio,
        if (explanation != null) 'explanation': explanation,
        'rewardStars': rewardStars,
      };

  factory Question.fromMap(Map<String, dynamic> map) => Question(
        id: (map['id'] ?? '').toString(),
        subject: (map['subject'] ?? '').toString(),
        topic: (map['topic'] ?? '').toString(),
        ageMin: MapUtils.asInt(map['ageMin'], 3),
        ageMax: MapUtils.asInt(map['ageMax'], 8),
        difficulty: MapUtils.asInt(map['difficulty'], 1),
        questionType: QuestionType.fromName(map['questionType']?.toString()),
        question: (map['question'] ?? '').toString(),
        options: MapUtils.asStringList(map['options']),
        correctAnswer: (map['correctAnswer'] ?? '').toString(),
        image: map['image']?.toString(),
        audio: map['audio']?.toString(),
        explanation: map['explanation']?.toString(),
        rewardStars: MapUtils.asInt(map['rewardStars'], 1),
      );
}
