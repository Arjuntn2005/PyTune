sharp_notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
flat_notes = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

major_steps = [2, 2, 1, 2, 2, 2, 1]
minor_steps = [2, 1, 2, 2, 1, 2, 2]
mohanam_steps = [2, 2, 3, 2, 3]        # S R2 G3 P D2
hamsadhwani_steps = [2, 2, 3, 4]        # S R2 G3 P N3

major_chords = ['major', 'minor', 'minor', 'major', 'major', 'minor', 'diminished']
minor_chords = ['minor', 'diminished', 'major', 'minor', 'minor', 'major', 'major']
mohanam_chords = ['major', 'minor', 'minor', 'major', 'major']
hamsadhwani_chords = ['major', 'minor', 'minor', 'major', 'major']

notes = flat_notes if key[-1] == 'b' else sharp_notes

if key not in notes:
    print("Invalid key entered.")
    exit()

start = notes.index(key)

if scale_type == 'major':
    steps = major_steps
    chords = major_chords
elif scale_type == 'minor':
    steps = minor_steps
    chords = minor_chords
elif scale_type == 'mohanam':
    steps = mohanam_steps
    chords = mohanam_chords
elif scale_type == 'hamsadhwani':
    steps = hamsadhwani_steps
    chords = hamsadhwani_chords
else:
    print("Invalid scale type.")
    exit()

# Build scale
scale = [notes[start]]
index = start
for step in steps:
    index = (index + step) % 12
    scale.append(notes[index])

if scale[0] == scale[-1]:
    scale.pop()

print("\nNotes in the scale:")
print(" → ".join(scale), "→ end")

print("\nDiatonic chords in the scale:")
for i, (note, chord) in enumerate(zip(scale, chords), 1):
    print(f"{i}. {note} {chord}")
