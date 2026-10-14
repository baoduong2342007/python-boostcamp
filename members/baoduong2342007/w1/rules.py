def can_register_thesis(credits: int, gpa: float) -> bool:
    return ((credits >= 120) and (gpa >= 2.0))

def missing(credits, gpa) -> list[str] :
    x = []
    if (can_register_thesis(credits , gpa) == False) :
        if (credits < 120) :
            y = 'need ' + str(120 - credits) + ' more credits'
            x.append(y)

        if (gpa < 2.0) :
            y = 'need GPA at least 2.0'
            x.append(y)
    return x
