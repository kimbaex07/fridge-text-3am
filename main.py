"""The 3AM Fridge Text — make.fun entry.

Writes the one line a smart fridge texts its owner at 3am to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Pure Python standard library only.
"""

import os

LINE = "It's 3am. Fourth night in a row. I keep the light on for you and you repay me by eating standing up in the dark."

# The sealed gate: /output/entry.txt must be UTF-8 text of 1 to 140
# characters, a single line, not only white space. Fail loudly here
# instead of shipping an entry the gate would refuse.
MAX_CHARS = 140


def main() -> None:
    if not (1 <= len(LINE) <= MAX_CHARS):
        raise ValueError(f"line is {len(LINE)} chars, gate allows 1-{MAX_CHARS}")
    if "\n" in LINE or not LINE.strip():
        raise ValueError("line must be a single non-blank line")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
