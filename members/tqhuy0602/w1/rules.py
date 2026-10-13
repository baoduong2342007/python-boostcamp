def can_register_thesis(credits: int, gpa: float) -> bool:
    """Check the minimum credits and GPA required for thesis registration."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """List unmet requirements, with the credits requirement first."""
    reasons = []
    if credits < 120:
        reasons.append(f"need {120 - credits} more credits")
    if gpa < 2.0:
        reasons.append("need GPA at least 2.0")
    return reasons
