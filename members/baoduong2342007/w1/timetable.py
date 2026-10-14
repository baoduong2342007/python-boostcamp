def by_day(a : list[tuple[str , str]]) -> dict[str , list[str]] :
    b = {}
    for course , day in a :
        b.setdefault(day, []).append(course)
    for day in b :
        b[day].sort()
    return b
