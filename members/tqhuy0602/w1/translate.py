def insertion_sort(a: list) -> list:
    """C++ needs `vector<int>& a` to sort the caller's vector; a Python list is already passed by reference."""
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a
