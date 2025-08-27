
print('计算a+b')

while True:
    fn1 = lambda a, b: a + b
    a = int(input('输入a的值：'))
    b = int(input('输入b的值：'))
    print(fn1(a,b))