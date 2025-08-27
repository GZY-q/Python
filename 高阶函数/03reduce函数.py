list2 = [1, 2, 3, 4, 5]
import functools  #*****导入模块


# 1导入模块
# 2定义功能模块
# reduce作用：功能函数计算的结果和序列的下一个数据做累计计数

def func(a, b):
    return a + b


result = functools.reduce(func, list2)
print(result)
