# Git Workflow

Short guide for Team03. Based on Chapter 18 of **Git & GitHub for Team Projects** (18.3 workflow, 18.9 review, 18.11 AI use).

## Labels and milestones

| Name | Use |
| --- | --- |
| `python-hw` | Individual exercises |
| `team-hw` | Shared team tasks |
| `w1`, `w2`, `w3` | Week of the work |
| `PY-W1`, `PY-W2`, `PY-W3` | Milestone per week; due dates come from LMS only |

## Steps for each week

1. **Issue.** Open an issue from the *Python exercises* or *Team task* template, assign yourself, add the week label and milestone, and name your reviewer.
2. **Branch.** Start from an up-to-date `main`:
   ```bash
   git switch main
   git pull
   git switch -c feat/<github-username>-w1
   ```
   Team tasks use `chore/t-w1-<topic>`.
3. **Commit.** Work only in `members/<github-username>/wx/` (or the shared folder for team tasks). Commit after each exercise with a clear message, e.g. `feat(py-w1): W1-2 word counter`. Never fake authors or dates.
4. **Check.** Run before pushing:
   ```bash
   pytest -q tests/test_w1.py --member <github-username> --variant <N>
   ruff check members/<github-username>
   ```
   Tests that are skipped do not count as passed.
5. **PR.** Push and open one PR per issue with `Closes #<issue>`, the same labels and milestone, and request your reviewer. Declare any AI use in the PR and in [ai-use-log.md](ai-use-log.md).
6. **Review.** The reviewer reads the code, runs the checks, tries the examples and edge cases, and leaves at least one **Question**, **Suggestion** and **Praise**.
7. **Fix and merge.** The author makes the fixes. Merge only after approval and green checks, then delete the branch.
8. **Progress.** Update your own row in [PROGRESS.md](../PROGRESS.md) with the issue/PR links, reviewer, test result and actual hours.

## Keeping a branch up to date

```bash
git switch main
git pull
git switch feat/<github-username>-w1
git merge main
```

Resolve conflicts, rerun the checks, then push. Do not commit `.venv/`, caches or secrets.
