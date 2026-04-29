import requests
import re

GITHUB_API = "https://api.github.com/search/code"

PATTERN = r"AKIA[0-9A-Z]{16}"  # AWS key example

def search_github(query, token=None):
    headers = {}
    if token:
        headers["Authorization"] = f"token {token}"

    params = {"q": query}

    response = requests.get(GITHUB_API, headers=headers, params=params)
    return response.json()

def scan_results(results):
    findings = []

    for item in results.get("items", []):
        url = item["html_url"]
        findings.append(url)

    return findings


if __name__ == "__main__":
    query = "AKIA"
    results = search_github(query)

    findings = scan_results(results)

    print("Potential exposed keys found in:")
    for f in findings:
        print(f)
