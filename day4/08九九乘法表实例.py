# j = 0
# while j < 5:
# #一行开始
#     i=0
#     while i < 5:
#         print('*', end='')
#         i += 1
#     print() #换行
#     j += 1
j = 1
while j < 10:
    i = 1
    while i <= j:
        print(f'{i}x{j}={i*j}', end='\t')
        i += 1
        # 一行结束
    print()
    j += 1

