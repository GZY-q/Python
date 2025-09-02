class Washer():
    def __init__(self):
        self.width = 500
        self.height = 800
    def print_info(self):
        print(f'洗衣机的宽度是{self.width},高度是{self.height}')

haier1 = Washer()
haier1.print_info()


class Washer():
    def __init__(self):
        self.width = 500
        self.height = 800

    def print_info(self):
        print(f'洗衣服的宽度是{self.width}')
        print(f'洗衣服的高度是{self.height}')


haier1 = Washer()
haier1.print_info()


