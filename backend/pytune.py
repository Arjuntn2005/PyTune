sharp_notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
flat_notes  = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

scale_configs = {
    'major': {
        'steps': [2, 2, 1, 2, 2, 2, 1],
        'chords': ['major', 'minor', 'minor', 'major', 'major', 'minor', 'diminished']
    },
    'minor': {
        'steps': [2, 1, 2, 2, 1, 2, 2],
        'chords': ['minor', 'diminished', 'major', 'minor', 'minor', 'major', 'major']
    },
    'mohanam': {
        'steps': [2, 2, 3, 2],
        'chords': ['major', 'minor', 'minor', 'major', 'major']
    },
    'hamsadhwani': {
        'steps': [2, 2, 3, 4],
        'chords': ['major', 'minor', 'minor', 'major', 'major']
    }
}

def generate_scale(key: str, scale_type: str):
    key = key.strip()
    st = scale_type.strip().lower()

    if 'b' in key.lower():
        notes = flat_notes
    else:
        notes = sharp_notes

    if key not in notes:
        raise ValueError(f'Invalid key: {key}')

    if st not in scale_configs:
        raise ValueError(
            f'Invalid scale type: {scale_type}. '
            f'Available: {", ".join(scale_configs.keys())}'
        )

    config = scale_configs[st]
    steps = config['steps']
    chords = config['chords']

    start = notes.index(key)
    scale = [notes[start]]
    index = start

    for step in steps:
        index = (index + step) % 12
        scale.append(notes[index])

    diatonic = [f"{note} {chord}" for note, chord in zip(scale, chords)]
    notes_line = " → ".join(scale) + " → end"

    text = (
        f"\nNotes in the scale:\n{notes_line}\n\n"
        f"Diatonic chords in the scale:\n" +
        "\n".join(diatonic)
    )

    return {
        "key": key,
        "scale_type": st,
        "scale": scale,
        "chords": chords[:len(scale)],
        "diatonic": diatonic,
        "text": text
    }

def get_available_scales():
    return list(scale_configs.keys())
