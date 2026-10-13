"""W1-3 - Thesis eligibility."""

MIN_CREDITS = 120
MIN_GPA = 2.0


def can_register_thesis(credits: int, gpa: float) -> bool:
    """A student may register when credits >= 120 and GPA >= 2.0."""
    return credits >= MIN_CREDITS and gpa >= MIN_GPA


def missing(credits: int, gpa: float) -> list[str]:
    """Return the unmet requirements; the credit reason comes before the GPA reason."""
    reasons = []
    if credits < MIN_CREDITS:
        reasons.append(f"need {MIN_CREDITS - credits} more credits")
    if gpa < MIN_GPA:
        reasons.append(f"need GPA at least {MIN_GPA}")
    return reasons
