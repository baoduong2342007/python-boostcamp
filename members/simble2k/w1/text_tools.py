"""W1-2: Word counter module."""

PUNCTUATION = ".,!?;:"


def word_count(text: str) -> dict[str, int]:
    """Count occurrences of each word in text, case-insensitive and ignoring punctuation .,!?;:."""
    cleaned = text.lower().translate(str.maketrans("", "", PUNCTUATION))
    counts: dict[str, int] = {}
    for word in cleaned.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return top k most frequent words sorted by count (descending), then alphabetically (ascending)."""
    if k <= 0:
        return []
    counts = word_count(text)
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return ranked[:k]
