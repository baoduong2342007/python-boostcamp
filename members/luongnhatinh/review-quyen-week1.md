# Review notes for Quyên's Week1 PR #14

Prepared by Minh (TV4) on 2026-10-14.
PR: https://github.com/baoduong2342007/python-bootcamp/pull/14, merged commit `b400900`.
GitHub Review Comment: https://github.com/baoduong2342007/python-bootcamp/pull/14#issuecomment-6170604741

This document records the follow-up post-merge review as required by the team workflow, not an approval prior to merge.

## Validation
- `python -m pytest -q tests/test_w1.py --member pqquyenn --variant 3`: 5 passed in 0.16s, no skips.
- `python -m ruff check members/pqquyenn`: All checks passed!
- Instructor tests were not modified.
- All 5 exercises correctly implement the Week 1 requirements:
  - W1-1 (`grades.py`): Correctly raises `ValueError` on empty input; accurately calculates min, max, mean, and median rounded to 2 decimal places.
  - W1-2 (`text_tools.py`): Clean tokenization stripping `.,!?;:`; case-insensitive word count; correct tie-breaking for `top_k` sorted by count descending and word ascending.
  - W1-3 (`rules.py`): Accurately verifies credit (>= 120) and GPA (>= 2.0) thresholds; returns clear descriptive reasons in `missing`.
  - W1-4 (`translate.py`): Matrix transpose (Variant 3) cleanly implemented with `zip(*matrix)` and list comprehension; includes informative docstring contrasting C++ `std::vector<std::vector<int>>` with Python dynamic lists.
  - W1-5 (`timetable.py`): Uses `setdefault` and sorts by iterating over `.values()`, completely avoiding Ruff `PLC0206`.

## Praise
- Code is very clean, concise, and well-structured, with clear docstrings and complete PEP 484 type annotations throughout.
- Matrix transpose variant is idiomatic and pythonic, properly handling edge cases like empty matrices or empty rows.
- Ruff clean with zero warnings on the first pass.

## Question
- Can Quyên confirm the actual hours spent on Week 1 and state AI use explicitly (e.g., None if completely self-written, or disclose any tools used) so that the team progress table (`PROGRESS.md`) and `docs/ai-use-log.md` can be updated from Pending?
- In `grades.py`, `round(..., 2)` handles floating point values cleanly. Did you consider any special float cases such as empty / invalid inputs for future exercises?

## Suggestion
- Link the personal Week 1 Issue to PR #14 and update your progress row in `PROGRESS.md`.
- When implementing the team CI workflow (TV3 assignment), ensure separate jobs for `pytest` and `ruff` on Ubuntu with Python 3.12, along with the environment setup guide for the team.
