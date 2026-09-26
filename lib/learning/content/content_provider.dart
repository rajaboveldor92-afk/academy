import 'package:flutter_riverpod/flutter_riverpod.dart';

import 'content_repository.dart';

/// O'quv kontenti (bir marta yuklanadi va keshlanadi).
final contentProvider = FutureProvider<ContentRepository>((ref) => ContentRepository.load());
