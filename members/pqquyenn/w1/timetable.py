"""Module for grouping timetable entries by weekday."""


def by_day(entries: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group courses by day and return a dict with courses sorted alphabetically.

    Preserves duplicates and returns an empty dictionary for empty entries.
    """
    grouped: dict[str, list[str]] = {}
    for course, day in entries:
        grouped.setdefault(day, []).append(course)

    for courses in grouped.values():
        courses.sort()

    return grouped
