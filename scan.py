
import re
import sys
from pathlib import Path

PATTERNS = {
    "GitHub Token": r"ghp_[A-Za-z0-9]{20,}",
    "GitHub PAT": r"github_pat_[A-Za-z0-9_]{20,}",
    "OpenAI Key": r"sk-[A-Za-z0-9]{20,}",
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
}

def scan_file(filepath):
    path = Path(filepath)

    if not path.exists():
        print(f"[ERROR] File not found: {filepath}")
        return

    content = path.read_text(errors="ignore").splitlines()

    found = False

    for line_num, line in enumerate(content, start=1):
        for name, pattern in PATTERNS.items():
            matches = re.findall(pattern, line)

            if matches:
                found = True

                for match in matches:
                    print("=" * 50)
                    print(f"[FOUND] {name}")
                    print(f"Line {line_num}")
                    print(match)

    if not found:
        print("No secrets detected.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("python scan.py <file>")
        sys.exit(1)

    scan_file(sys.argv[1])
  
