import re

PATTERNS = {
    "aws_key": r"AKIA[0-9A-Z]{16}",
    "eth": r"0x[a-fA-F0-9]{40}"
}

def scan_text(text):
    results = []
    for name, pattern in PATTERNS.items():
        matches = re.findall(pattern, text)
        if matches:
            results.append({"type": name, "count": len(matches)})
    return results
