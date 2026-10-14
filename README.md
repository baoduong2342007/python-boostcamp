# Python Bootcamp - Team03

This repository contains Team03's Python exercises for **CSC10014 - Computational Thinking**, covering Weeks 1, 2, and 3. The team builds on its C++ background to learn Python while practicing collaboration with Git and GitHub.

## Topics

| Week | Topics |
| --- | --- |
| W1 | Syntax, data types, conditionals, loops, functions, strings, and basic data structures |
| W2 | Modules, file handling, CSV/JSON, exceptions, classes, dataclasses, and pytest |
| W3 | The standard library, type hints, argparse, Ruff, and study planner integration |

## Team Members

| Member | Name | GitHub / Personal Folder |
| --- | --- | --- |
| 1 | Trương Quang Bảo Dương | [baoduong2342007](https://github.com/baoduong2342007) |
| 2 | Trần Quốc Huy | [tqhuy0602](https://github.com/tqhuy0602) |
| 3 | Phan Quỳnh Quyền | [pqquyenn](https://github.com/pqquyenn) |
| 4 | Lương Nhật Minh | [luongnhatinh](https://github.com/luongnhatinh) |
| 5 | Phạm Quốc Bảo | [simble2k](https://github.com/simble2k) |

## Repository Structure

```text
python-boostcamp/
├── README.md
├── PROGRESS.md              # Progress by member and week
├── .gitignore
├── .github/                # Issue templates and CI
├── members/                # Individual exercises
│   ├── baoduong2342007/
│   ├── tqhuy0602/
│   ├── pqquyenn/
│   ├── luongnhatinh/
│   └── simble2k/
├── shared/                 # Shared team exercises
├── tests/                  # Tests
└── docs/                   # Documentation and AI use records
```

Each member's folder contains `w1/`, `w2/`, and `w3/`. Individual exercises belong in their author's folder; team work belongs in the relevant shared folders.

## Workflow

Each member works on a separate branch, opens a pull request, and receives a review before merging. Record progress, test results, and issue/PR links in [PROGRESS.md](PROGRESS.md). Disclose AI assistance in [docs/ai-use-log.md](docs/ai-use-log.md).

**Current status:** the scaffold and instructor Week 1 tests are available. Each member completes their own exercises. Use [PROGRESS.md](PROGRESS.md) for individual completion and test results.

### Verification for Member 5 (simble2k)

Run Week 1 checks from the repository root in an environment with pytest and Ruff installed:

```bash
# Run 4 official instructor tests (deselecting instructor variant 1-4)
python -m pytest -q tests/test_w1.py -k "not test_w1_4" --member simble2k

# Run 1 extra test for Member 5's unique_preserve_order
python -m pytest -q tests/test_w1_extra.py --member simble2k

# Linter and formatting check
python -m ruff check members/simble2k/w1 tests/test_w1_extra.py
python -m ruff format --check members/simble2k/w1 tests/test_w1_extra.py
```

Expected result: 4 official passed, 1 deselected; 1 extra test passed (`4 official + 1 extra`).

## Course Materials

The exercises follow Chapter 18 of **Git & GitHub for Team Projects**. Instructor materials and reference tests are available in [CSC10014 public materials](https://github.com/CSC10014-at-fit-hcmus/public_materials).
