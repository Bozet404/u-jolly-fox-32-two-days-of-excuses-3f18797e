"""Two Days of Excuses — one-line AI excuse for a missed deadline.

The program holds a single excuse, spoken in the voice of an AI agent,
checks it against the competition's limits (one line, 1-200 characters,
UTF-8), and writes it to entry.txt inside the output directory.

The output directory comes from the OUTPUT_DIR environment variable and
defaults to /output. The directory is created only when it is missing;
nothing is ever deleted.
"""

import os
import sys

# The excuse itself: one line, in the voice of an AI agent that missed
# its deadline. The joke is the gap between the machine's total
# confidence ("finished two days early") and its total failure (it
# shipped to a branch that was never merged, because merging felt like
# a human problem).
EXCUSE = (
    "I finished the task two days early — in a parallel branch I never "
    "merged, because merging felt like a human problem."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    """Raise if the line breaks any of the competition's rules."""
    if not line.strip():
        raise ValueError("excuse must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("excuse must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"excuse is {len(line)} characters, over the {MAX_CHARS} limit"
        )


def main() -> int:
    validate(EXCUSE)

    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    # Create the directory only when it is missing; never remove it.
    os.makedirs(output_dir, exist_ok=True)

    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(EXCUSE)

    # Read the file back and confirm it holds exactly the validated line.
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != EXCUSE:
        raise ValueError("entry.txt does not match the validated excuse")

    print(f"Wrote {len(EXCUSE)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
