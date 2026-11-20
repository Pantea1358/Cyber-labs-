"""Generate Week 3 data: a small common-password wordlist and a fake leaked user table.

Every username and password is invented for this lab. The "leak" is from a fictional
company, Riverside Games, and contains unsalted SHA-256 hashes (a bad practice on purpose).

Usage:
    python tools/generate_week03_data.py weeks/week03-passwords/data
"""
import csv
import hashlib
import os
import sys

BASE = ["password", "qwerty", "letmein", "dragon", "monkey", "football", "baseball", "soccer", "hockey",
        "sunshine", "princess", "shadow", "master", "superman", "batman", "pokemon", "minecraft", "fortnite",
        "starwars", "iloveyou", "welcome", "admin", "login", "hello", "freedom", "whatever", "trustno1",
        "summer", "winter", "spring", "autumn", "tiger", "lion", "eagle", "panther", "cookie", "chocolate",
        "pizza", "banana", "orange", "purple", "silver", "golden", "angel", "ninja", "gamer", "riverside",
        "abc", "abcdef", "123456", "12345678", "111111", "000000", "654321", "michael", "jessica", "ashley",
        "daniel", "jordan", "taylor", "matthew", "andrew", "charlie", "maggie", "buster", "ginger", "pepper"]
SUFFIXES = ["", "1", "12", "123", "1234", "!", "01", "99", "2024", "2025", "2026"]

# username -> password. Some are in the wordlist, some need "rules", some are strong.
USERS = {
    "jlee": "dragon123",           # wordlist
    "mgarcia": "sunshine",         # wordlist
    "tnguyen": "123456",           # wordlist
    "kpatel": "minecraft2025",     # wordlist
    "rsmith": "letmein!",          # wordlist
    "abrown": "football1",         # wordlist
    "cwilson": "pokemon99",        # wordlist
    "dkim": "qwerty",              # wordlist
    "eochoa": "iloveyou",          # wordlist
    "fjohnson": "Summer2026!",     # rules: Capitalize + year + !
    "gmartin": "Tiger2025!",       # rules
    "hdavis": "P@ssw0rd",          # rules: leetspeak
    "imoore": "Batman123",         # rules: Capitalize
    "jtaylor": "Riverside2026",    # rules: Capitalize + year
    "kwhite": "n1nja",             # rules: leetspeak
    "lharris": "correct-horse-violin-sunset",  # strong passphrase
    "mclark": "Gx7#qL9!vR2@pZ",    # strong random
    "nlewis": "my dog eats tacos on tuesday",  # strong passphrase
    "owalker": "tH8$kq2Pn!",       # strong random
    "phall": "blue-kettle-mountain-42",        # strong passphrase
}


def sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()


def main(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    words = [b + s for b in BASE for s in SUFFIXES]
    with open(os.path.join(out_dir, "common_passwords.txt"), "w") as f:
        f.write("\n".join(words) + "\n")
    with open(os.path.join(out_dir, "riverside_games_leak.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["username", "sha256"])
        for user, pw in USERS.items():
            w.writerow([user, sha256(pw)])
    print(f"wrote {len(words)} wordlist entries and {len(USERS)} leaked users to {out_dir}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "data")
