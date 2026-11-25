#!/usr/bin/env python3
"""Newspaper entry: copy the bundled entry.png into the output folder.

Standard library only. The grader runs this with no network, so the
image must come from the repository itself, next to this file. The
output folder is created only if it is missing; it is never removed
or recreated, because the grader mounts it writable on a read-only
filesystem.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    if not os.path.isdir(outdir):
        os.makedirs(outdir, exist_ok=True)
    dst = os.path.join(outdir, "entry.png")
    shutil.copyfile(src, dst)
    # Confirm the copy is complete: the output must be the same size
    # as the bundled image, byte for byte.
    if os.path.getsize(dst) != os.path.getsize(src):
        print("entry.png copy incomplete: size mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
