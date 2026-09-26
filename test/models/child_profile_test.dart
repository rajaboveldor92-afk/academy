import 'package:academy/core/utils/age_group.dart';
import 'package:academy/models/child_profile.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  group('ChildProfile', () {
    test('yangi profil yoshga mos standart limit oladi', () {
      final young = ChildProfile.create(id: 'a', name: ' Ali ', age: 4, avatar: '🦁');
      final older = ChildProfile.create(id: 'b', name: 'Vali', age: 6, avatar: '🐻');
      expect(young.name, 'Ali');
      expect(young.dailyLimitMinutes, 15);
      expect(older.dailyLimitMinutes, 20);
    });

    test('yosh guruhi faqat yoshga bog\'liq, ismga emas', () {
      final p = ChildProfile.create(id: 'x', name: 'Azamjon', age: 4, avatar: '🦁');
      expect(p.ageGroup, AgeGroup.junior);
      expect(p.copyWith(age: 6).ageGroup, AgeGroup.senior);
      expect(AgeGroup.fromAge(5), AgeGroup.junior);
      expect(AgeGroup.fromAge(7), AgeGroup.senior);
      expect(AgeGroup.junior.suffix, '4');
      expect(AgeGroup.senior.suffix, '6');
    });

    test('toMap/fromMap aylanishi ma\'lumotni yo\'qotmaydi', () {
      final p = ChildProfile.create(
        id: 'id1',
        name: 'Muhammadjon',
        age: 4,
        avatar: '🐻',
        colorIndex: 2,
        now: DateTime(2026, 1, 2, 3, 4, 5),
      ).copyWith(disabledSubjects: ['chess'], difficultyBias: -1);
      final restored = ChildProfile.fromMap(p.toMap());
      expect(restored, p);
      expect(restored.createdAt, DateTime(2026, 1, 2, 3, 4, 5));
      expect(restored.isSubjectEnabled('chess'), isFalse);
      expect(restored.isSubjectEnabled('math'), isTrue);
    });

    test('buzilgan qiymatlar xavfsiz o\'qiladi', () {
      final p = ChildProfile.fromMap({'id': 'z', 'age': '5', 'difficultyBias': 9});
      expect(p.age, 5);
      expect(p.difficultyBias, 1);
      expect(p.avatar, isNotEmpty);
    });
  });
}
