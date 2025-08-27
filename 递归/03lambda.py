# lambda 参数列表 ：表达式
# 能接受任何数量的参数，但只能返回一个返回值

# 函数
def fn1():
    return 100


result = fn1()
print(result)

fn2 = lambda: 100  # 匿名函数
print(fn2)  # 内存地址
print(fn2())  # 返回值100
