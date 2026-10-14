"""Extra test for Member 5's W1-4 variant (unique_preserve_order).

Not part of official instructor tests; written for Member 5's personal variant.
"""

import pytest


def test_w1_4_unique_preserve_order(load, member):
    if member != "simble2k":
        pytest.skip("Test specifically for Member 5 (simble2k)")
    tr = load("w1", "translate")
    assert tr.unique_preserve_order([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4]
    assert tr.unique_preserve_order([]) == []
    assert tr.unique_preserve_order([5, 5, 5]) == [5]
    assert tr.unique_preserve_order([-1, 0, -1, 2, 0]) == [-1, 0, 2]
    items = [3, 1, 2, 1]
    result = tr.unique_preserve_order(items)
    assert result == [3, 1, 2]
    assert items == [3, 1, 2, 1]
    assert tr.__doc__ or any(
        getattr(tr, n).__doc__ for n in dir(tr) if callable(getattr(tr, n))
    )
