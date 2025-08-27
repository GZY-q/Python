fn1 = lambda: 100
print(fn1())

fn2 = lambda a: a
print(fn2('hello world'))

fn3 = lambda a, b, c=100: a + b + c
print(fn3(100,200,))
