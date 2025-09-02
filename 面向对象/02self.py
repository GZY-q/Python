#定义类:洗衣机 功能 洗衣机
class Washer():
    def wash(self):
        print('洗衣服')
        print(self)


haier = Washer()
print(haier)

haier.wash()