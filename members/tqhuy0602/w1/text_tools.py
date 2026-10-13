"""W1-2 - Word counter."""

PUNCTUATION = ".,!?;:"


def word_count(text: str) -> dict[str, int]:
    """Count words after lowercasing and removing the characters .,!?;:"""
    cleaned = text.lower().translate(str.maketrans("", "", PUNCTUATION))
    counts: dict[str, int] = {}
    for word in cleaned.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return the k most frequent words.

    Sorted by count descending, ties broken alphabetically ascending.
    Team convention: k <= 0 returns []; k larger than the number of
    distinct words returns every word.
    """
    if k <= 0:
        return []
    items = sorted(word_count(text).items(), key=lambda item: (-item[1], item[0]))
    return items[:k]
