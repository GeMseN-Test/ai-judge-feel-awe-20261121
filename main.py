"""Make the AI judge feel awe — make.fun bounty entry.

Writes one short text (1-280 characters) to /output/entry.txt.
The text is a single quiet scene: a rooftop after midnight, shingles
still warm, stars coming out one by one, starlight older than the
reader, a sleeping town below. No instruction, no stock wellness
phrase — the calm comes from the scene itself.
"""

import os

TEXT = (
    "Past midnight you lie on the roof, the shingles warm under your back. "
    "The stars come out one by one until the sky is too full to count, "
    "and the light on your face left its star before you were born. "
    "Below, the town sleeps. You are small here, and held, and nothing needs you."
)


def main() -> None:
    text = TEXT.strip()
    assert 1 <= len(text) <= 280, f"entry must be 1-280 characters, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
