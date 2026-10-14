def by_day(entries: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group subjects by day, sorting their names and preserving duplicates."""
    grouped = {}
    for subject, day in entries:
        grouped.setdefault(day, []).append(subject)
    return {day: sorted(subjects) for day, subjects in grouped.items()}
