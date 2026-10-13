def summary(scores: list[float]) -> dict:
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
