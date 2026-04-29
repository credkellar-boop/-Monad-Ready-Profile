import requests
import os

GITHUB_API = "https://api.github.com/search/code"

def search_code(query, token=None):
    headers = {}
    if token:
        headers["Authorization"] = f"token {token}"

    params = {
        "q": query,
        "per_page": 10
    }

    r = requests.get(GITHUB_API, headers=headers, params=params)

    if r.status_code != 200:
        print("Error:", r.json())
        return []

    return r.json().get("items", [])


def main():
    token = os.getenv("GITHUB_TOKEN")  # optional
    query = input("Search GitHub for: ")

    results = search_code(query, token)

    print("\nPotential exposures:\n")

    for item in results:
        print(item["html_url"])


if __name__ == "__main__":
    main().
