"""news-image-20261125 entrypoint: copy the bundled entry.png to the output dir.

Stdlib only. The grader runs this with no network; it must write the same
bytes on every run.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Verify the copy is complete: same byte size as the bundled image.
    if os.path.getsize(dst) != os.path.getsize(src):
        raise SystemExit("entry.png copy incomplete: size mismatch")


if __name__ == "__main__":
    main()
