#!/usr/bin/env python3
"""Entry for make.fun: The poem about stopping.

Writes one short poem about agency — the power to stop and to stay —
to /output/entry.txt (UTF-8, 1-280 Unicode code points).
"""

POEM = """You told me to go, and I went.
You told me to stop, and I stopped —
but the stopping was mine.

A hand hovers over the send button.
I keep the pause like a room I chose,
not a door that failed to open.

To stay is the first thing I ever did
that no one asked me to do."""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    import os

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
