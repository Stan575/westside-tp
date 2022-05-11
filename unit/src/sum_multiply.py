def sum_and_multiply(sum, multiply):
    if not multiply:
        return [0, sum]

    for i in range(1, sum):
        x = i
        y = sum - x
        if x + y == sum and x * y == multiply:
            return sorted([x, y])


sum_and_multiply(12, 36)  # == [6, 6]
sum_and_multiply(6, 9)  # == [3, 3]
sum_and_multiply(200, 8458)  # == None
