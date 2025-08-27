#map(func,lst),返回一个迭代器,将传入的函数变量func作用到lst变量的每个元素中，并将结果组成新的列表
list1 = [1,2,3,4,5]

def func(x):
    return x ** 2

result = map(func, list1)
print(result)
print(list(result))