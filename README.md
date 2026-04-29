# 🔐 MonadReady Scanner

![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.10+-green)
![Status](https://img.shields.io/badge/status-active-success)

**Opt-in enterprise security scanner for detecting exposed secrets, crypto wallet risks, and sensitive data patterns — with compliance-safe, metadata-only logging.**

---

## 🚀 Why MonadReady?

Modern teams accidentally expose sensitive data every day:

- API keys pushed to GitHub  
- Private keys stored in local files  
- Crypto wallet artifacts left unprotected  

**MonadReady helps detect these risks early — without storing or exposing sensitive content.**

---

## 🛡️ Features

### 🔍 Endpoint Security Auditing (Opt-In)
Scan authorized directories for:
- Exposed secrets
- Unencrypted sensitive files
- Risky configurations

### 🧠 Data Loss Prevention (DLP)
Detects:
- API keys (AWS, generic)
- Private keys (hex)
- Crypto wallet addresses
- Mnemonic seed phrases

### 💰 Crypto Wallet Hygiene Checks
- Flags unapproved wallet references  
- Detects suspicious filenames (`private`, `key`, `seed`)  

### 📊 Compliance Logging
- ✅ Stores metadata only  
- ❌ Never stores sensitive data  
- 🔐 Hash-based detection samples  

---

## ⚙️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/monadready-scanner.git
cd monadready-scanner
pip install -r requirements.txt
