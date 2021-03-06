from match import match
perfect_unison, minor_second, augmented_unison, major_second,\
diminished_third, minor_third, augmented_second, major_third,\
diminished_fourth, perfect_fourth, augmented_third, diminished_fifth,\
augmented_fourth, perfect_fifth, diminished_sixth, minor_sixth,\
augmented_fifth, major_sixth, diminished_seventh, minor_seventh,\
augmented_sixth, major_seventh, diminished_octave, perfect_octave,\
octave, augmented_seventh = 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7,\
7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 12
INTERVAL = {
    0: ('perfect unison', ),
    1: ('minor second', 'augmented unison'),
    2: ('major second', 'diminished third'),
    3: ('minor third', 'augmented second'),
    4: ('major third', 'diminished fourth'),
    5: ('perfect fourth', 'augmented third'),
    6: ('diminished fifth', 'augmented fourth'),
    7: ('perfect fifth', 'diminished sixth'),
    8: ('minor sixth', 'augmented fifth'),
    9: ('major sixth', 'diminished seventh'),
    10: ('minor seventh', 'augmented sixth'),
    11: ('major seventh', 'diminished octave'),
    12: ('perfect octave', 'octave', 'augmented seventh')
}
NAME_OF_INTERVAL = {
    'perfect unison': 0,
    'minor second': 1,
    'augmented unison': 1,
    'major second': 2,
    'diminished third': 2,
    'minor third': 3,
    'augmented second': 3,
    'major third': 4,
    'diminished fourth': 4,
    'perfect fourth': 5,
    'augmented third': 5,
    'diminished fifth': 6,
    'augmented fourth': 6,
    'perfect fifth': 7,
    'diminished sixth': 7,
    'minor sixth': 8,
    'augmented fifth': 8,
    'major sixth': 9,
    'diminished seventh': 9,
    'minor seventh': 10,
    'augmented sixth': 10,
    'major seventh': 11,
    'diminished octave': 11,
    'perfect octave': 12,
    'octave': 12,
    'augmented seventh': 12
}
standard = {
    'C': 0,
    'C#': 1,
    'D': 2,
    'D#': 3,
    'E': 4,
    'F': 5,
    'F#': 6,
    'G': 7,
    'G#': 8,
    'A': 9,
    'A#': 10,
    'B': 11,
    'Bb': 10,
    'Eb': 3,
    'Ab': 8,
    'Db': 1,
    'Gb': 6
}
standard2 = {
    'C': 0,
    'C#': 1,
    'D': 2,
    'D#': 3,
    'E': 4,
    'F': 5,
    'F#': 6,
    'G': 7,
    'G#': 8,
    'A': 9,
    'A#': 10,
    'B': 11
}
scaleTypes = match({
    ('major', ): [2, 2, 1, 2, 2, 2, 1],
    ('minor', ): [2, 1, 2, 2, 1, 2, 2],
    ('melodic minor', ): [2, 1, 2, 2, 2, 2, 1],
    ('harmonic minor', ): [2, 1, 2, 2, 1, 3, 1],
    ('lydian', ): [2, 2, 2, 1, 2, 2, 1],
    ('dorian', ): [2, 1, 2, 2, 2, 1, 2],
    ('phrygian', ): [1, 2, 2, 2, 1, 2, 2],
    ('mixolydian', ): [2, 2, 1, 2, 2, 1, 2],
    ('locrian', ): [1, 2, 2, 1, 2, 2, 2],
    ('whole tone', ): [2, 2, 2, 2, 2, 2],
    ('12', ): [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
})
modern_modes = [
    'major', 'dorian', 'phrygian', 'lydian', 'mixolydian', 'minor', 'locrian'
]
chordTypes = match({
    ('major', 'M', 'maj', 'majorthird'): ((4, 7), ),
    ('minor', 'm', 'minorthird', 'min'): ((3, 7), ),
    ('maj7', 'M7', 'major7th', 'majorseventh'): ((4, 7, 11), ),
    ('m7', 'min7', 'minor7th', 'minorseventh'): ((3, 7, 10), ),
    ('7', 'seven', 'seventh', 'dominant seventh', 'dom7', 'dominant7', 'germansixth'):
    ((4, 7, 10), ),
    ('minormajor7', 'minor major 7', 'mM7'): ((3, 7, 11), ),
    ('dim', 'dim3', '-'): ((3, 6), ),
    ('dim7', '-7'): ((3, 6, 9), ),
    ('half-diminished7', 'ø7', 'ø', 'half-diminished', 'half-dim', 'o7', 'o', 'm7b5'):
    ((3, 6, 10), ),
    ('aug', 'augmented', '+', 'aug3', '+3'): ((4, 8), ),
    ('aug7', 'augmented7', '+7'): ((4, 8, 10), ),
    ('augmaj7', 'augmented-major7', '+maj7'): ((4, 8, 11), ),
    ('aug6', 'augmented6', '+6', 'italian-sixth'): ((4, 10), ),
    ('frenchsixth', ): ((4, 6, 10), ),
    ('aug9', '+9'): ((4, 8, 10, 14), ),
    ('augmaj9', '+maj9'): ((4, 8, 11, 14), ),
    ('sus', 'sus4'): ((5, 7), ),
    ('sus2', ): ((2, 7), ),
    ('9', 'dominant9', 'dominant-ninth', 'ninth'): ((4, 7, 10, 14), ),
    ('maj9', 'major-ninth', 'major9th'): ((4, 7, 11, 14), ),
    ('m9', 'minor9', 'minor9th'): ((3, 7, 10, 14), ),
    ('add6', '6', 'sixth'): ((4, 7, 9), ),
    ('m6', 'minorsixth'): ((3, 7, 9), ),
    ('add2', '+2'): ((2, 4, 7), ),
    ('add9', '+9'): ((4, 7, 14), ),
    ('madd2', 'm+2'): ((2, 3, 7), ),
    ('madd9', 'm+9'): ((3, 7, 14), ),
    ('7sus4', '7sus'): ((5, 7, 10), ),
    ('7sus2', ): ((2, 7, 10), ),
    ('maj7sus4', 'maj7sus', 'M7sus4'): ((5, 7, 11), ),
    ('maj7sus2', 'M7sus2'): ((2, 7, 11), ),
    ('9sus4', '9sus'): ((5, 7, 10, 14), ),
    ('9sus2', ): ((2, 7, 10, 14), ),
    ('maj9sus4', 'maj9sus'): ((5, 7, 11, 14), ),
    ('maj9sus2', ): ((2, 7, 11, 14), ),
    ('13sus4', '13sus'): ((5, 7, 10, 14, 17, 21), ),
    ('13sus2', ): ((2, 7, 10, 14, 17, 21), ),
    ('maj13sus4', 'maj13sus'): ((5, 7, 11, 14, 17, 21), ),
    ('maj13sus2', ): ((2, 7, 11, 14, 17, 21), ),
    ('add4', '+4'): ((4, 5, 7), ),
    ('madd4', 'm+4'): ((3, 5, 7), ),
    ('add24', '24', 'sus2sus4'): ((2, 5), ),
    ('add2omit5', ): ((2, 4), ),
    ('madd2omit5', ): ((2, 3), ),
    ('maj7#11', ): ((4, 7, 11, 18), ),
    ('m7#11', ): ((3, 7, 10, 18), ),
    ('7#11', ): ((4, 7, 10, 18), ),
    ('maj9#11', ): ((4, 7, 11, 14, 18), ),
    ('m9#11', ): ((3, 7, 10, 14, 18), ),
    ('9#11', ): ((4, 7, 10, 14, 18), ),
    ('69', '6/9', 'add69'): ((4, 7, 9, 14), ),
    ('m69', 'madd69'): ((3, 7, 9, 14), ),
    ('6sus4', '6sus'): ((5, 7, 9), ),
    ('6sus2', ): ((2, 7, 9), ),
    ('5', 'power chord'): ((7, ), ),
    ('5(+octave)', 'power chord(with octave)'): ((7, 12), ),
    ('11', 'M11', 'maj11', 'eleventh', 'major 11', 'major eleventh'):
    ((4, 7, 11, 14, 17), ),
    ('m11', 'minor eleventh', 'minor 11'): ((3, 7, 10, 14, 17), ),
    ('dominant11', 'dominant eleventh'): ((4, 7, 10, 14, 17), ),
    ('13', 'dominant 13'): ((4, 7, 10, 14, 17, 21), ),
    ('maj13', 'major 13'): ((4, 7, 11, 14, 17, 21), ),
    ('m13', 'minor 13'): ((3, 7, 10, 14, 17, 21), ),
    ('maj7add13', ): ((4, 7, 11, 21), ),
    ('maj7#13', ): ((4, 7, 11, 14, 22), ),
    ('maj13#11', ): ((4, 7, 11, 14, 18, 21), ),
    ('13#11', ): ((4, 7, 10, 14, 18, 21), ),
    ('m13#11', ): ((3, 7, 10, 14, 18, 21), ),
    ('fifth 9th', ): ((7, 14), ),
    ('minormajor9', 'minor major 9', 'mM9'): ((3, 7, 11, 14), )
})
standard_reverse = {j: i for i, j in standard2.items()}
detectScale = scaleTypes.reverse()
detectTypes = chordTypes.reverse()
notedict = {
    'C': 'C',
    'c': 'C#',
    'D': 'D',
    'd': 'D#',
    'E': 'E',
    'F': 'F',
    'f': 'F#',
    'G': 'G',
    'g': 'G#',
    'A': 'A',
    'a': 'A#',
    'B': 'B',
    ' ': 'interval'
}
