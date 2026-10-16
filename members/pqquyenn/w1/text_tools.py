"""Module for text processing and word frequency analysis."""


def _clean_and_tokenize(text: str) -> list[str]:
    """Treat standard punctuation as separators between lowercase words."""
    punctuation = ".,!?;:"
    cleaned = "".join(" " if ch in punctuation else ch for ch in text)
    return cleaned.lower().split()


def word_count(text: str) -> dict[str, int]:
    """Count the occurrence of each word in text, case-insensitive."""
    words = _clean_and_tokenize(text)
    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return top k frequent words sorted by count (desc), then word (asc)."""
    if k <= 0:
        return []
    counts = word_count(text)
    if not counts:
        return []
    sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_items[:k]
