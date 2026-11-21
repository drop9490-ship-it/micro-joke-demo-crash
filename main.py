#!/usr/bin/env python3
"""Write one short joke about AI coding agents to a text file.

The joke is a fixed literal: the program has no inputs, no clocks, no
network calls and no variation between runs, so every execution produces
exactly the same bytes. By default the file is /output/entry.txt; pass a
different path as the first command-line argument, or set ENTRY_OUTPUT.
"""

import os
import sys

# The entry: a single line about an agent whose own demo crashed.
# The dash before "then" is one em dash character (U+2014), written here
# as an escape so the source stays plain ASCII.
JOKE = (
    "Live on stage, our agent fixed its own crash in three seconds "
    "\u2014 then deleted the whole demo to prove the fix worked."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def resolve_output(argv):
    """Pick the output path: argv[1] wins, then ENTRY_OUTPUT, then default."""
    if len(argv) > 1 and argv[1]:
        return argv[1]
    env_path = os.environ.get("ENTRY_OUTPUT")
    if env_path:
        return env_path
    return DEFAULT_OUTPUT


def main(argv):
    out_path = resolve_output(argv)
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
