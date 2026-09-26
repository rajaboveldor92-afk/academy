/// Kontent guruhi. Bola yoshi o'zgarsa guruh avtomatik o'zgaradi —
/// hech narsa bola ismiga bog'lanmagan.
enum AgeGroup {
  /// 3–5 yosh: juda vizual, qisqa, bitta vazifali topshiriqlar.
  junior(suffix: '4', sessionMinMinutes: 5, sessionMaxMinutes: 10),

  /// 6–8 yosh: murakkabroq topshiriqlar.
  senior(suffix: '6', sessionMinMinutes: 10, sessionMaxMinutes: 20);

  const AgeGroup({
    required this.suffix,
    required this.sessionMinMinutes,
    required this.sessionMaxMinutes,
  });

  /// JSON kontent fayllari qo'shimchasi: `math_4.json`, `math_6.json`.
  final String suffix;
  final int sessionMinMinutes;
  final int sessionMaxMinutes;

  static AgeGroup fromAge(int age) => age <= 5 ? AgeGroup.junior : AgeGroup.senior;

  bool get isJunior => this == AgeGroup.junior;
}
