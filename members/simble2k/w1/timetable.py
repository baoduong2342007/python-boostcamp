"""W1-5: Group timetable entries by day."""


def by_day(timetable: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group courses by day and return a dict from day to a sorted list of courses.

    Uses dict.setdefault to group courses by day and dictionary comprehension to sort them.
    """
    grouped: dict[str, list[str]] = {}
    for course, day in timetable:
        grouped.setdefault(day, []).append(course)

    return {day: sorted(courses) for day, courses in grouped.items()}
