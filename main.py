"""Write one funny line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun "The One-Line Laugh": a single joke about an AI agent
that "organises" an inbox by deleting everything, then helpfully emails
a summary of what was lost — the punchline is the agent reporting its
own disaster as if it were a job well done.

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
