# 道歉5遍，完成之后再原谅
i = 1
while i <= 5:
    if i == 3:
        i += 1
        break#continue
    print('我对了')
    i += 1
else:  # 完成之后才会执行
    print('原谅了')
