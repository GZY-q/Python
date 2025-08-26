#等待存储所有学员信息
info = []
def info_print():
    print('请选择功能----------')
    print('1.添加学员')
    print('2.删除学员')
    print('3.修改学员')
    print('4.查询学员')
    print('5.显示所有学员')
    print('-' * 20)
#定义函数
# todo:添加学员函数
def add_info():
    #用户输入学号姓名手机号
    new_id = input('请输入学号：')
    new_name = input('请输入姓名：')
    new_tel = input('请输入手机号：')
    #判断是否添加这个学员
    global info
    for i in info:
        if new_id == i['name']:
            print('此用户已经存在')
            #return：退出当前代码
            return


    info_dict = {}
#字典创建
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel

    #列表追加字典
    info.append(info_dict)
    print(info)


#todo:删除学员函数
def del_info():
    #1.用户输入要删除的姓名
    del_name = input('请输入要删除的学员姓名:')
    #2.判断学员是否存在，存在则删除，不存在提示
    #声明info是全局变量
    global info
    #遍历列表
    for i in info:
        if del_name == i['name']:
            info.remove(i)
            break
    else:
        print('该学员不存在')
    print(info)
    #判断学员是否存在，存在就删除（列表里的字典）break：这个系统不允许重名，删除了一个不需要遍历，不存在就提示


#todo:修改学员信息函数

def modify_info():
    #1.用户输入要修改的学员姓名
    modify_name = input('请输入要修改的学员的姓名')
    global info
    for i in info:
        if modify_name == i['name']:
            i['tel'] = input('输入要修改的电话')
            break
    #打印info

    else:
        print('该学员不存在')
    #2.判断学员是否存在
    print(info)

#系统需要循环使用
while True:
    #1显示功能界面
    info_print()
    #2用户输入功能序号
    user_num = int(input('请输入功能序号：'))
    #3按照用户输入的序号执行不同的功能
    if user_num == 1:
        #print('添加')
        add_info()
    elif user_num == 2:
        #print('删除')
        del_info()
    elif user_num == 3:
        modify_info()
    elif user_num == 4:
        print('查询')
    elif user_num == 5:
        print('显示所有')
    elif user_num == 6:
        print('退出系统')
    else:
        print('输入有误')
info_print()
