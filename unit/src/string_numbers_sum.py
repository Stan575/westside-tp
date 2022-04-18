"""
    Write a function that returns sum of all numbers from a given string.
    "hello5word15hi" -> 20 (5+15)
"""


def get_num_sum_from_string(s):
    num_sum = 0
    num = ''
    for i in range(len(s)):
        if s[i].isdigit():
            num += s[i]
            if i == len(s) - 1:
                num_sum += int(num)
        else:
            if num != '':
                num_sum += int(num)
                num = ''

    return num_sum
