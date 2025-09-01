# 1文件的打开
# 2读写操作
# 3关闭
# open(name,mode)
f = open('students.txt', 'w')

f.write('aa')

f.close()
# 写入会覆盖原有内容