from pandas import Series

my_list = [100,200,300,400]

new_list=[]

for val in my_list:
    new_list.append(val/10)

print(my_list)

print(new_list)