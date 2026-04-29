#!/usr/bin/env python3

"""
MonadReady Scanner 🔐
Enterprise Security & DLP Tool (Opt-In)

- Endpoint auditing (authorized directories only)
- DLP detection (API keys, private keys, seed phrases)
- Crypto wallet hygiene checks
- Compliance-safe logging (NO sensitive data stored)

Author: Darion Kellar
License: MIT
"""

import os
import re
import json
import hashlib
import datetime
from pathlib import Path

# ----------------------------
# CONFIG
# ----------------------------

MAX_FILE_SIZE_MB = 5
LOG_FILE = "scan_report.json"

APPROVED_WALLETS = ["ledger", "trezor", "coinbase", "metamask"]

EXCLUDED_DIRS = {"/System", "/Library", "/usr", "/bin", "/dev", "/proc"}

# ----------------------------
# PATTERNS (DLP)
# ----------------------------

PATTERNS = {
    "bitcoin_address": r"\b(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}\b",
    "ethereum_address": r"\b0x[a-fA-F0-9]{40}\b",
    "private_key_hex": r"\b[a-fA-F0-9]{64}\b",
    "aws_api_key": r"\bAKIA[0-9A-Z]{16}\b",
    "generic_api_key": r"(api[_-]?key|secret)[\"'\s:=]+[A-Za-z0-9_\-]{16,}",
    "mnemonic_seed": r"\b(?:abandon|ability|able|about|above|absent)\b(?:\s+\w+){11,23}"
}

# ----------------------------
# HELPERS
# ----------------------------

def is_excluded(path):
    return any(str(path).startswith(ex) for ex in EXCLUDED_DIRS)


def file_too_large(filepath):
    size_mb = os.path.getsize(filepath) / (1024 * 1024)
    return size_mb > MAX_FILE_SIZE_MB


def hash_match(match):
    """Hash sensitive match so we never store raw data"""
    return hashlib.sha256(match.encode()).hexdigest()[:12]


# ----------------------------
# SCANNING
# ----------------------------

def scan_file(filepath):
    findings = []

    if file_too_large(filepath):
        return findings

    try:
        with open(filepath, "r", errors="ignore") as f:
            content = f.read()

        for label, pattern in PATTERNS.items():
            matches = re.findall(pattern, content)

            if matches:
                findings.append({
                    "type": label,
                    "count": len(matches),
                    "sample_hash": hash_match(matches[0])
                })

    except Exception:
        pass

    return findings


def wallet_hygiene(filepath):
    issues = []
    lower = filepath.lower()

    if "wallet" in lower:
        if not any(w in lower for w in APPROVED_WALLETS):
            issues.append({
                "type": "unapproved_wallet_reference",
                "count": 1
            })

    if any(k in lower for k in ["private", "key", "seed"]):
        issues.append({
            "type": "suspicious_filename",
            "count": 1
        })

    return issues


def scan_directory(directory):
    report = []

    for root, dirs, files in os.walk(directory):

        if is_excluded(root):
            continue

        for name in files:
            path = os.path.join(root, name)

            file_findings = scan_file(path)
            hygiene_findings = wallet_hygiene(path)

            all_findings = file_findings + hygiene_findings

            if all_findings:
                report.append({
                    "file": path,
                    "issues": all_findings
                })

    return report


# ----------------------------
# LOGGING
# ----------------------------

def save_report(report):
    output = {
        "scan_time": datetime.datetime.utcnow().isoformat(),
        "files_flagged": len(report),
        "findings": report
    }

    with open(LOG_FILE, "w") as f:
        json.dump(output, f, indent=4)

    print(f"\n[✔] Report saved: {LOG_FILE}")


# ----------------------------
# MAIN
# ----------------------------

def main():
    print("=== MonadReady Security Scanner ===")
    print("⚠️ Authorized use only.\n")

    consent = input("Do you have permission to scan this system? (yes/no): ").lower()
    if consent != "yes":
        print("Consent required. Exiting.")
        return

    target = input("Enter directory to scan: ").strip()

    if not os.path.exists(target):
        print("Invalid path.")
        return

    print("\n[+] Scanning...\n")

    report = scan_directory(target)

    save_report(report)

    print(f"[✔] Scan complete. {len(report)} files flagged.")


if __name__ == "__main__":
    main()
