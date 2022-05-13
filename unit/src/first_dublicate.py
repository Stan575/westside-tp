'''
Given a list a that contains only numbers in range from 1 to len(a), find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than one duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.
Examples:
For a = [2, 1, 3, 5, 3, 2]  the output should be first_duplicate(a) = 3
For a = [2, 2]  the output should be first_duplicate(a) = 2
For a = [2, 4, 3, 5, 1]  the output should be first_duplicate(a) = -1
'''


def first_duplicate(a):
    if len(a) == 2:
        return -1 if a[0] != a[1] else a[0]
    for i in range(0, len(a) - 1):
        for j in range(i + 1, len(a) - 1):
            if a[i] == a[j]:
                return a[j]
    return -1


print(first_duplicate([10, 20, 30, -20, 2, 30, 40, 50, -20, 60, 60, -20, -20]))
print(first_duplicate([2, 1, 3, 5, 3, 2]))
print(first_duplicate([2, 1, 3, 5, 1, 3, 2]))
print(first_duplicate([2, 2]))
print(first_duplicate([2, 4, 3, 5, 1]))
