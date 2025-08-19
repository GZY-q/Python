age = int(input('请输入你的年龄：'))

if 18<=age<=60:
    print('合法')
elif age<18:
    print('童工')
elif age>60:
    print('太老了。。。')

else:
    print('不是人类')

# age = int(input('请输入您的年龄：'))
# if age < 18:
#     print(f'您的年龄是{age},童工一枚')
# elif 18 <= age <= 60:
#     print(f'您的年龄是{age},合法工龄')
# else:
#     print(f'您的年龄是{age},可以退休')