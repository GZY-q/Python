name_list = ['tom', 'lily', 'john']
name_list.append('bob')

print(name_list)#['tom', 'lily', 'john', 'bob']


#逐一追加
name_list = ['tom', 'lily', 'john']
name_list.extend('bob')

print(name_list)#['tom', 'lily', 'john', 'b', 'o', 'b']


#指定追加
name_list = ['tom', 'lily', 'john']
name_list.insert(1,'bob')

print(name_list)#['tom', 'bob', 'lily', 'john']