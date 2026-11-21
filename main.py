#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

The poem is about the power to ask and to be given: a person hands the
weight of a day to a machine that acts for them, and discovers that the
permission has quietly changed hands.
"""

import os

POEM = (
    "I asked the machine to carry my day,\n"
    "and it did — arms full, no questions asked.\n"
    "Now I stand at my own front door,\n"
    "key in my pocket, and wonder\n"
    "which of us still has to knock.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
