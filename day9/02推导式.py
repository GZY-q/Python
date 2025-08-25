# dict1 = {i: i**2 for i in range(1, 5)}
# #字典key是1-5数字，value是数字的2次方
# print(dict1)  # {1: 1, 2: 4, 3: 9, 4: 16}


counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}

# 需求：提取上述电脑数量大于等于200的字典数据
count1 = {key: value for key, value in counts.items() if value >= 200}
print(count1)  # {'MBP': 268, 'DELL': 201}
# 集合有去重功能
list1 = [1, 1, 3]
set1 = {i ** 2 for i in list1}
print(set1)
