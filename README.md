![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.10+-green)
![Status](https://img.shields.io/badge/status-active-success)
# SentinelScan 🔐
Enterprise Security & DLP Scanner (Opt-In)

SentinelScan is a lightweight, compliance-focused security auditing tool designed to help organizations detect potential exposure of sensitive data such as private keys, API tokens, and crypto wallet artifacts—without collecting or storing the sensitive data itself.

---

## 🚀 Features

- 🔍 **Endpoint Security Auditing (Opt-In)**
  - Scans authorized directories for potential sensitive data exposure

- 🛡️ **Data Loss Prevention (DLP)**
  - Detects patterns like:
    - API keys
    - Private keys
    - Crypto wallet addresses
    - Mnemonic seed phrases

- 💰 **Crypto Wallet Hygiene Checks**
  - Flags:
    - Unapproved wallet references
    - Suspicious filenames (e.g., containing "key", "private")

- 📊 **Compliance Logging**
  - Stores **metadata only**:
    - File path
    - Risk type
    - Match count
  - ❌ Never stores raw sensitive data

---

## ⚠️ Important Notice

This tool is intended for:
- Authorized corporate environments
- Security auditing with **explicit user/admin consent**

**Do NOT use this tool on systems you do not own or have permission to scan.**

---

## 🧰 Installation

```bash
git clone https://github.com/yourusername/sentinelscan.git
cd sentinelscan
python3 enterprise_security_scanner.py
Opt-in enterprise security scanner for detecting exposed secrets, crypto wallet risks, and sensitive data patterns with compliance-safe, metadata-only logging.
