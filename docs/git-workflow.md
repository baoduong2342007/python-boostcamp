# Git workflow — Team03

## Week1 reviewer assignments

| Author | Username | Reviewer | Official W1-4 variant |
| --- | --- | --- | --- |
| Dương (TV1) | `baoduong2342007` | Huy (`tqhuy0602`) | 1 |
| Huy (TV2) | `tqhuy0602` | Quyền (`pqquyenn`) | 2 |
| Quyền (TV3) | `pqquyenn` | Minh (`luongnhatinh`) | 3 |
| Minh (TV4) | `luongnhatinh` | Bảo (`simble2k`) | 4 |
| Bảo (TV5) | `simble2k` | Dương (`baoduong2342007`) | Separate group test |

The same reviewer handles the author's individual and team PRs, including
follow-ups. A review contains a specific Question, Suggestion, and Praise,
plus the tested commit, commands, and actual results. For an already merged
PR, submit a supplemental review and state that it happened after merge;
do not record it as approval before merge.

## Branches, checks, and pull requests

1. Open the relevant individual or team issue, assign yourself, select milestone
   `PY-W1`, and name the assigned reviewer. Huy (`tqhuy0602`, MSSV 25125053)
   receives reviews from Quyền (`pqquyenn`) and reviews Dương (`baoduong2342007`).
2. Start from the latest `main` and create a personal branch:

   ```bash
   git switch main
   git pull --ff-only origin main
   git switch -c feat/tqhuy0602-w1
   ```

3. Implement each exercise in `members/tqhuy0602/w1/`. Test it, stage only the
   relevant file, and commit after each exercise, with at least five meaningful
   commits. Keep your own Git author identity and the actual commit dates.

   ```bash
   python -m pytest -q tests/test_w1.py --member tqhuy0602 --variant 2
   ruff check members/tqhuy0602
   git add members/tqhuy0602/w1/grades.py
   git commit -m "feat(w1-1): implement grade summary for Huy"
   ```

4. Push the branch and open one personal PR into `main`. Link its issue and
   request `pqquyenn` as reviewer. Put team setup work on branch
   `chore/t-w1-github-setup` in a separate PR, also reviewed by `pqquyenn`.
5. Review the assigned member's code and team setup PR. Run the relevant checks,
   inspect examples and edge cases, and leave Question, Suggestion, and Praise.
   For Huy's insertion sort, verify the input is modified and the returned list
   is the same object, since the public tests do not check this.
6. Address review feedback in new commits. Merge only after approval and passing
   checks. Update only your own row in `PROGRESS.md` with issue/PR links, actual
   test results, and actual hours. Keep unfinished fields Pending.

For follow-up team work, create a new branch from the latest `main`, link the
relevant team issue, and request the reviewer in the table above. Keep the
original commits and dates; do not rewrite old history to manufacture separate
PRs or exercise commits. Disclose retained AI-generated code and other AI
assistance in the PR and [AI use log](ai-use-log.md). If earlier use is unknown,
record that explicitly until the author confirms it.

## Week1 verification

Run from the repository root with `pytest` and Ruff installed. TV1–TV4 use their
username and variant from the table, for example Huy:

```bash
python -m pytest -q tests/test_w1.py --member tqhuy0602 --variant 2
python -m ruff check members/tqhuy0602
```

Expected: **5 passed**, no skips, and clean Ruff. Omitting `--member` causes
the official tests to skip; a nonexistent member folder fails import. Neither
result counts as passing. See the [README](../README.md) for all four commands
and function interfaces. Public tests are a baseline: reviewers also inspect
edge cases and the required function behavior.

TV5 implements `unique_preserve_order`, which has no official variant number.
Run the four applicable instructor tests, explicitly deselect W1-4, then run
the group-written extra test separately:

```bash
python -m pytest -q tests/test_w1.py --member simble2k -k "not test_w1_4"
python -m pytest -q tests/test_w1_extra.py --member simble2k
python -m ruff check members/simble2k/w1 tests/test_w1_extra.py
```

Expected: **4 passed, 1 deselected** in the first run, **1 passed** in the
second, and clean Ruff. Record `4 official + 1 extra`; the extra test belongs
to the group. Do not pass `--variant 5`: the official test's fallback branch
checks TV4's `primes_up_to`, not TV5's function. Do not edit instructor tests
or suppress checks to obtain a passing result. Local results do not establish
that Ubuntu/Python 3.12 CI passed.

The maintainer creates `py-w1-done` only after the whole team's work is reviewed,
merged, and passing. Configure repository labels and milestones using
[github-setup.md](github-setup.md).
