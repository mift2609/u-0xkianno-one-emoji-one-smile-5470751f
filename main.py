"""One Emoji, One Smile.

Writes exactly one emoji to /output/entry.txt — the warmest single
emoji we could think of, chosen to make a stranger smile.
"""

import os

EMOJI = "\U0001f60a"


def main():
    os.makedirs("/output", exist_ok=True)

    entry = EMOJI

    # The entry must be exactly one emoji: one grapheme, 1-8 characters.
    assert isinstance(entry, str) and 1 <= len(entry) <= 8, "entry length out of range"
    assert entry == EMOJI, "entry is not the chosen emoji"

    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)

    # Re-read and verify exactly what was written: one emoji, nothing else.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()

    assert written == entry, "written entry does not match"
    assert len(written) == 1, "entry must be exactly one character"
    assert written.isprintable(), "entry must be printable"

    print(written)


if __name__ == "__main__":
    main()
