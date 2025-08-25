name_list = ['tom','lily','john']

name = input('请输入您的用户名')

if name in name_list:
    print(f'您输入的名字{name}已存在')
else:
    print(f'你的名字是{name}注册成功')
