from backend.app.pytune_core import generate_scale

def main():
    import sys
    if len(sys.argv) >= 3:
        key = sys.argv[1]
        scale = sys.argv[2]
    else:
        key = input("Enter the key (e.g., C, D#, Bb): ").strip()
        scale = input("Enter the scale type (major or minor): ").strip().lower()
    res = generate_scale(key, scale)
    print(res['text'])

if __name__ == '__main__':
    main()
