# AI use log

## 2026-10-14 — TV1 / baoduong2342007

- Dương confirms that the original five Week1 exercises were self-written and AI assistance was used for GitHub operations. Reported time: approximately 2 hours.
- Codex assisted with review, running checks, opening PR #17, and resolving/merging Huy's PRs #10/#11 at Dương's request. The conflict resolutions preserved team progress and both README verification guides; no individual Python code was changed in those merges.
- In the TV1 follow-up linked to issue #18, Codex changed the timetable loop from dictionary-key lookup to iteration over `b.values()` to resolve Ruff PLC0206. This AI-assisted code change is retained; W1-2 punctuation behavior remains unchanged.
- Verification after the follow-up change: TV1 official tests 5 passed, no skip; Ruff for TV1 passed; `git diff --check` passed. Local checks are not evidence of Ubuntu CI.
- The original exercise history has one combined commit. It was not rewritten to manufacture five exercise commits.
- Bao's PR #15 was read and tested with Codex assistance; the local review notes are in TV1's member folder. These notes are not a GitHub approval or a review performed before the original merge.

## 2026-10-14 — TV5 / simble2k

- Bảo confirms that the five Week 1 exercises (`grades.py`, `rules.py`, `text_tools.py`, `timetable.py`, `translate.py`) and the extra test suite (`tests/test_w1_extra.py`) were implemented independently. AI assistance was not used to generate or retain solution code (`AI use: None` for exercise logic). Actual time spent: approximately 2 hours.
- AI assistance was used for Git/GitHub workflow guidance, formatting verification with Ruff, and preparing progress documentation.
- Verification results: 4 official instructor tests passed, 1 deselected (`test_w1_4_translate`); 1 extra test passed (`tests/test_w1_extra.py`); Ruff check and format clean for `members/simble2k/w1` and `tests/test_w1_extra.py`.
- Progress tracking: linked to issue #16 and merged PR #15 in `PROGRESS.md`.
## 2026-10-14 — TV4 / luongnhatinh

- Minh confirms that the original five Week1 exercises were self-written with no AI assistance (as declared in PR #13: None). Recorded actual time: 3.5 hours.
- In the follow-up review based on `need_to_fix.md`:
  - AI assistance was used to check and resolve Ruff warnings: refactored dictionary value iteration in `members/luongnhatinh/w1/timetable.py` to eliminate `PLC0206`, formatted the import block in `members/luongnhatinh/w1/translate.py` to resolve `I001`, and fixed escaped Markdown characters in the PR #13 body.
  - Follow-up verification for TV4: 5 official tests passed with 0 skips (`--member luongnhatinh --variant 4`), Ruff clean (`All checks passed!`). TV4 personal follow-up PR #20 opened and requested Bao (@simble2k) to review.
  - AI assisted with drafting team documentation for function interfaces (TV1–TV4), logging the official test source revision `2c6edc79772984f6a6ca0c3664ad0a49c907e80a` and upstream audit, recording review notes for Quyên's PR #14, and preparing the team documentation PR.
