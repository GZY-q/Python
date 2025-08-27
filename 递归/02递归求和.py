def sum_num(num):
    if num == 1:
        return 1
    return num + sum_num(num - 1)

print(sum_num(5))

def chen_num(num):
    if num == 1:
        return 1
    return num * chen_num(num - 1)
print(chen_num(4))