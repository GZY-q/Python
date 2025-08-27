# filter用于过滤序列，过滤掉不符合条件的元素，返回一个filter对象，如果要转换为列表，可以使用list()来转换

# 定义功能函数，过滤序列中的偶数
list1 = [1, 2, 3, 4, 5]


def func(x):
    return x % 2 == 0


result = filter(func, list1)
print(list(result))
