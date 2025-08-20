"""
语法
条件城成立的表达式if 条件else 条件不成立执行的表达式
"""
a = 1
b = 2

c = a if a > b else b
print(c)

# 需求：有两个变量，比较大小，如果变量1大于变量2执行；否则 变量2-变量1
aa = 10
bb = 6
cc = aa - bb if aa > bb else bb - aa
print(cc)