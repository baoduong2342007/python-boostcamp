"""Team regression tests for punctuation-based word boundaries.

These supplement the instructor tests without modifying them. TV4's
individually assigned implementation is intentionally left to its author.
"""

import importlib
import pytest


MEMBERS = (
    "baoduong2342007",
    "tqhuy0602",
    "pqquyenn",
    "simble2k",
)


@pytest.mark.parametrize("member", MEMBERS)
def test_punctuation_separates_words_and_preserves_unicode_and_digits(member):
    text_tools = importlib.import_module(f"members.{member}.w1.text_tools")

    assert text_tools.word_count("Hello,world! Python3 học AI;AI.") == {
        "hello": 1,
        "world": 1,
        "python3": 1,
        "học": 1,
        "ai": 2,
    }
    assert text_tools.top_k("hello,world hello", 2) == [
        ("hello", 2),
        ("world", 1),
    ]
