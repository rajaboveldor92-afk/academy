import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../core/constants/app_constants.dart';
import '../../models/child_profile.dart';
import '../../theme/app_colors.dart';
import '../../widgets/avatar_bubble.dart';
import 'profiles_controller.dart';

/// Yangi profil yaratish yoki mavjudini tahrirlash.
class ProfileEditorScreen extends ConsumerStatefulWidget {
  const ProfileEditorScreen({super.key, this.initial});

  /// `null` bo'lsa — yangi profil.
  final ChildProfile? initial;

  @override
  ConsumerState<ProfileEditorScreen> createState() => _ProfileEditorScreenState();
}

class _ProfileEditorScreenState extends ConsumerState<ProfileEditorScreen> {
  late final TextEditingController _name;
  late int _age;
  late String _avatar;
  late int _colorIndex;
  String? _error;
  bool _saving = false;

  bool get _isEdit => widget.initial != null;

  @override
  void initState() {
    super.initState();
    final p = widget.initial;
    _name = TextEditingController(text: p?.name ?? '');
    _age = p?.age ?? 5;
    _avatar = p?.avatar ?? AppConstants.avatars.first;
    _colorIndex = (p?.colorIndex ?? ref.read(profilesProvider).length) %
        AppColors.profilePalette.length;
  }

  @override
  void dispose() {
    _name.dispose();
    super.dispose();
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
          age: _age,
          avatar: _avatar,
          colorIndex: _colorIndex,
        );
      } else {
        await notifier.updateProfile(initial.copyWith(
          name: _name.text.trim(),
          age: _age,
          avatar: _avatar,
          colorIndex: _colorIndex,
        ));
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
    final color = AppColors.profileColor(_colorIndex);
    final textTheme = Theme.of(context).textTheme;

    return Scaffold(
      appBar: AppBar(title: Text(_isEdit ? 'Profilni tahrirlash' : 'Yangi profil')),
      body: SafeArea(
        child: ListView(
          padding: const EdgeInsets.all(20),
          children: [
            Center(child: AvatarBubble(avatar: _avatar, color: color, size: 120, selected: true)),
            const SizedBox(height: 24),
            Text('Ism', style: textTheme.titleMedium),
            const SizedBox(height: 8),
            TextField(
              key: const Key('name_field'),
              controller: _name,
              maxLength: AppConstants.maxNameLength,
              textCapitalization: TextCapitalization.words,
              style: const TextStyle(fontSize: 22, fontWeight: FontWeight.w700),
              decoration: InputDecoration(hintText: 'Masalan: Azamjon', errorText: _error),
            ),
            const SizedBox(height: 12),
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
            Text('Avatar', style: textTheme.titleMedium),
            const SizedBox(height: 8),
            Wrap(
              spacing: 10,
              runSpacing: 10,
              children: [
                for (final a in AppConstants.avatars)
                  GestureDetector(
                    onTap: () => setState(() => _avatar = a),
                    child: AvatarBubble(avatar: a, color: color, size: 60, selected: a == _avatar),
                  ),
              ],
            ),
            const SizedBox(height: 20),
            Text('Rang', style: textTheme.titleMedium),
            const SizedBox(height: 8),
            Wrap(
              spacing: 12,
              runSpacing: 12,
              children: [
                for (var i = 0; i < AppColors.profilePalette.length; i++)
                  GestureDetector(
                    onTap: () => setState(() => _colorIndex = i),
                    child: Container(
                      width: 48,
                      height: 48,
                      decoration: BoxDecoration(
                        color: AppColors.profilePalette[i],
                        shape: BoxShape.circle,
                        border: Border.all(
                          color: i == _colorIndex ? AppColors.text : Colors.transparent,
                          width: 4,
                        ),
                      ),
                    ),
                  ),
              ],
            ),
            const SizedBox(height: 32),
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
