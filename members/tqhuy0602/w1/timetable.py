"""W1-5 - Group the timetable."""


def by_day(entries: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group (course, day) pairs by day; courses sorted ascending, duplicates kept."""
    grouped: dict[str, list[str]] = {}
    for course, day in entries:
        grouped.setdefault(day, []).append(course)
    return {day: sorted(courses) for day, courses in grouped.items()}
