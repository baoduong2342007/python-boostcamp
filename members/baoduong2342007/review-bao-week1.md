# Supplemental review notes for Bao's Week1 PR #15

Prepared for Dương with Codex assistance on 2026-10-14. PR: https://github.com/baoduong2342007/python-bootcamp/pull/15, head `f9572bd33bc580ea66e19f7f89729c660390578e`. This is a factual post-merge review draft based on the merged code on `main`; it is not a review submitted on GitHub and does not represent pre-merge approval.

## Validation performed

- `python -m pytest -q tests/test_w1.py --member simble2k -k 'not test_w1_4_translate'`: 4 passed, 1 deselected.
- `python -m pytest -q tests/test_w1_extra.py --member simble2k`: 1 passed.
- `python -m ruff check members/simble2k tests/test_w1_extra.py`: all checks passed.
- The group-written extra test covers empty input, all duplicates, interleaved duplicates, negative values and zero, and preservation of the input. The instructor test files were not modified.

## Question

Can Bao confirm that the PR's AI-use declaration matches the declaration now recorded in `docs/ai-use-log.md`? The log says AI did not generate or retain the exercise solution code and was used for workflow guidance, Ruff verification, and progress documentation.

## Suggestion

Keep the progress label `4 official + 1 extra` so the group-written test is not mistaken for an instructor test. The current progress row now links issue #16 and PR #15.

## Praise

`unique_preserve_order` builds a new result and uses a set for membership checks, preserving first occurrence order without modifying the input. The extra test verifies those behaviors, and the README keeps the official tests separate from the TV5-specific check.

## Conclusion

The validation above passed on the current main checkout. The review notes describe a supplemental review after merge; no GitHub review has been posted by this task.
