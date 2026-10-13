def insertion_sort(a: list[int]) -> list[int]:
    """Sort in place with insertion sort and return the same list.

    Python passes a reference to a mutable list, so item assignments affect the
    caller's list. In C++, a vector parameter needs an explicit reference (&)
    to modify the caller's vector instead of a copy.
    """
    for index in range(1, len(a)):
        value = a[index]
        previous = index - 1
        while previous >= 0 and a[previous] > value:
            a[previous + 1] = a[previous]
            previous -= 1
        a[previous + 1] = value
    return a
