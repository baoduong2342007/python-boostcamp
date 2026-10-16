"""W1-4: Translate C++ to Python - Remove duplicates while preserving order."""


def unique_preserve_order(items: list[int]) -> list[int]:
    """Return a new list containing elements with duplicates removed, preserving first-occurrence order.

    Difference from C++:
    A C++ starting point is `vector<int> uniquePreserveOrder(const vector<int>& items)`:
    loop through `items`, check `seen.find(item) == seen.end()`, then append the item
    to both a result vector and the set. C++ requires explicit container types and
    iterator checks; Python uses dynamic lists and sets with direct membership tests.
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
