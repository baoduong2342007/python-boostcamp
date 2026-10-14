"""W1-4: Translate C++ to Python - Remove duplicates while preserving order."""


def unique_preserve_order(items: list[int]) -> list[int]:
    """Return a new list containing elements with duplicates removed, preserving first-occurrence order.

    Difference from C++:
    In C++, maintaining insertion order while eliminating duplicates typically requires
    explicit container types (e.g., std::vector<int> alongside std::unordered_set<int>),
    explicit iterator checks (seen.find(x) == seen.end()), and careful memory/parameter
    management (passing by const reference const std::vector<int>& to prevent deep copies).
    In Python, dynamic high-level collections allow a clean and expressive approach:
    using 'set' for O(1) membership checks with 'not in', dynamically growing a new list,
    and benefiting from automatic memory management without modifying the original input list.
    """
    seen: set[int] = set()
    result: list[int] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
