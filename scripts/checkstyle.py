# scripts/check_style_py.py
import subprocess
import sys

# Lint these paths; adjust as you add code
TARGETS = ["src", "tests"]

def main() -> int:
    print("▶ Running ruff (Python style/lint)…")
    # "ruff check" returns non-zero if there are violations
    result = subprocess.run(["ruff", "check", *TARGETS], text=True)
    if result.returncode != 0:
        print("\n❌ Python style check failed (ruff).")
        return result.returncode
    print("\n✅ Python style check passed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
