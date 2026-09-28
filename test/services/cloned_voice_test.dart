import 'package:academy/learning/content/instructions.dart';
import 'package:academy/services/cloned_voice.dart';
import 'package:academy/services/mother_voice.dart';
import 'package:flutter_test/flutter_test.dart';

/// Klonlangan ovoz fayllari matn xeshi bo'yicha topiladi — Python (`tool/voice/voice_keys.py`)
/// bilan aynan bir xil bo'lishi shart.
void main() {
  test('kalit Python bilan bir xil (FNV-1a 64)', () {
    expect(ClonedVoice.keyFor('Qaysi rasm boshqalardan farq qiladi?'), '5240d0ad310e573c');
    expect(ClonedVoice.keyFor("Besh qo'shuv uch  nechchi bo‘ladi? "), 'c1e668a1aa15779f');
    expect(ClonedVoice.keyFor('Yutuqlarim'), '3dc292749a0f7214');
    expect(ClonedVoice.keyFor('Кто играет?'), '0a4defc333dc277b');
  });

  test('normalizatsiya: apostrof va bo‘shliqlar', () {
    expect(ClonedVoice.normalize("  Yo'q,   bu  o`rdak "), 'Yo‘q, bu o‘rdak');
    expect(ClonedVoice.keyFor("to'g'ri"), ClonedVoice.keyFor('to‘g‘ri'));
    expect(ClonedVoice.keyFor('Olma'), isNot(ClonedVoice.keyFor('Olma?')));
  });

  test('onaning haqiqiy iborasi matn bo‘yicha topiladi', () {
    expect(MotherVoice.clipForText('Barakalla!'), 'barakalla');
    expect(MotherVoice.clipForText("to'g'ri topding!"), 'togri_topding');
    expect(MotherVoice.clipForText('Bir'), 'bir');
    expect(MotherVoice.clipForText('Qaysi hayvon katta?'), isNull);
  });

  test('ovozda son va qo‘shimcha qo‘shib aytiladi', () {
    expect(InstructionBank.toSpeech('18 ga 1 ni qo‘sh'), 'o‘n sakkizga birni qo‘sh');
    expect(InstructionBank.toSpeech('1 ta olma, 3 ta nok'), 'bitta olma, uchta nok');
    expect(InstructionBank.toSpeech('50 ga 40 ni qo‘sh'), 'ellikka qirqni qo‘sh');
    expect(InstructionBank.toSpeech('12 dan 2 ni ayir'), 'o‘n ikkidan ikkini ayir');
    expect(InstructionBank.toSpeech('B4 katagini bos'), 'B to‘rt katagini bos');
    expect(InstructionBank.toSpeech('7 + 3 = ?'), 'yetti qo‘shuv uch teng ?');
    expect(InstructionBank.speechFor('Tap the square b4', 'en'), 'Tap the square b four');
  });
}
