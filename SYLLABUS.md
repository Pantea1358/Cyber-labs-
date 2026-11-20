# Syllabus: AI + Python for Cybersecurity (14 weeks)

**Audience:** cybersecurity students with basic Python and basic AI knowledge.
**Format:** one 2-hour lab per week in Google Colab, free tools only, synthetic data only.

## Course goals

By the end of the course students can:

- Write Python scripts that parse logs, hash files, and analyze traffic.
- Build and evaluate simple machine learning models that detect phishing, malicious URLs, and anomalies.
- Find and fix common web and code vulnerabilities, with and without AI help.
- Explain and test the main security risks of AI systems, including prompt injection and adversarial inputs.
- Judge when an AI answer is trustworthy and verify it.
- Act ethically and legally when using security skills.

## Lab shape (every week)

| Part | Time | What happens |
| --- | --- | --- |
| Warm-up | 15 min | A real-world story or short demo |
| Guided build | 60 min | Students code the core tool step by step |
| AI twist | 30 min | Use, test, or attack an AI model on the same task |
| Reflect | 15 min | Ethics question, exit ticket, short write-up |

## Weekly plan

| Week | Lab | Students build | AI angle | Tools |
| --- | --- | --- | --- | --- |
| 1 | Python for security, lab ethics | A script that reads a log file and counts failed logins | Ask an AI assistant to explain code, then check if it is right | Colab, Python basics |
| 2 | Encoding, hashing, file integrity | A file integrity checker with SHA-256 | Ask AI "is Base64 encryption?" and fact-check it | `hashlib`, `base64` |
| 3 | Passwords and cracking | A dictionary attack on provided weak hashes, plus a strength checker | Compare AI-suggested passwords to human ones | `hashlib`, `bcrypt` |
| 4 | Cryptography basics | A Caesar cipher breaker, then AES encryption | Spot insecure choices in AI-written crypto code | `cryptography` |
| 5 | Intro to ML for security | A malicious URL classifier | Accuracy vs false positives | scikit-learn, pandas |
| 6 | Phishing detection with ML | A phishing email classifier | Does AI-written phishing fool the model? | scikit-learn |
| 7 | Log analysis and anomaly detection | A login anomaly detector | Verify an LLM incident summary | pandas, Isolation Forest |
| 8 | Midterm mini-CTF | 10 flag challenges from weeks 1 to 7 | AI allowed, answers must be cited | CTFd |
| 9 | Network traffic analysis | A pcap reader that spots a port scan | Flow classifier | Scapy (provided .pcap only) |
| 10 | Web vulnerabilities | Exploit and fix SQLi and XSS in a practice app | AI explains each bug | Flask practice app |
| 11 | Secure code review with AI | Patches for a buggy app | Student vs AI vs scanner | Bandit, AI assistant |
| 12 | LLM security: prompt injection | Attack, then defend, a chatbot hiding a secret | Red-team and add guardrails | Free LLM API or local model |
| 13 | Attacking AI models | Adversarial inputs and data poisoning on the week 5 model | Measure how easily models are fooled | scikit-learn, Pillow |
| 14 | Capstone: blue team challenge | Team incident report on a staged breach | AI as analyst helper, every claim verified | All prior tools |

## Grading (suggested)

| Item | Weight |
| --- | --- |
| Weekly lab notebooks (12 labs) | 40% |
| Weekly exit tickets and reflections | 10% |
| Midterm mini-CTF (week 8) | 20% |
| Capstone report and presentation (week 14) | 30% |

## Rules

- Sign the [ethics agreement](ETHICS_AGREEMENT.md) before Week 1.
- Attack only what the lab provides.
- Cite AI help in a code comment or write-up.
