# 1位置参数调用的时候根据函数定义的参数来传递
def user_info(name, age, gender):
    print(f'你的名字{name}，年龄是{age}，性别是{gender}')


user_info('tom',20,'男')


#2关键字参数
def user_info(name, age, gender):
    print(f'你的名字{name}，年龄是{age}，性别是{gender}')


user_info('小明',gender='男',age='20')

#缺省参数
def user_info(name, age, gender='男'):
    print(f'你的名字{name}，年龄是{age}，性别是{gender}')

user_info('tom',20,'女')


#不定长参数
def user_info(*args):
    print(args)


user_info('tom', 18, 22)
#args收集变量，都会输出一个元组





#包裹一个关键字

def user_info(**kwargs):
    print(kwargs)


# {'name': 'TOM', 'age': 18, 'id': 110}
user_info(name='TOM', age=18, id=110)

















