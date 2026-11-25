"""Warning Label for Humans: One Line, Big Laugh — a printed label.

The program writes a single line to /output/entry.txt: the safety
warning label that should come printed on every human being,
funny first and plausible second.
"""

import os

MAX_CHARS = 160
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILENAME = "entry.txt"

# The joke is recognition: humans take everything personally.
# The label opens like a real printed warning — "WARNING: Handle
# with care." is the rhythm of a real label — and the sting lands
# in the last words — including this label. The label itself is
# the thing taken personally.
LINE = "WARNING: Handle with care. This human will take everything personally, including this label."


def build_line():
    """Return the entry line, checked: one line, under 160 characters."""
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, "entry must be 1-160 characters"
    return line


def ensure_output_dir(out_dir):
    os.makedirs(out_dir, exist_ok=True)


def write_entry(line, out_dir=OUTPUT_DIR):
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main():
    line = build_line()
    ensure_output_dir(OUTPUT_DIR)
    write_entry(line)


if __name__ == "__main__":
    main()
