"""
Finding a median value of an array of numbers.
If result is a decimal number, round to 3 digits after decimal point
"""


def median(a: list):
    """
    O(n log n)
    :param a: list of numbers
    :return: median value
    """
    if not a:
        return

    if len(a) == 1:
        return a[0]

    b = sorted(a)

    if len(b) % 2:
        return b[len(b) // 2]
    else:
        middle = len(b) // 2
        median_ = (b[middle] + b[middle - 1]) / 2
        if median_.is_integer():
            return int(median_)
        else:
            return round(median_, 3)

