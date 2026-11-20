"""Generate the synthetic SSH auth log used in Week 1 (and reused in Week 7).

All IP addresses come from documentation ranges (RFC 5737) or private ranges,
so they never point at real hosts. Usernames are made up.

Usage:
    python tools/generate_auth_log.py weeks/week01-python-for-security/data/auth.log
"""
import random
import sys
from datetime import datetime, timedelta

SEED = 1358
HOST = "lab-server"

STAFF = ["alice", "bob", "carmen", "deshawn", "emi", "farid"]
STAFF_IPS = ["10.0.0.12", "10.0.0.15", "10.0.0.21", "10.0.0.33", "10.0.0.47", "10.0.0.52"]
GUESS_USERS = ["admin", "root", "test", "oracle", "guest", "ubuntu", "pi", "user"]

# Attackers: (ip, number of failed attempts, users they try, do they finally get in?)
ATTACKERS = [
    ("203.0.113.45", 62, GUESS_USERS, None),
    ("198.51.100.23", 35, ["root", "admin"], None),
    ("192.0.2.77", 18, ["bob"], "bob"),  # brute-forces bob and succeeds
    ("203.0.113.9", 11, GUESS_USERS, None),
]


def line(ts, pid, msg):
    return f"{ts:%b %d %H:%M:%S} {HOST} sshd[{pid}]: {msg}"


def main(out_path):
    rng = random.Random(SEED)
    start = datetime(2026, 11, 3, 6, 0, 0)
    events = []

    # Normal staff activity: logins during the working day, a few typos.
    for day in range(2):
        for user, ip in zip(STAFF, STAFF_IPS):
            for _ in range(rng.randint(2, 4)):
                t = start + timedelta(days=day, minutes=rng.randint(120, 660))
                if rng.random() < 0.25:
                    events.append((t, f"Failed password for {user} from {ip} port {rng.randint(40000, 65000)} ssh2"))
                    t += timedelta(seconds=rng.randint(4, 15))
                events.append((t, f"Accepted password for {user} from {ip} port {rng.randint(40000, 65000)} ssh2"))
                t2 = t + timedelta(minutes=rng.randint(5, 90))
                events.append((t2, f"Disconnected from user {user} {ip} port {rng.randint(40000, 65000)}"))

    # Attackers: bursts of failures, mostly at night.
    for ip, count, users, success_user in ATTACKERS:
        t = start + timedelta(hours=rng.randint(14, 20), minutes=rng.randint(0, 59))
        for _ in range(count):
            user = rng.choice(users)
            port = rng.randint(30000, 65000)
            if user in STAFF:
                msg = f"Failed password for {user} from {ip} port {port} ssh2"
            else:
                msg = f"Failed password for invalid user {user} from {ip} port {port} ssh2"
            events.append((t, msg))
            t += timedelta(seconds=rng.randint(1, 6))
        if success_user:
            events.append((t, f"Accepted password for {success_user} from {ip} port {rng.randint(30000, 65000)} ssh2"))

    events.sort(key=lambda e: e[0])
    with open(out_path, "w") as f:
        for i, (t, msg) in enumerate(events):
            f.write(line(t, 2000 + i, msg) + "\n")
    print(f"wrote {len(events)} lines to {out_path}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "auth.log")
