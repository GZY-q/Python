#引用当实参
def aa(a):
    print(a)
    print(id(a))


    a+=a
    print(a)
    print(id(a))

aa(1)