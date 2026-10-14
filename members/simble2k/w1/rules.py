"""W1-3: Thesis eligibility module."""


def can_register_thesis(credits: int, gpa: float) -> bool:
    """Return True if credits >= 120 and gpa >= 2.0."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """Return list of human-readable reasons if requirements are unmet."""
    reasons: list[str] = []
    if credits < 120:
        reasons.append(f"need {120 - credits} more credits")
    if gpa < 2.0:
        reasons.append("need GPA at least 2.0")
    return reasons
