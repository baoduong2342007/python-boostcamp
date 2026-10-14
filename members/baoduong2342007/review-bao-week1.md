# Review notes for Bao's Week1 PR #15

Prepared for Dương with Codex assistance on 2026-10-14. PR: https://github.com/baoduong2342007/python-bootcamp/pull/15, head `f9572bd33bc580ea66e19f7f89729c660390578e`. The reviewed code and extra test on current main match that PR's implementation. This document is a follow-up review draft, not a GitHub approval before merge.

## Validation

- `python -m pytest -q tests/test_w1.py --member simble2k -k 'not test_w1_4_translate'`: 4 passed, 1 deselected.
- `python -m pytest -q tests/test_w1_extra.py --member simble2k`: 1 passed.
- `python -m ruff check members/simble2k tests/test_w1_extra.py`: passed.
- The extra test covers empty input, all duplicates, interleaved duplicates, negatives/zero, and input preservation. Instructor tests were not modified.
- The unique-preserve-order implementation creates a new result list and tracks membership with a set. The C++/Python comparison is documented; the README separates official tests from the extra group test.

## Question

Can Bao confirm the AI-use declaration for this PR and add issue #16 / PR #15 to his progress row? The current PR body has no AI-use declaration and the progress links remain Pending. This does not establish whether AI was used.

## Suggestion

Add the actual issue and PR links to the progress row and state AI use explicitly, including None if applicable. Keep the label `4 official + 1 extra` so the extra test is not mistaken for an instructor test.

## Praise

The extra test clearly identifies itself as group-written and checks that deduplication preserves the original input. The README commands correctly avoid running the instructor's sieve variant for TV5.

## Conclusion

The checked tests and Ruff pass. Remaining feedback concerns evidence and declarations. No Bao files were changed. Dương should read these notes before personally submitting his review on GitHub; no review has been posted by this follow-up task.
