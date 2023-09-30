# CRUD Operations

# 1. Create
lis1 = [3, 5, 7, 1, 8, 2, 9]

list1 = [1, 2, [3, 5, 6], (5, 4, 3), {1: 1, 2: 2, 3: 3}, {1, 2, 3, 4}]

# 2. Retrieve
print('list values1: ', list1)
print('list values2: ', list1[2][2])
print('list values3: ', list1[4])

# 3. Update
list1.insert(4, 5)  # shifts the value and inserts in the position we need
print("updated list: ", list1)
list1[1] = 300  # replaces the existing value with new value
print("updated list1: ", list1)

# 4. Delete
del list1[4]
print("After deletion list: ", list1)
del list1

# a = list(input("Enter list: "))
a = [1, 2, 3, 4, 5]
print(a)

# list comprehension
# By default we get a string format in list comprehension
# [1, 2, 3, 4]-->['[', '1', ',', '2', ',', '3', ',', '4', ']']
a1 = '123456'
print([int(x) for x in list(a1)])  # [1, 2, 3, 4, 5, 6]

a2 = (1, 2, 3, 4)
print([int(x) for x in list(a2)])  # [1, 2, 3, 4]

a3 = {1, 2, 3, 4}
print([str(x) for x in list(a3)])  # ['1', '2', '3', '4']

a4 = {1: 2, 3: 4, 4: 5}
print([int(x) for x in list(a4)])  # [1, 3, 4]


str1 = '[1,2,3,4]'
li = []
for val in str1:
    if val.isdigit():
        val = int(val)
        li.append(val)
print(li)

print([int(x) for x in list()])

list1 = list('1234')
print(list1)  # ['1', '2', '3', '4']
list1[0] = list1[1] = 5
print(list1)  # [5, 5, '3', '4']


