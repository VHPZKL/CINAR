basic.forever(function on_forever() {
    basic.showNumber(0)
    basic.showLeds(`
        # # # # #
                # . . . .
                # . . . .
                # . . . .
                # # # # #
    `)
    basic.showLeds(`
        . . # . .
                . . # . .
                . . # . .
                . . # . .
                . . # . .
    `)
    basic.showLeds(`
        # . . . #
                # # . . #
                # . # . #
                # . . # #
                # . . . #
    `)
    basic.showLeds(`
        . . # . .
                . # . # .
                . # . # .
                # . . . #
                # . . . #
    `)
    basic.showLeds(`
        # # # # #
                # . . . #
                # # # # #
                # . # . .
                # . . # .
    `)
    music.playMelody("E B C5 A B G A F ", 500)
    music.changeTempoBy(22)
    music.startMelody(music.builtInMelody(Melodies.Funk), MelodyOptions.ForeverInBackground)
    music.playSoundEffect(music.createSoundEffect(WaveShape.Square, 1600, 5000, 255, 255, 1000, SoundExpressionEffect.None, InterpolationCurve.Curve), SoundExpressionPlayMode.InBackground)
    basic.showArrow(ArrowNames.East)
    music.setVolume(255)
})
