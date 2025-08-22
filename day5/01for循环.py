# for 临时变量 in 序列：
#     重复执行的代码1
#     重复执行的代码2
#     。。。

str1 = 'gzy'
for i in str1:
    if i == 'y':
        print(f'遇到{i}不打印')
        break
    print(i)
