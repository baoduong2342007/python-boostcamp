def binary_search(a : list[int] , key : int) -> int :
    """Search a sorted list using Python's dynamic list instead of a sized C++ array.

    Both languages use zero-based indexing, but Python lists grow dynamically and
    do not require a separately declared array length.
    """
    l = 0
    r = len(a) - 1
    while (l <= r) :
        mid = (l + r) // 2
        if (a[mid] == key) :
            return mid
        if (a[mid] < key) :
            l = mid + 1
        else :
            r = mid - 1
    return -1
