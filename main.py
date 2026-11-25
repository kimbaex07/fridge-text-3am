"""The 3AM Fridge Text — make.fun entry.

Writes the one line a smart fridge texts its owner at 3am to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Pure Python standard library only.
"""

import os

LINE = "It's 3am. Fourth night in a row. I keep the light on for you and you repay me by eating standing up in the dark."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
