import 'dart:io';

import 'package:flutter/foundation.dart';
import 'package:image_picker/image_picker.dart';
import 'package:path_provider/path_provider.dart';

/// Bola rasmini tanlash va **faqat qurilmada** saqlash.
///
/// Rasm ilovaning shaxsiy hujjatlar papkasiga (`profile_photos/`) nusxalanadi.
/// Boshqa ilovalar uni ko'ra olmaydi, ilovada INTERNET ruxsati yo'q —
/// rasm hech qayerga yuborilmaydi. Ilova o'chirilsa, rasm ham o'chadi.
class ProfilePhotoService {
  ProfilePhotoService({ImagePicker? picker}) : _picker = picker ?? ImagePicker();

  final ImagePicker _picker;

  /// Rasm hajmi: profil doirasi uchun 720px yetarli (xotira va tezlik uchun).
  static const double maxSide = 720;

  Future<Directory> _photoDir() async {
    final docs = await getApplicationDocumentsDirectory();
    final dir = Directory('${docs.path}${Platform.pathSeparator}profile_photos');
    if (!dir.existsSync()) await dir.create(recursive: true);
    return dir;
  }

  /// Galereyadan (yoki kameradan) rasm tanlaydi va lokal nusxa yo'lini qaytaradi.
  /// Foydalanuvchi bekor qilsa `null`.
  Future<String?> pick({required String childId, bool fromCamera = false}) async {
    final XFile? file = await _picker.pickImage(
      source: fromCamera ? ImageSource.camera : ImageSource.gallery,
      maxWidth: maxSide,
      maxHeight: maxSide,
      imageQuality: 85,
      preferredCameraDevice: CameraDevice.front,
    );
    if (file == null) return null;
    final dir = await _photoDir();
    final safeId = childId.replaceAll(RegExp(r'[^a-zA-Z0-9_-]'), '_');
    final target =
        '${dir.path}${Platform.pathSeparator}${safeId}_${DateTime.now().millisecondsSinceEpoch}.jpg';
    await file.saveTo(target);
    return target;
  }

  /// Eski rasm faylini o'chiradi (faqat ilova papkasidagi fayllar).
  Future<void> delete(String? path) async {
    if (path == null || path.isEmpty) return;
    try {
      final f = File(path);
      if (f.existsSync() && path.contains('profile_photos')) await f.delete();
    } catch (e) {
      debugPrint('ProfilePhotoService: rasm o\'chirilmadi: $e');
    }
  }
}
