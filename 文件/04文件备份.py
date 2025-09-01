"""
文件备份
1接受用户输入的文件名
2规划备份文件名
3备份文件写入数据
"""
old_name = input('请输入您要备份的文件')
index = old_name.rfind('.')
# print(index)
# 原名字就是字符串中的一部分子串，切片[开始：结束：步长]
if index > 0:
    postfix = old_name[index:]
# print(old_name[index:])
# new_name = old_name[:index] + '[备份]' + old_name[index:]
new_name = old_name[:index] + '[备份]' + postfix
print(new_name)

old_f = open(old_name, 'rb')  # rb二进制
new_f = open(new_name, 'wb')

while True:
    con = old_f.read(1024)
    if len(con) == 0:
        break
    new_f.write(con)


old_f.close()
new_f.close()