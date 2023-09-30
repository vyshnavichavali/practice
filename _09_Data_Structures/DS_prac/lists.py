# list-[]
# lists are mutable(we can change the data present in the list)and contains heterogenous datatypes and it is ordered
# Creating the list
"""
Methods: Which are followed by dot like append., extend.
Functions: Which are followed by braces like del()
"""

list1 = [1, 2, 3, "vyshu", 4.5]
print("Data present in list1 is:", list1)

# Methods: append(), extend(), insert(), pop(), remove()
# Function: del()
# Append: append takes single element
list1.append(2)
print("append one value:", list1)

a = (2, 0)
list1.append(a)
print("appending tuple to list:", list1)

b = [3, 4]
list1.append(b)
print("appending list to list:", list1)

c = {1: 'vyshu', 2: 'vn2'}
list1.append(c)
print("appending dict to list:", list1)

# Extend: Extend takes iterables
# list1.extend((2))
# print("Extend with one value:", list1)
g = [{1: 2}]
list1.extend(g)
print("Extending list with dict:", list1)

h = [4, 5]
list1.extend(h)
print("Extending the list:", list1)

i = (6, 7)
list1.extend(i)
print("Extending the list:", list1)

j = {1, 2}
list1.extend(j)
print("Extending the list:", list1)

k = {1: 2}  # only key will print
list1.extend(k)
print("Extending the list:", list1)

l = [[4, 5]]  # list
list1.extend(l)
print("Extending the list with list:", list1)

m = [(6, 7)]  # tuple
list1.extend(m)
print("Extending the list with tuple:", list1)

o = [{1, 2}]  # set
list1.extend(o)
print("Extending the list with set:", list1)

# pop syntax: list_name.pop(index)
# pop: pop the position of the element

list1.pop(7)
print("poping the element:", list1)

list1.pop(4)
print("list after poping:", list1)

list1.pop(-1)
print("list after poping:", list1)

# Remove: Removes the values from the list
list1.remove('vyshu')
print("removing the value:", list1)

list1.remove(1)
print("removing the value from the list:", list1)

list1.remove(1)
print("removing the value from the list:", list1)

# insert syntax: list_name.insert(index, element)
# insert: inserts the element from the list
list1.insert(1, 89)
print("Inserting element in the list", list1)

# del: deletes the element according to the index
del list1[2]
print("deleting element from the list:", list1)



