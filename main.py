78def on_forever():
    basic.show_number(0)
    basic.show_leds("""
        # # # # #
                # . . . .
                # . . . .
                # . . . .
                # # # # #
    """)
    basic.show_leds("""
        . . # . .
                . . # . .
                . . # . .
                . . # . .
                . . # . .
    """)
    basic.show_leds("""
        # . . . #
                # # . . #
                # . # . #
                # . . # #
                # . . . #
    """)
    basic.show_leds("""
        . . # . .
                . # . # .
                . # . # .
                # . . . #
                # . . . #
    """)
    basic.show_leds("""
        # # # # #
                # . . . #
                # # # # #
                # . # . .
                # . . # .
    """)
    music.play_melody("E B C5 A B G A F ", 500)
    music.change_tempo_by(22)
    music.start_melody(music.built_in_melody(Melodies.FUNK),
        MelodyOptions.FOREVER_IN_BACKGROUND)
    music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
            1600,
            5000,
            255,
            255,
            1000,
            SoundExpressionEffect.NONE,
            InterpolationCurve.CURVE),
        SoundExpressionPlayMode.IN_BACKGROUND)
    basic.show_arrow(ArrowNames.EAST)
    music.set_volume(255)
basic.forever(on_forever)
