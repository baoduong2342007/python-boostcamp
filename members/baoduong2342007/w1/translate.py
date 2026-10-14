def binary_search(a : list[int] , key : int) -> int :
    """Python lists use zero-based indexing and need no declared array size."""
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
