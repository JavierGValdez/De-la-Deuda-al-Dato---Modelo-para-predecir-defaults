import re
from pathlib import Path

root = Path(__file__).parent
files = [
    root / "credit_defaults.csv",
    root / "entregable2.ipynb",
]

# ...existing code...
PATTERNS = {
    "ghp_": re.compile(r"(ghp_)[A-Za-z0-9]{36}"),
    "github_pat_": re.compile(r"(github_pat_)[A-Za-z0-9_]{82,}"),
    "sk-": re.compile(r"(sk-)[A-Za-z0-9]{20,}"),
    "AKIA": re.compile(r"(AKIA)[0-9A-Z]{16}"),
    "AIza": re.compile(r"(AIza)[0-9A-Za-z\-_]{35}"),
    "PKHDR": re.compile(r"-----BEGIN (?:RSA|EC|DSA|OPENSSH|PRIVATE) KEY-----"),
    "SSH": re.compile(r"ssh-rsa\s+[A-Za-z0-9+/=]{100,}"),
    # Tencent Cloud SecretId
    "TENCENT_AKID": re.compile(r"(AKID)[0-9A-Za-z]{32}")
}
# ...existing code...

def redact_text(s: str) -> str:
    for name, rx in PATTERNS.items():
        if name in ("PKHDR","SSH"):
            s = rx.sub("[REDACTED-KEY]", s)
        else:
            s = rx.sub(lambda m: (m.group(1) + "REDACTED"), s)
    return s

for p in files:
    try:
        original = p.read_text(encoding="utf-8", errors="ignore")
        redacted = redact_text(original)
        if redacted != original:
            p.write_text(redacted, encoding="utf-8")
            print(f"[REDACTED] {p.name}")
    except FileNotFoundError:
        pass
print("Done.")
