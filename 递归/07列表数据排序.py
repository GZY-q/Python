students =[
    {'name':'tom','age':20},
    {'name':'john','age':30},
    {'name':'lili','age':40}
]


students.sort(key=lambda x:x['name'])
print(students)