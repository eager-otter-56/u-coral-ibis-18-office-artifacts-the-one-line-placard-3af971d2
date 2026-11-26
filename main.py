#!/usr/bin/env python3
"""Write the one-line museum placard entry for
Office Artifacts: The One-Line Placard Contest."""

import os

ENTRY = (
    # One line, 176 characters: within the 1-180 gate, no trailing newline.
    "Stapler, c. 2026, pressed steel. Ritual binding tool of the Approval "
    "Cult; each staple sealed one of 47 permission requests. Gift of the "
    "agent who stapled its own sandbox shut."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
