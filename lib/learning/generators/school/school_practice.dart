import '../../models/exercise.dart';
import '../generator_base.dart';
import 'school_base.dart';

/// Grade-specific authored questions and original reading/logic exercises.
class SchoolPractice {
  SchoolPractice._();

  /// Eski formatdagi bank savoli (`question`, `answer`, `wrong`, `explanation`, `lang`).
  static Exercise bankItem(GenContext g, Map<String, dynamic> item) {
    return g.textChoice(
      question: item['question'] as String,
      answer: item['answer'] as String,
      wrong: (item['wrong'] as List).cast<String>(),
      options: g.p('options', 4),
      concept: '${g.topic.id}:${item['id']}',
      lang: item['lang'] as String? ?? 'uz',
      hint: g.topic.theoryIn('uz'),
      explanation: item['explanation'] as String,
      meta: {'bankId': item['id'] as String, 'answerText': item['answer'] as String},
    );
  }

  static const _names = ['Ali', 'Zarina', 'Bobur', 'Madina', 'Sardor', 'Nodira', 'Jasur', 'Malika'];

  static Exercise sequence(GenContext g) {
    final start = g.range(2, g.p('maxStart', 20));
    final step = g.range(2, g.p('maxStep', 5));
    final multiply = g.pb('multiply') && g.chance(0.5);
    final values = <int>[start];
    for (var i = 0; i < 4; i++) {
      values.add(multiply ? values.last * step : values.last + step);
    }
    return g.numberAnswer(
      question: 'Qoidani toping va davom ettiring: ${values.take(4).join(', ')}, …',
      answer: values.last,
      concept: 'rule:$start:$step:$multiply',
      input: g.useInput(),
      hint: 'Qo‘shni sonlarni solishtiring. Har safar bir xil amal bajariladi.',
      explanation: multiply ? 'Har safar $step ga ko‘paytiriladi. Javob: ${values.last}.' : 'Har safar $step qo‘shiladi. Javob: ${values.last}.',
      meta: {'ruleStart': start, 'ruleStep': step, 'multiply': multiply},
    );
  }

  static Exercise ordering(GenContext g) {
    final names = g.sample(_names, 3);
    final askFirst = g.chance(0.5);
    final distance = g.range(2, 25);
    return g.textChoice(
      question: '${names[0]} ${names[1]}dan $distance sm baland. ${names[1]} esa ${names[2]}dan baland. Kim eng ${askFirst ? 'baland' : 'past'}?',
      answer: askFirst ? names[0] : names[2],
      wrong: askFirst ? [names[1], names[2]] : [names[0], names[1]],
      concept: 'ordering:${names.join(':')}:$askFirst',
      hint: 'Uch bolaning bo‘yini uzunlik bo‘yicha ketma-ket joylashtiring.',
      explanation: 'Balanddan pastga: ${names.join(' → ')}.',
    );
  }

  static Exercise sets(GenContext g) {
    final both = g.range(1, 8);
    final chessOnly = g.range(2, 15);
    final musicOnly = g.range(2, 15);
    final chess = chessOnly + both, music = musicOnly + both;
    return g.numberAnswer(
      question: '$chess o‘quvchi shaxmatga, $music o‘quvchi musiqaga qatnaydi. Ulardan $both nafari ikkala to‘garakka ham qatnaydi. Kamida bitta to‘garakka qatnaydigan o‘quvchilar nechta?',
      answer: chessOnly + musicOnly + both,
      input: g.useInput(),
      concept: 'sets:$chess:$music:$both',
      hint: 'Ikkala to‘garakka qatnaydigan bolalarni ikki marta sanamang.',
      explanation: '$chess + $music − $both = ${chess + music - both}.',
      meta: {'setA': chess, 'setB': music, 'intersection': both},
    );
  }

  static Exercise timeline(GenContext g) {
    final year = g.range(1, 2025);
    final century = (year - 1) ~/ 100 + 1;
    return g.numberAnswer(
      question: 'Milodiy $year-yil nechanchi asrga kiradi? Asr raqamini toping.',
      answer: century,
      concept: 'century:$year',
      input: g.useInput(),
      hint: 'Birinchi asr — 1–100-yillar. Ikkinchi asr — 101–200-yillar.',
      explanation: '$century-asr ${(century - 1) * 100 + 1}–${century * 100}-yillarni qamraydi.',
      meta: {'year': year},
    );
  }

