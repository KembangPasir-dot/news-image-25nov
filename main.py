#!/usr/bin/env python3
"""THE WORLD IN ONE DAY - Wednesday 25 November 2026.

Rebuild (resubmit) of the make.fun news-image-20261125 entry.
Revision 2: fact-checked, hero changed to the day's global story
(the U.S. tariff salvo on 14 trading partners), every number
re-verified against the original wires.
A clean, readability-first newspaper front page: one dominant hero
four big key numbers, eleven compact numbered secondary stories grouped
by region, a market bar chart under the hero as supporting evidence,
and an enlarged dotted world map with numbered pins matching the
stories. Clean vector graphics only - no generated scene illustrations.

This program copies the rendered front page (entry.png, in the same
directory as this script) to the output directory as entry.png.
Python 3.13, standard library only. No network access. Deterministic:
every run writes byte-identical output, and the copy is verified
(size and SHA-256) before the program reports success.
"""

import hashlib
import os
import sys

ENTRY = "entry.png"


def _sha256(data):
    return hashlib.sha256(data).hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, ENTRY)

    with open(src, "rb") as fh:
        data = fh.read()
    if not data:
        print("error: %s is empty" % src, file=sys.stderr)
        return 1
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        print("error: %s is not a PNG file" % src, file=sys.stderr)
        return 1
    src_hash = _sha256(data)

    with open(dst, "wb") as fh:
        fh.write(data)

    with open(dst, "rb") as fh:
        copied = fh.read()
    if len(copied) != len(data):
        print(
            "error: copied %d bytes, expected %d" % (len(copied), len(data)),
            file=sys.stderr,
        )
        return 1
    if _sha256(copied) != src_hash:
        print("error: copied file hash mismatch", file=sys.stderr)
        return 1

    print("wrote %s (%d bytes)" % (dst, len(data)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
