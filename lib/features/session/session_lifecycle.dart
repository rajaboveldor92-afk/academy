import 'package:flutter/widgets.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../core/providers.dart';
import 'session_controller.dart';

/// Ilova fonga o'tganda vaqt hisobini to'xtatadi, qaytganda davom ettiradi.
class SessionLifecycle extends ConsumerStatefulWidget {
  const SessionLifecycle({super.key, required this.child});

  final Widget child;

  @override
  ConsumerState<SessionLifecycle> createState() => _SessionLifecycleState();
}

class _SessionLifecycleState extends ConsumerState<SessionLifecycle>
    with WidgetsBindingObserver {
  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addObserver(this);
  }

  @override
  void dispose() {
    WidgetsBinding.instance.removeObserver(this);
    super.dispose();
  }

  @override
  void didChangeAppLifecycleState(AppLifecycleState state) {
    final session = ref.read(sessionProvider.notifier);
    final foreground = state == AppLifecycleState.resumed;
    if (foreground) {
      session.resume();
    } else {
      session.pause();
    }
    // Fonda nutq to'xtaydi, musiqa pauza qilinadi.
    ref.read(audioServiceProvider).setForeground(foreground);
  }

  @override
  Widget build(BuildContext context) => widget.child;
}
