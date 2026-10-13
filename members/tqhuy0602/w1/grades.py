"""W1-1 - Grade summary."""


def summary(scores: list[float]) -> dict:
    """Return min, max, mean and median of the scores.

    Mean and median are rounded to two decimals with Python's round().
    The input list is not modified: sorted() returns a new list.
    """
    if not scores:
        raise ValueError("scores must not be empty")

    ordered = sorted(scores)
    n = len(ordered)
    mid = n // 2
    if n % 2 == 1:
        median = ordered[mid]
    else:
        median = (ordered[mid - 1] + ordered[mid]) / 2

    return {
        "min": ordered[0],
        "max": ordered[-1],
        "mean": round(sum(scores) / n, 2),
        "median": round(median, 2),
    }
