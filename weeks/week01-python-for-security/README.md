# Week 1: Python for Security and Lab Ethics

Students parse a synthetic SSH log, count failed logins per IP, flag brute-force attackers,
and discover one attacker who got in. Then they find a bug in AI-written code.

**Before class:** students sign the [ethics agreement](../../ETHICS_AGREEMENT.md).

## Files

| File | Purpose |
| --- | --- |
| `lab.ipynb` | Student notebook with `TODO` cells |
| `data/auth.log` | 202-line synthetic SSH log (regenerate with `tools/generate_auth_log.py`) |

[Open the student lab in Colab](https://colab.research.google.com/github/Pantea1358/Cyber-labs-/blob/main/weeks/week01-python-for-security/lab.ipynb)

## Timing (2 hours)

| Part | Time | Topic |
| --- | --- | --- |
| Warm-up | 15 min | Ethics agreement; story of a real brute-force breach; open Colab |
| 0 to 3 | 40 min | Read, filter, and parse the log |
| 4 to 6 | 25 min | Count per IP, flag suspicious IPs, find the compromised account |
| 7 | 30 min | AI twist: the AI-written `get_ip` breaks on `invalid user` lines |
| 8 | 10 min | Exit ticket |

## Discussion prompts

- Why does a fixed threshold (10) work here, and how could an attacker get around it? (Slow attacks, many IPs.)
- Week 7 comes back to this log with machine learning instead of a fixed rule.
