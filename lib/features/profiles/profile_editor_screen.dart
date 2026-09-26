import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../core/constants/app_constants.dart';
import '../../core/providers.dart';
import '../../models/child_profile.dart';
import '../../services/profile_photo_service.dart';
import '../../theme/app_colors.dart';
import '../../theme/profile_themes.dart';
import '../../widgets/profile_photo.dart';
import 'profiles_controller.dart';

/// Profil yaratish yoki tahrirlash (faqat ota-ona bo'limidan, PIN orqali).
///
/// Tahrirlanadi: rasm, to'liq ism, qisqa ism, yosh, mavzu (ramka), avatar,
/// salomlashuv matni. Rasm faqat qurilmada saqlanadi.
class ProfileEditorScreen extends ConsumerStatefulWidget {
  const ProfileEditorScreen({super.key, this.initial});

  /// `null` bo'lsa — yangi profil.
  final ChildProfile? initial;

  @override
  ConsumerState<ProfileEditorScreen> createState() => _ProfileEditorScreenState();
}

class _ProfileEditorScreenState extends ConsumerState<ProfileEditorScreen> {
  late final TextEditingController _name;
  late final TextEditingController _fullName;
  late final TextEditingController _greeting;
  late int _age;
  late String _avatar;
  late int _themeIndex;
  String? _photoPath;
  late final ProfilePhotoService _photos;

  /// Saqlanmagan holda tanlangan yangi rasmlar — bekor qilinsa o'chiriladi.
  final List<String> _pickedPhotos = [];
  String? _error;
  bool _saving = false;
  bool _saved = false;

  bool get _isEdit => widget.initial != null;

  @override
  void initState() {
    super.initState();
    final p = widget.initial;
    _name = TextEditingController(text: p?.name ?? '');
    _fullName = TextEditingController(text: p?.fullName ?? '');
    _greeting = TextEditingController(text: p?.greeting ?? '');
    _age = p?.age ?? 5;
    _avatar = p?.avatar ?? AppConstants.avatars.first;
    _themeIndex = (p?.colorIndex ?? ref.read(profilesProvider).length) % ProfileThemes.all.length;
    _photoPath = p?.photoPath;
    _photos = ref.read(profilePhotoServiceProvider);
  }

  @override
  void dispose() {
    if (!_saved) {
      // Saqlanmagan rasmlar qurilmada ortiqcha joy egallamasin.
      for (final path in _pickedPhotos) {
        _photos.delete(path);
      }
    }
    _name.dispose();
    _fullName.dispose();
    _greeting.dispose();
    super.dispose();
  }

  /// Oldindan ko'rish uchun joriy qiymatlardan profil.
  ChildProfile get _preview => ChildProfile(
        id: widget.initial?.id ?? 'preview',
        name: _name.text.trim().isEmpty ? 'Ism' : _name.text.trim(),
        fullName: _fullName.text.trim(),
        age: _age,
        avatar: _avatar,
        photoPath: _photoPath,
        greeting: _greeting.text.trim(),
        colorIndex: _themeIndex,
        dailyLimitMinutes: 0,
        createdAt: DateTime.fromMillisecondsSinceEpoch(0),
      );

