a = 10
b = 20

# 定义变量
c = 0
# 将a数据储存到c
c = a
# 将b的数据赋值到a
a = b
# 将c的值赋值给b
b = c
print(f'a={a}')
print(f'b={b}')

'''
方法二
'''

a,b=1,2
a,b=b,a
print(f'a={a}')
print(f'b={b}')