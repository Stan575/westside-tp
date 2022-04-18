"""
There are two wooden sticks of lengths a and b respectively.
Each of them can be cut into shorter sticks of integer lengths.
Our goal is to construct the largest possible square.
In order to do this, we want to cut the sticks in such a way as to achieve four sticks of the same length
(note that there can be some leftover pieces).
What is the longest side of square that we can achieve?
Write a function:
	def solution (a, b)
that, given two integers a, b, returns the side length of the largest square that we can obtain.
If it is not possible to create any square, the function should return 0.
Examples:
1. Given a = 10, b = 21, the function should return 7. We can split the second stick into three sticks of length 7 and shorten the first stick by 3.
2. Given a = 13, b = 11, the function should return 5. We can cut two sticks of length 5 from each of the given sticks.
3. Given a = 2, b = 1, the function should return 0. It is not possible to make any square from the given sticks.
4. Given a = 1, b = 8, the function should return 2. We can cut stick B into four parts.
Write an efficient algorithm for the following assumptions: A and B are integers within the range [1..1,000,000,000).
"""


def solution(long, short):
    # if same length
    if long == short:
        return long // 2

    # make sure long is longer than short
    if short > long:
        long, short = short, long

    # find longest possible perimeter
    length_sum = long + short

    # return 0 if not possible to make four sticks of length 1
    if length_sum < 4:
        return 0

    # if short is too short to consider deal with the long one
    if short <= long // 4:
        return long // 4

    # find longest possible side
    max_length = length_sum // 4

    # the magic
    for num in range(max_length, 0, -1):
        if long // num + short // num == 4:
            return num


assert solution(10, 21) == 7
assert solution(13, 11) == 5
assert solution(2, 1) == 0
assert solution(1, 8) == 2
assert solution(1, 3) == 1
assert solution(1, 1) == 0
assert solution(5, 5) == 2
assert solution(5, 1) == 1
assert solution(2, 2) == 1
