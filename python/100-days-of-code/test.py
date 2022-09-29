# File for testing small sections of code that are not required as part of a project

list = [0, 1, 2, 3]
max = list[0]

for i in list:
    if i > max:
        max = i

num = 14     
while num > len(list)-1:
    num -= len(list)
print(list[num])