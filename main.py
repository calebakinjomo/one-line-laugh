"""Write one funny line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Reads no environment variable except MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

LINE = (
    "I asked my AI agent to organise my inbox; it deleted everything "
    "and emailed me a summary of what I'd lost."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
