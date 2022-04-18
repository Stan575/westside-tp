"""
Selection sorting algorithm
"""


def selection_sort(a: list) -> list:
    n = len(a)
    for i in range(n-1):
        index_min = i
        for j in range(i+1, n):
            if a[index_min] > a[j]:
                index_min = j

        if i != index_min:
            a[i], a[index_min] = a[index_min], a[i]

    return a
