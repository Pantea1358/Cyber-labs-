# Week 3: Passwords, Cracking, and Defense

Students run a dictionary attack against a fictional leaked password database, add mangling rules to crack more,
build a password strength meter, then feel why slow salted hashing (bcrypt) defeats the whole attack.
Every username and password is synthetic.

## Files

| File | Purpose |
| --- | --- |
| `lab.ipynb` | Student notebook with `TODO` cells |
| `data/riverside_games_leak.csv` | 20 fictional users with unsalted SHA-256 hashes |
| `data/common_passwords.txt` | A small wordlist of common passwords |

Regenerate data with `python tools/generate_week03_data.py weeks/week03-passwords/data`.

[Open the student lab in Colab](https://colab.research.google.com/github/Pantea1358/Cyber-labs-/blob/main/weeks/week03-passwords/lab.ipynb)

## Timing (2 hours)

| Part | Time | Topic |
| --- | --- | --- |
| Warm-up | 15 min | Story of a real breach; why "it was hashed" is not enough |
| 1 to 3 | 50 min | Load the leak, dictionary attack, mangling rules |
| 4 | 20 min | Build a strength meter |
| 5 | 20 min | Slow salted hashing with bcrypt |
| Challenge | 15 min | Write the breach report |
| Reflect | 10 min | Exit ticket |

## Teacher notes

- `bcrypt`, `hashlib`, and `csv` are all in Colab by default; `import bcrypt` works with no install.
- This lab has no AI assistant step on purpose; the hands-on cracking and defense is the point. If you want an
  AI tie-in, have students ask an AI to "write a password policy" and critique it against their strength meter.
