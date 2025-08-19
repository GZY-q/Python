# 格式化输出 %s字符串  %d有符号的十进制  %f浮点数
"""
1.今天我的年龄是x岁
2.我的名字是x
3.我的体重是x公斤
4.我的学号是x，     我的学号是001
5.我今年x岁了
"""
age = 18
name = "tom"
weight = 260
stu_id = 1

print('今天我的年龄是%d岁' % age)
print('我的名字是%s' % name)
print('我的体重是%.2f公斤' % weight)       #  %.1f   %.2f，表示小数点后显示的小数位数。
print('我的学号是%.06d' % stu_id)            #  01%d  %06d，表示输出的整数显示位数，不足以0补全，超出当前位数则原样输出
print('我的名字是%s,今年%d岁了' %(name,age))
print('我的名字是%s,明年%d岁了'%(name,age+1))
print('我的名字是%s,今年%d,体重是%.1f公斤,学号是%06d'%(name,age,weight,stu_id))
