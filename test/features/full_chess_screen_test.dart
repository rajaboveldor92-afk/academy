import 'package:academy/core/providers.dart';
import 'package:academy/database/local_database.dart';
import 'package:academy/features/chess/full_chess_game.dart';
import 'package:academy/features/chess/full_chess_screen.dart';
import 'package:academy/models/child_profile.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  testWidgets('two-player board moves, saves, undoes and stays usable on small screen', (tester) async {
    tester.view.physicalSize = const Size(360,640);
    tester.view.devicePixelRatio = 1;
    addTearDown(tester.view.resetPhysicalSize); addTearDown(tester.view.resetDevicePixelRatio);
    final db = LocalDatabase.memory();
    final profile = ChildProfile.create(id:'test',name:'Test',age:4,avatar:'🐻');
    await db.saveChessGame(profile.id,FullChessGame(mode:'local').toMap());
    await tester.pumpWidget(ProviderScope(overrides:[databaseProvider.overrideWithValue(db)],child:MaterialApp(home:FullChessScreen(profile:profile))));
    await tester.pumpAndSettle();
    await tester.tap(find.byKey(const Key('full_square_e2')));
    await tester.pump();
    await tester.tap(find.byKey(const Key('full_square_e4')));
    await tester.pumpAndSettle();
    expect(find.text('Qoralar yuradi'),findsOneWidget);
    expect(db.getChessGame(profile.id)!['moves'],['e4']);
    await tester.tap(find.text('Qaytarish'));
    await tester.pumpAndSettle();
    expect(find.text('Oqlar yuradi'),findsOneWidget);
    expect(tester.takeException(),isNull);
  });
}
