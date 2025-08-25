def sum_mun(a, b, c):
    return a + b + c


result = sum_mun(1, 2, 3)
print(result) #6


def average_mun(a, b, c):
    sumResult = sum_mun(a, b, c)
    return int(sumResult) / 3
averageResult = average_mun(1, 2, 3)
print(averageResult)