"""W1-4 - In-place insertion sort (variant 2), translated from C++."""


def insertion_sort(a: list) -> list:
    """Sort a in place with insertion sort and return the same list object.

    C++ vs Python: in C++ the function would take `vector<int>& a` to modify
    the caller's vector; Python passes a reference to the list object, so
    assigning to a[j + 1] changes the caller's list without any `&`.
    """
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a
