"""Tell a Whole Story in 32 Characters.

Writes a single Wi-Fi network name to entry.txt in the output
directory named by MAKEFUN_OUTPUT_DIR (default /output).

The name is a tiny deadpan story: a proposal, a breakup, and a
petty parting shot, all in one line a stranger can read at a glance.
"""

import os

ENTRY = "He proposed. She took the WiFi."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
