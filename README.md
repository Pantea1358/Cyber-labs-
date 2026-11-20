# Cyber Labs: AI + Python for Cybersecurity

A 14-week, hands-on lab course for cybersecurity students with basic Python and basic AI knowledge.
Students write Python to defend systems and use AI both as a helper and as something to test and attack.

Every lab runs in **Google Colab** (free, browser only) and uses **synthetic data** we provide.
Nothing in this course touches real accounts, real networks, or other people's systems.

## Start here

1. Read [SETUP.md](SETUP.md) to open a lab in Colab.
2. Sign the [lab ethics agreement](ETHICS_AGREEMENT.md) before Week 1.
3. See the full [syllabus](SYLLABUS.md) for all 14 weeks.

## Weekly labs

| Week | Lab | Status |
| --- | --- | --- |
| 1 | [Python for security and lab ethics](weeks/week01-python-for-security/) | Ready |
| 2 | [Encoding, hashing, and file integrity](weeks/week02-hashing-integrity/) | Ready |
| 3 | [Passwords, cracking, and defense](weeks/week03-passwords/) | Ready |
| 4 | [Cryptography, hands-on](weeks/week04-cryptography/) | Ready |
| 5 | Intro to ML for security | Planned |
| 6 | Phishing detection with ML | Planned |
| 7 | Log analysis and anomaly detection | Planned |
| 8 | Midterm mini-CTF | Planned |
| 9 | Network traffic analysis | Planned |
| 10 | Web vulnerabilities | Planned |
| 11 | Secure code review with AI | Planned |
| 12 | LLM security: prompt injection | Planned |
| 13 | Attacking AI models | Planned |
| 14 | Capstone: blue team challenge | Planned |

## What is in each week's folder

- `lab.ipynb`: the student notebook, with `TODO` cells to fill in.
- `data/`: synthetic files the lab uses.
- `README.md`: teacher notes, timing, and the exit ticket.

## For teachers

Each lab follows the same 2-hour shape: warm-up (15 min), guided build (60 min), AI twist (30 min), reflect (15 min).
Data files can be regenerated with the scripts in [`tools/`](tools/).

Answer notebooks and answer keys are kept out of this public repo so students cannot see them.
The instructor has them separately.
