"""
1，8老师（嵌套列表）
2，3办公室（随机分配）
3，验证是否成功
"""
import random
# 1
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
offices = [[],[],[]]
# 2
for name in teachers:
    #列表追加数据 --append(选中) extend insert
    #xx[0] - -不能指定是具体某个下标 - -随机
    num = random.randint(0,2)
# print(num)
    offices[num].append(name)
# print(offices)
i = 1
#验证是否成功
for office in offices:
    #打印办公室人数
    print(f'办公室{i}人数是{len(office)}')
    #打印老师的名字
    for name in office:
        print(name)
    i+=1