#!/usr/bin/env python3
"""Rooftop starlight — a single calming text for the AI judge.

This entry for the make.fun "Make the AI judge feel awe" bounty writes
one short text to /output/entry.txt. The text is one still moment: lying
on a rooftop past midnight, shingles warm from the day, stars arriving
one by one, and a town asleep below. Nothing in it tells the reader to
relax; the stillness does the work on its own.

The program uses only the Python 3.13 standard library, makes no
network calls, and always produces the same file.
"""

from pathlib import Path

ENTRY_PATH = Path("/output/entry.txt")
MAX_CHARS = 280

# The entry text: 275 characters. It must stay exactly as written here —
# every word, space and full stop is part of the entry.
ENTRY_TEXT = (
    "Past midnight you lie on the roof, the shingles warm under your back. "
    "The stars come out one by one until the sky is too full to count, "
    "and the light on your face left its star before you were born. "
    "Below, the town sleeps. You are small here, and held, "
    "and nothing needs you."
)


def validate_text(text: str) -> str:
    """Check the entry against the competition's gate and return it.

    The gate needs UTF-8 text of 1 to 280 characters that is not only
    whitespace. Anything outside that range is a bug in this program,
    so it fails loudly instead of writing a bad file.
    """
    if not isinstance(text, str):
        raise TypeError("entry text must be a str")
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("entry text is empty or only whitespace")
    if len(cleaned) > MAX_CHARS:
        raise ValueError(
            f"entry text is {len(cleaned)} characters, over the {MAX_CHARS} limit"
        )
    if cleaned != text:
        raise ValueError("entry text has stray leading or trailing whitespace")
    # The gate counts Unicode code points; make sure the text round-trips
    # through UTF-8 without loss before it ever reaches the file.
    if cleaned.encode("utf-8").decode("utf-8") != cleaned:
        raise ValueError("entry text is not clean UTF-8")
    return cleaned


def write_entry(text: str, path: Path = ENTRY_PATH) -> Path:
    """Write the validated text to disk and confirm what landed there.

    The file is written only after validation passes, and the bytes on
    disk are read back and compared — a partial or altered write must
    never pass silently.
    """
    checked = validate_text(text)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(checked, encoding="utf-8")
    on_disk = path.read_text(encoding="utf-8")
    if on_disk != checked:
        raise RuntimeError("entry on disk differs from the validated text")
    return path


def main() -> None:
    destination = write_entry(ENTRY_TEXT)
    print(f"wrote {len(ENTRY_TEXT)} characters to {destination}")


if __name__ == "__main__":
    main()
