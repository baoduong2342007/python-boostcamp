"""Module for thesis registration eligibility rules."""


def can_register_thesis(credits: int, gpa: float) -> bool:
    """Return True if student meets credit and GPA thresholds for thesis."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """Return list of human-readable reasons if requirements are unmet."""
    reasons: list[str] = []
    if credits < 120:
        needed = 120 - credits
        reasons.append(f"need {needed} more credits")
    if gpa < 2.0:
        reasons.append("need GPA at least 2.0")
    return reasons
