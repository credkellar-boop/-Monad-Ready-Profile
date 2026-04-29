import requests
import os
import sys

# MonadReady Scanner - GitHub Search Module
# Designed for high-frequency security auditing of the Monad ecosystem
GITHUB_API = "https://api.github.com/search/code"

def search_code(query, token=None):
    """
    Queries the GitHub API for code snippets matching the security pattern.
    """
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }
    if token:
        headers["Authorization"] = f"token {token}"
    
    # Params for targeted search within the scope
    params = {
        "q": query,
        "per_page": 10
    }
    
    try:
        response = requests.get(GITHUB_API, headers=headers, params=params)
        
        if response.status_code == 200:
            return response.json().get("items", [])
        elif response.status_code == 401:
            print("Error: Unauthorized. Verify your GITHUB_TOKEN.")
        elif response.status_code == 403:
            print("Error: Rate limit exceeded or access forbidden.")
        else:
            print(f"Error: GitHub API returned status {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")
        
    return []

def scan_results(items):
    """
    Processes raw API results into a scannable list of findings.
    """
    findings = []
    for item in items:
        findings.append(item.get("html_url", "URL missing"))
    return findings

def main():
    token = os.getenv("GITHUB_TOKEN")
    
    # --- AUTOMATION GATE ---
    # Detects if running in CI (GitHub Actions) to prevent input() hangs
    if os.getenv("GITHUB_ACTIONS") == "true":
        query = "Monad" # Default query for automated runs
    else:
        try:
            # Local interactive mode
            query = input("Enter search query (default 'Monad'): ")
            if not query:
                query = "Monad"
        except EOFError:
            query = "Monad"

    print(f"\n--- 🔍 Scanning GitHub for: {query} ---")
    
    results = search_code(query, token)
    findings = scan_results(results)
    
    if not findings:
        print("✅ No potential exposures detected.")
    else:
        print(f"🚨 Found {len(findings)} potential exposures:\n")
        for f in findings:
            print(f"- {f}")

if __name__ == "__main__":
    main()
