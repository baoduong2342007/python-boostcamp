# AI use log

## 2026-10-15 — TV2 / tqhuy0602

- Trần Quốc Huy confirms that the five original Week1 exercise implementations
  were self-written; AI assisted the other operations in PR #10/#11. No
  AI-generated exercise code is declared retained by Huy. Actual Week1 time
  before this follow-up: 2 hours, confirmed by Huy in this session.
- Codex assisted this follow-up by inspecting PR #17/#19 at their exact heads,
  running official tests, Ruff and edge checks, drafting supplemental reviews,
  adding the reviewer table and TV5 workflow, and preparing Git/GitHub updates.
  No individual exercise Python code or instructor tests changed in this PR.
- Verification on main `07b39013b62145d4e035fe8e964c6637aa65c9be`: Huy 5 official
  tests passed, no skips; Ruff clean; 1,093 insertion-sort cases passed with
  in-place mutation and identical returned object. TV5: 4 official passed,
  1 deselected; 1 group extra passed; Ruff clean. Local Python version: 3.14.0.
- Dương's original PR #17: 5 official passed; Ruff reported PLC0206. Follow-up
  PR #19: 5 official passed; Ruff clean. Both PRs were already merged when
  reviewed; these are supplemental reviews, not approvals before merge.
- Commands, tested revisions, review links and follow-up links are recorded
  in [Huy's evidence](../members/tqhuy0602/week1-followup.md). This local
  verification does not establish Ubuntu/Python 3.12 CI success.

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
