# Git workflow — Team03

1. Open the relevant individual or team issue, assign yourself, select milestone
   `PY-W1`, and name the assigned reviewer. Huy (`tqhuy0602`, MSSV 25125053)
   receives reviews from Quyền (`pqquyenn`) and reviews Dương (`baoduong2342007`).
2. Start from the latest `main` and create a personal branch:

   ```bash
   git switch main
   git pull --ff-only origin main
   git switch -c codex/huy-w1
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
   request `pqquyenn` as reviewer. Put team setup work on a separate branch and
   in a separate PR, also reviewed by `pqquyenn`.
5. Review the assigned member's code and team setup PR. Run the relevant checks,
   inspect examples and edge cases, and leave Question, Suggestion, and Praise.
   For Huy's insertion sort, verify the input is modified and the returned list
   is the same object, since the public tests do not check this.
6. Address review feedback in new commits. Merge only after approval and passing
   checks. Update only your own row in `PROGRESS.md` with issue/PR links, actual
   test results, and actual hours. Keep unfinished fields Pending.

The maintainer creates `py-w1-done` only after the whole team's work is reviewed,
merged, and passing. Configure repository labels and milestones using
[github-setup.md](github-setup.md).
