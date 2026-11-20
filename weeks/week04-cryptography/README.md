# Week 4: Cryptography, Hands-On

Students break a Caesar-encrypted message by brute force and then by frequency analysis, see why AES (Fernet)
resists both, encrypt and decrypt their own messages, critique insecure AI-written crypto code, and build a small
secure note tool. All data is fictional.

## Files

| File | Purpose |
| --- | --- |
| `lab.ipynb` | Student notebook with `TODO` cells |
| `data/intercepted.txt` | A Caesar-encrypted message (shift 7) to break |

Regenerate data with `python tools/generate_week04_data.py weeks/week04-cryptography/data`.

[Open the student lab in Colab](https://colab.research.google.com/github/Pantea1358/Cyber-labs-/blob/main/weeks/week04-cryptography/lab.ipynb)

## Timing (2 hours)

| Part | Time | Topic |
| --- | --- | --- |
| Warm-up | 10 min | Why people still reach for "hide it" ciphers |
| 1 to 3 | 55 min | Caesar cipher, brute force, frequency analysis |
| 4 | 20 min | AES/Fernet: encrypt, decrypt, avalanche |
| 5 | 25 min | AI twist: find the bugs in AI-written crypto |
| Challenge | 15 min | Build a secure note tool |
| Reflect | 10 min | Exit ticket |

## Teacher notes

- `cryptography` (Fernet) is preinstalled in Colab; `from cryptography.fernet import Fernet` works with no install.
- The frequency guess assumes the top letter is `e`. On a short message it can miss by a letter or two; that is a
  teaching moment, not a bug. The brute-force list in Part 2 is the safety net.
