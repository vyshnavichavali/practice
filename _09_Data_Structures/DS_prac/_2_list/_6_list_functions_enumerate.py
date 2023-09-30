# list functions: append, extend, insert, pop, remove, del
# count, index , reverse, sort, copy

# append: appends a value at the end of the list
list1 = [1, 2, 3, 4, 6]
print("Before append: ", list1)
list1.append(10)
print("After append: ", list1)
list1.append(10.4)
print("After append: ", list1)
list1.append([1, 2, 3])
print("After append1: ", list1)
list1.append((1, 2, 4))
print("After append2: ", list1)
list1.append({1: 1, 2: 2})
print("After append3: ", list1)
list1.append('shush')
print("After append4: ", list1)
list1.append({1, 2})
print("After append5: ", list1)
list1.append(True)
print("After append6: ", list1)

# enumerate: Which gives the count and value both
# count starts from 0
for ind, value in enumerate(list1):
    print(ind, '---->', value)

print("After append: ", list1)

list1 = [1, 2, 3]
list1.append(5)
list1.append({1: 1, 2: 2})

list1 = [1, 2, 3]
print("Before list: ", list1)
list1.append([4, 5, 6])
print("After list: ", list1)

# 2extend: only sequence str, list, tuple
#          list1.extend(seq)  appends the contents of seq to list
list1 = [3, 4, 2, 4]
list2 = [3, 6, 2, 6]
# list1 = list1+list2  # [3, 4, 2, 4, 3, 6, 2, 6]

list1 = [1, 2, 3, 4, 5, 6]
# list1.extend(10)  ERROR
list1.extend([1, 2])
print("extended list: ", list1)
list1.extend((3, 4))
print("extended list: ", list1)
list1.extend({5, 6})
print("extended list: ", list1)
list1.extend({1: 1, 2: 3})
print("extended list: ", list1)
list1.extend("Helloworld")
print("extended list: ", list1)

# append   vs    extend
# anyobject      sequence
list1 = [1, 2, 3]
list1.append([1, 2])
list1.extend([1, 2])
print('list after append and extend: ', list1)

# 3. pop  # list.pop(obj=list[-1]) Removes and returns last obj or obj from list
list1 = [4, 5, 3, 6, 1, 0]
print('Before pop: ', list1)
list1.pop()  # By default pops the last element
print('After pop: ', list1)
list1.pop(-1)
print('After pop: ', list1)
list1.pop(1)
print('After pop: ', list1)

rem_val = list1.pop(0)
print('popped element: ', rem_val)
print('After pop: ', list1)

# 4. remove
# list.remove(obj) removes object from list

li1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Before remove operation: ", li1)
# li1.remove() # ERROR
li1.remove(1)
print("After remove operation:", li1)

li = [34, 56, 12, 77, 12, 21, 89]
print('Before remove operation: ', li)
# li.remove(12)
li.pop(4)
print('After pop operation: ', li)

# 5. list.insert(index, obj) inserts object obj into the list at offset index
li = [1, 2, 3, 4, 5]
print('Before index: ', li)
li[0] = 10  # [10, 2, 3, 4, 5]  Replace the value in index
print('After index: ', li)
li.insert(2, 9)  # [10, 2, 9, 3, 4, 5] insert the value in particular index
print('After insert: ', li)
li.insert(0, 8)
print('After insert: ', li)

# 6. count: list.count(obj) Returns count of how many times obj occurs in list
li1 = [1, 2, 3, 4, 2, 1, 2, 3, 4, 4, 5, 6, 5]
obj_count = li1.count(2)
print('count of 2 is: ', obj_count)










