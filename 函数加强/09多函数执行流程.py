glo_num = 0



def a():
    global glo_num
    glo_num = 100


def b():
    print(glo_num)

a()
b()