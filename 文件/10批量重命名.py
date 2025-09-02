# 需求：把code文件所有的文件进行重命名  Python-xxx
# 需求：删除Python- 重命名：1、构建条件数额 2、书写if
import os


#构造条件的数据
flag = 2


# 1找到所有文件:获取code文件夹的目录列表
file_list = os.listdir()
print(file_list)

# 2构造名字
for i in file_list:
    if flag == 1:
        new_name = 'Python_'+i
    elif flag == 2:
        num = len('Python_')
        new_name = i[num:]
# 3重命名
    os.rename(i, new_name)
