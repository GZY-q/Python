# #abs 求绝对值
# result = abs(-10)
# print(result)
# #对数字四舍五入计算
# print(round(1.2))
# print(round(1.9))


def add_num(a, b):
    return abs(a) + abs(b)


result = add_num(-1, 2)
print(result)  # 3


def sum_num(a, b, f):  # f是参数，作为参数
    return f(a) + f(b)


result = sum_num(-1, 2, abs)
print(result)
