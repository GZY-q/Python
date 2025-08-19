"""
1. 书写input
2. 观察特点：1等待用户输入2接受input存变量3.input接受数据类型
"""
password = input('请输入您的密码：')
print(f'您输入的密码是{password}')

print(type(password))   # <class 'str'>