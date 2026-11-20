# Week 2: Encoding, Hashing, and File Integrity

Students learn that Base64 is not encryption, see the avalanche effect in SHA-256, "crack" one password by guessing,
then build a file integrity checker that finds a tampered `login.js` on a library website.
The AI twist is a fact-check table on four common security myths.

## Files

| File | Purpose |
| --- | --- |
| `lab.ipynb` | Student notebook with `TODO` cells |
| `data/website/` | Five small website files; `login.js` has been tampered with |
| `data/baseline_hashes.json` | SHA-256 of each file when the site was clean |

Regenerate data with `python tools/generate_week02_data.py weeks/week02-hashing-integrity/data`.

[Open the student lab in Colab](https://colab.research.google.com/github/Pantea1358/Cyber-labs-/blob/main/weeks/week02-hashing-integrity/lab.ipynb)

## Timing (2 hours)

| Part | Time | Topic |
| --- | --- | --- |
| Warm-up | 15 min | Story: a skimmer script added to a real store's checkout page |
| 1 to 3 | 40 min | Base64, SHA-256 avalanche, password check by hash |
| 4 to 6 | 30 min | Hash files, build the checker, investigate the change |
| 7 | 25 min | AI twist: fact-check the AI |
| 8 | 10 min | Exit ticket |