  static Exercise reading(GenContext g) {
    final names = g.sample(_names, 2);
    final a = names[0], b = names[1];
    final infer = g.pb('infer');
    final kind = g.range(0, 3);
    late String story, question, answer, explanation;
    late List<String> wrong;
    switch (kind) {
      case 0:
        story = '$a maktabga ketayotib, ${b}ning kitoblari yerga tushganini ko‘rdi. $a to‘xtab, kitoblarni yig‘ishga yordam berdi. Ular maktabga birga bordilar.';
        question = infer ? '${a}ning qaysi xususiyati namoyon bo‘ldi?' : '$a kimga yordam berdi?';
        answer = infer ? 'Yordamga tayyorligi' : b;
        wrong = infer ? ['Befarqligi', 'Maqtanchoqligi', 'Shoshqaloqligi'] : [a, 'Kutubxonachiga', 'Haydovchiga'];
        explanation = '$a yo‘lida to‘xtab, ${b}ga kitoblarini yig‘ishda yordam berdi.';
      case 1:
        story = '$a va $b nihol ekdilar. $a har kuni tuproqni tekshirib, kerak bo‘lsa suv quydi. Bir necha haftadan keyin niholda yangi barglar paydo bo‘ldi.';
        question = infer ? 'Matn uchun eng mos sarlavhani tanlang.' : '$a nima uchun tuproqni tekshirdi?';
        answer = infer ? 'Parvarishning natijasi' : 'Niholga suv kerakligini bilish uchun';
        wrong = infer ? ['Yo‘qolgan kitob', 'Qishki sayohat', 'Sport musobaqasi'] : ['Kitob izlash uchun', 'To‘p topish uchun', 'Yo‘l qurish uchun'];
        explanation = 'Matnda niholni parvarish qilish va yangi barglar chiqishi haqida aytilgan.';
      case 2:
        story = '$a kutubxonadan kitob oldi. Qaytarish kunini daftariga yozdi. O‘sha kuni $b bilan kutubxonaga borib, kitobni qaytardi.';
        question = infer ? '${a}ning ishidan qanday xulosa chiqarish mumkin?' : '$a qaytarish kunini qayerga yozdi?';
        answer = infer ? 'U olgan narsasini vaqtida qaytarishga mas’uliyat bilan qaradi' : 'Daftariga';
        wrong = infer ? ['U kitobni yo‘qotdi', 'U kutubxonaga bormadi', 'U qaytarish kunini unutdi'] : ['Devoriga', 'Doskasiga', 'Derazasiga'];
        explanation = '$a sanani daftariga yozdi va belgilangan kuni kitobni qaytardi.';
      default:
        story = '$a masalani birinchi urinishda yecha olmadi. $b javobni aytib bermadi, balki shartni yana o‘qishni maslahat berdi. $a chizma chizib, yechimni o‘zi topdi.';
        question = infer ? 'Matnning asosiy fikri qaysi?' : '$a yechimni topish uchun nima chizdi?';
        answer = infer ? 'Qayta o‘ylash va izlanish natija beradi' : 'Chizma';
        wrong = infer ? ['Qiyin ishni darhol tashlash kerak', 'Javobni ko‘chirib olish kerak', 'Masala shartini o‘qish shart emas'] : ['Xarita', 'Portret', 'Manzara'];
        explanation = '$a shartni qayta o‘qib, chizma yordamida mustaqil yechim topdi.';
    }
    return g.textChoice(
      question: '$story\n\n$question', answer: answer, wrong: wrong,
      concept: 'reading:$kind:$a:$b:$infer', options: g.p('options', 4),
      hint: infer ? 'Voqea, sabab va natija orasidagi bog‘lanishga e’tibor bering.' : 'Javob uchun matndagi tegishli gapni toping.',
      explanation: explanation,
    );
  }
}