  Future<void> _pickPhoto({required bool fromCamera}) async {
    try {
      final path = await _photos.pick(
            childId: widget.initial?.id ?? 'new',
            fromCamera: fromCamera,
          );
      if (path == null || !mounted) return;
      setState(() {
        _pickedPhotos.add(path);
        _photoPath = path;
      });
    } catch (e) {
      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text("Rasmni ochib bo'lmadi: $e")),
      );
    }
  }

  Future<void> _showPhotoOptions() async {
    await showModalBottomSheet<void>(
      context: context,
      showDragHandle: true,
      builder: (ctx) => SafeArea(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            ListTile(
              leading: const Icon(Icons.photo_library_rounded),
              title: const Text('Galereyadan tanlash'),
              onTap: () {
                Navigator.of(ctx).pop();
                _pickPhoto(fromCamera: false);
              },
            ),
            ListTile(
              leading: const Icon(Icons.photo_camera_rounded),
              title: const Text('Kamerada suratga olish'),
              onTap: () {
                Navigator.of(ctx).pop();
                _pickPhoto(fromCamera: true);
              },
            ),
            if (_photoPath != null)
              ListTile(
                leading: const Icon(Icons.hide_image_outlined),
                title: const Text("Rasmni olib tashlash (avatar ko'rsatiladi)"),
                onTap: () {
                  Navigator.of(ctx).pop();
                  setState(() => _photoPath = null);
                },
              ),
          ],
        ),
      ),
    );
  }

  Future<void> _save() async {
    setState(() {
      _error = null;
      _saving = true;
    });
    try {
      final notifier = ref.read(profilesProvider.notifier);
      final initial = widget.initial;
      if (initial == null) {
        await notifier.create(
          name: _name.text,
          fullName: _fullName.text,
          greeting: _greeting.text,
          age: _age,
          avatar: _avatar,
          colorIndex: _themeIndex,
          photoPath: _photoPath,
        );
      } else {
        await notifier.updateProfile(initial.copyWith(
          name: _name.text.trim(),
          fullName: _fullName.text.trim(),
          greeting: _greeting.text.trim(),
          age: _age,
          avatar: _avatar,
          colorIndex: _themeIndex,
          photoPath: _photoPath,
          clearPhoto: _photoPath == null,
        ));
      }
      _saved = true;
      // Almashtirilgan eski rasm va ishlatilmay qolgan tanlovlarni tozalash.
      final old = initial?.photoPath;
      if (old != null && old != _photoPath) await _photos.delete(old);
      for (final path in _pickedPhotos) {
        if (path != _photoPath) await _photos.delete(path);
      }
      if (mounted) Navigator.of(context).pop(true);
    } on ProfileValidationException catch (e) {
      setState(() => _error = e.message);
    } finally {
      if (mounted) setState(() => _saving = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    final textTheme = Theme.of(context).textTheme;
    final preview = _preview;
    final theme = ProfileThemes.of(_themeIndex);

    return Scaffold(
      appBar: AppBar(title: Text(_isEdit ? 'Profilni tahrirlash' : 'Yangi profil')),
      body: SafeArea(
        child: ListView(
          padding: const EdgeInsets.all(20),
          children: [
            // Oldindan ko'rish: bola kartada qanday ko'radi.
            Container(
              padding: const EdgeInsets.symmetric(vertical: 20, horizontal: 12),
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(32),
                gradient: LinearGradient(
                  begin: Alignment.topCenter,
                  end: Alignment.bottomCenter,
                  colors: theme.gradient,
                ),
              ),
              child: Column(
                children: [
                  GestureDetector(
                    key: const Key('photo_picker'),
                    onTap: _showPhotoOptions,
                    child: ProfilePhoto(profile: preview, size: 150),
                  ),
                  const SizedBox(height: 8),
                  TextButton.icon(
                    onPressed: _showPhotoOptions,
                    icon: const Icon(Icons.add_a_photo_rounded),
                    label: Text(_photoPath == null ? "Rasm qo'shish" : 'Rasmni almashtirish'),
                  ),
                  Text(
                    preview.displayFullName,
                    textAlign: TextAlign.center,
                    style: const TextStyle(fontSize: 22, fontWeight: FontWeight.w900),
                  ),
                  Text('$_age yosh', style: TextStyle(color: theme.primary, fontWeight: FontWeight.w700)),
                ],
              ),
            ),
            const SizedBox(height: 8),
            Text(
              "🔒 Rasm faqat shu telefonda saqlanadi va hech qayerga yuborilmaydi.",
              style: textTheme.bodyMedium?.copyWith(color: AppColors.textSoft),
            ),
            const SizedBox(height: 20),
            Text("To'liq ism (kartada)", style: textTheme.titleMedium),
            const SizedBox(height: 8),
            TextField(
              key: const Key('full_name_field'),
              controller: _fullName,
              maxLength: AppConstants.maxFullNameLength,
              textCapitalization: TextCapitalization.words,
              onChanged: (_) => setState(() {}),
              style: const TextStyle(fontSize: 20, fontWeight: FontWeight.w700),
              decoration: const InputDecoration(hintText: 'Masalan: Odilbekov Azamjon Eldorovich'),
            ),
            const SizedBox(height: 8),
            Text('Qisqa ism (murojaat uchun)', style: textTheme.titleMedium),
            const SizedBox(height: 8),
            TextField(
              key: const Key('name_field'),
              controller: _name,
              maxLength: AppConstants.maxNameLength,
              textCapitalization: TextCapitalization.words,
              onChanged: (_) => setState(() {}),
              style: const TextStyle(fontSize: 20, fontWeight: FontWeight.w700),
              decoration: InputDecoration(hintText: 'Masalan: Azamjon', errorText: _error),
            ),
            const SizedBox(height: 8),
            Text('Yosh', style: textTheme.titleMedium),
            const SizedBox(height: 8),
            Wrap(
              spacing: 10,
              runSpacing: 10,
              children: [
                for (var a = AppConstants.minAge; a <= AppConstants.maxAge; a++)
                  ChoiceChip(
                    key: Key('age_$a'),
                    label: Text('$a', style: const TextStyle(fontSize: 22)),
                    selected: _age == a,
                    onSelected: (_) => setState(() => _age = a),
                    padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                  ),
              ],
            ),
            const SizedBox(height: 20),
            Text('Profil mavzusi va ramkasi', style: textTheme.titleMedium),
            const SizedBox(height: 8),
            Wrap(
              spacing: 10,
              runSpacing: 10,
              children: [
                for (var i = 0; i < ProfileThemes.all.length; i++)
                  _ThemeChip(
                    theme: ProfileThemes.all[i],
                    selected: i == _themeIndex,
                    onTap: () => setState(() => _themeIndex = i),
                  ),
              ],
            ),
            const SizedBox(height: 20),
            Text("Avatar (rasm bo'lmasa ko'rinadi)", style: textTheme.titleMedium),
            const SizedBox(height: 8),
            Wrap(
              spacing: 8,
              runSpacing: 8,
              children: [
                for (final a in AppConstants.avatars)
                  GestureDetector(
                    onTap: () => setState(() => _avatar = a),
                    child: Container(
                      width: 54,
                      height: 54,
                      alignment: Alignment.center,
                      decoration: BoxDecoration(
                        color: theme.light,
                        shape: BoxShape.circle,
                        border: Border.all(
                          color: a == _avatar ? theme.primary : Colors.transparent,
                          width: 3,
                        ),
                      ),
                      child: Text(a, style: const TextStyle(fontSize: 28)),
                    ),
                  ),
              ],
            ),
            const SizedBox(height: 20),
            Text('Salomlashuv (ikkinchi qator)', style: textTheme.titleMedium),
            const SizedBox(height: 8),
            TextField(
              key: const Key('greeting_field'),
              controller: _greeting,
              maxLength: 60,
              onChanged: (_) => setState(() {}),
              decoration: InputDecoration(hintText: preview.welcomeSubtitle),
            ),
            Text(
              'Bola ko\'radi: "${preview.welcomeTitle}  ${preview.welcomeSubtitle}"',
              style: textTheme.bodyMedium?.copyWith(color: AppColors.textSoft),
            ),
            const SizedBox(height: 28),
            FilledButton(
              key: const Key('save_profile'),
              onPressed: _saving ? null : _save,
              child: const Text('Saqlash'),
            ),
          ],
        ),
      ),
    );
  }
}

class _ThemeChip extends StatelessWidget {
  const _ThemeChip({required this.theme, required this.selected, required this.onTap});

  final ProfileTheme theme;
  final bool selected;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      key: Key('theme_${theme.id}'),
      onTap: onTap,
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 200),
        width: 96,
        padding: const EdgeInsets.symmetric(vertical: 10),
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(20),
          gradient: LinearGradient(colors: theme.gradient),
          border: Border.all(
            color: selected ? AppColors.text : Colors.transparent,
            width: 3,
          ),
        ),
        child: Column(
          children: [
            Text(theme.emoji, style: const TextStyle(fontSize: 28)),
            Text(theme.name, style: const TextStyle(fontWeight: FontWeight.w700)),
          ],
        ),
      ),
    );
  }
}
