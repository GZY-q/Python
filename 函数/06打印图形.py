def print_line():
    print('-' * 20)


# print_line()


# 函数嵌套调用

def print_lines(num):
    i = 0
    while i < num:
        print_line()
        i += 1


print_lines(5)
