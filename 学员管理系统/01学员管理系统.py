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

    info_dict = {}

    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel

    #列表追加字典
    info.append(info_dict)
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
        print('删除')
    elif user_num == 3:
        print('修改')
    elif user_num == 4:
        print('查询')
    elif user_num == 5:
        print('显示所有')
    elif user_num == 6:
        print('退出系统')
    else:
        print('输入有误')
info_print()
