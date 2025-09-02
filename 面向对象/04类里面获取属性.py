class Washer():
    def wash(self):
        print('我会洗衣服')

    def print_info(self):
        print(self.width)  # self.属性名


haier1 = Washer()
# 添加属性，对象名字.属性名 = 值
# 属性是自己创建的，对象是前面定义的
haier1.width = 400
haier1.height = 300

# 获取属性，对象名.属性名
print(f'haier1洗衣机的宽度是{haier1.width}')
print(f'haier1洗衣机的高度是{haier1.height}')

