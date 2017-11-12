# -*- coding:utf-8 -*-
# 现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给 N 个变量?

p = (4, 5)
x, y = p
print(x, y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data

print(name,date)

_, shares1, price1, _ = data

print(shares1, price1)

# 如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。那么怎样才能从这个可迭代对象中解压出 N 个元素出来?

def avg(middle):
    return sum(middle)/len(middle)

def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

record  = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email , *phone_number = record

print(name, email, phone_number)
