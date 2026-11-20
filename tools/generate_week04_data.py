"""Generate Week 4 data: a Caesar-encrypted "intercepted message" students must break.

The plaintext is a harmless fictional note. The lab is about frequency analysis, not secrets.

Usage:
    python tools/generate_week04_data.py weeks/week04-cryptography/data
"""
import os
import sys

PLAINTEXT = (
    "The meeting is moved to noon on friday. Bring the quarterly report and the "
    "updated budget. We will talk about the new library wing and the summer reading "
    "program. Do not forget to reserve the main hall for the whole afternoon."
)
SHIFT = 7


def caesar(text, shift):
    out = []
    for ch in text:
        if ch.isupper():
            out.append(chr((ord(ch) - 65 + shift) % 26 + 65))
        elif ch.islower():
            out.append(chr((ord(ch) - 97 + shift) % 26 + 97))
        else:
            out.append(ch)
    return "".join(out)


def main(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "intercepted.txt"), "w") as f:
        f.write(caesar(PLAINTEXT, SHIFT) + "\n")
    print(f"wrote intercepted.txt (Caesar shift {SHIFT}) to {out_dir}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "data")
