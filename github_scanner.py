import os
import sys

# ... (Keep your imports and logic)

def main():
    print("=== MonadReady Security Scanner ===")
    print("⚠️ Authorized use only.\n")
    
    # NEW: Automatically bypass for GitHub Actions to avoid EOFError
    if os.getenv("GITHUB_ACTIONS") == "true":
        consent = "yes"
    else:
        consent = input("Do you have permission to scan this system? (yes/no): ").lower()
    
    if consent != "yes":
        print("Consent required. Exiting.")
        sys.exit(1)

    # ... (Rest of your scan logic)

if __name__ == "__main__":
    main()
