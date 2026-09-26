import 'package:flutter/material.dart';

import '../../core/constants/app_constants.dart';
import '../../router/app_router.dart';
import '../../theme/app_colors.dart';

/// Qisqa (≈1.2 soniya) kirish ekrani.
class SplashScreen extends StatefulWidget {
  const SplashScreen({super.key});

  @override
  State<SplashScreen> createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen> {
  @override
  void initState() {
    super.initState();
    Future<void>.delayed(AppConstants.splashDuration, () {
      if (!mounted) return;
      Navigator.of(context).pushReplacementNamed(AppRoutes.profiles);
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.secondary,
      body: SafeArea(
        child: Center(
          child: Padding(
            padding: const EdgeInsets.all(24),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                const AppLogo(size: 140),
                const SizedBox(height: 28),
                Text(
                  AppConstants.appName,
                  textAlign: TextAlign.center,
                  style: Theme.of(context).textTheme.headlineMedium?.copyWith(color: Colors.white),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

/// Oddiy logo: kitob + yulduz + shaxmat oti.
class AppLogo extends StatelessWidget {
  const AppLogo({super.key, this.size = 120});

  final double size;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: size,
      height: size,
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(size * 0.28),
        boxShadow: const [
          BoxShadow(color: Color(0x33000000), blurRadius: 16, offset: Offset(0, 8)),
        ],
      ),
      child: Stack(
        alignment: Alignment.center,
        children: [
          Text('📖', style: TextStyle(fontSize: size * 0.5)),
          Positioned(
            top: size * 0.06,
            right: size * 0.08,
            child: Text('⭐', style: TextStyle(fontSize: size * 0.24)),
          ),
          Positioned(
            bottom: size * 0.04,
            left: size * 0.08,
            child: Text('♞', style: TextStyle(fontSize: size * 0.26, color: AppColors.primary)),
          ),
        ],
      ),
    );
  }
}
