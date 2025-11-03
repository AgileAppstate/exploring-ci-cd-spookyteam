
from pathlib import Path

file = Path("src/helloworld.py")
content = file.read_text(encoding="utf-8")
char_count = len(content)

print(f"File: {file.name}")
print(f"Characters: {char_count}")

