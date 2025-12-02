sharp_notes = ['C', 'C#', 'D', 'D#', 'E', 'F',
               'F#', 'G', 'G#', 'A', 'A#', 'B']

flat_notes = ['C', 'Db', 'D', 'Eb', 'E', 'F',
              'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

major_steps = [2, 2, 1, 2, 2, 2, 1]
minor_steps = [2, 1, 2, 2, 1, 2, 2]

major_chords = ['major', 'minor', 'minor', 'major', 'major', 'minor', 'diminished']
minor_chords = ['minor', 'diminished', 'major', 'minor', 'minor', 'major', 'major']

key = input("Enter the key (e.g., C, D#, Bb): ").strip()
scale_type = input("Enter the scale type (major or minor): ").strip().lower()

if 'b' in key:
    notes = flat_notes
else:
    notes = sharp_notes

start = notes.index(key)

if scale_type == 'major':
    steps = major_steps
    chords = major_chords
elif scale_type == 'minor':
    steps = minor_steps
    chords = minor_chords
else:
    print("Invalid scale type")
    exit()

scale = [notes[start]]
index = start
for step in steps:
    index = (index + step) % 12
    scale.append(notes[index])

scale = scale[:-1]

print("\nNotes in the scale:")
for note in scale:
    print(note, end=' → ')
print("end")

print("\nDiatonic chords in the scale:")
for i in range(7):
    print(f"{scale[i]} {chords[i]}")
