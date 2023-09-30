'''
REQ: 1.CRUD : create Retrieve update delete
     2.STATE: (Data types, Data structures)
     3.BEHAVIOUR: (Operators, DM, Loops)
'''
eid = 10
sal = 10.5
is_bool = True
ename = 'vyshu'

e_ids = [14, 45, 34, 35, 65, 34, 23, 42, 53]
#        0    1   2   3   4   5   6   7   8
print("list data structure: ", e_ids)

# order = [4353, 4345, 5675, 6786, 5667, 5677]
# list properties
'''
list properties:
===============
1. Follows indexing mechanism while storing elements(Sequence)
2. List is mutable
3. List allows duplicate elements
4. Maintains insertion order wrt Memory
5. List will allow both Homogeneous and Heterogeneous data
'''

# 1. Follow indexing mechanism
list1 = [21, 34, 56, 23, 34]
#        0    1   2   3   4

print("List: ", list1)
print("List: ", list1[1])  # Indexing
print('list:', list1[0:6])  # Slicing

# 2. List is mutable
print("------list is mutable-------")  # create,Insert, Update, Delete ops

list1 = [35, 34, 76, 67, 34, 56]  # create
print("Before list: ", list1)
list1[2] = 20  # update
print("After update:", list1)
list1.insert(1, 10)
print("After insert operation: ", list1)
del list1[3]  # delete
print("After deletion: ", list1)
del list1

# 3. list will allow both homogeneous and heterogeneous data
# homo
print('--------Homogeneous------------')
list1 = [3, 4, 5, 3, 6]
print("Integers in list: ", list1)

list1 = [3.4, 1.6, 2.5, 3.6, 5.6]
print('Float in list: ', list1)

list1 = [True, False, True, True, False]
print('Boolean in list: ', list1)


'''
| 1 2 3 |
| 4 5 6 |
| 7 8 9 |     M[3][1] = 7

[1, 2, 3]
[4, 5, 6]
[7, 8, 9]     M[2][3] = 6 
'''

list1 = ['hello', 'python', 'good', 'bad']
print("string in list: ", list1)

print('index value: ', list1[1])
print('index value: ', list1[1][2])
print('index value: ', list1[2][3])

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Index value: ", list1[2][2])
print("Index value: ", list1[2])
print("Index value: ", list1[1][0])

list1 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print("list of tuples: ", list1)
print("list of tuples: ", list1[1])
print("list of tuples: ", list1[1][0])
print("list of tuples: ", list1[0][2])

list1 = [{1: 1, 2: 2}, {'id': 100, 'name': 'vyshu'}]
print('list of dicts: ', list1)
print('list of dicts: ', list1[1]['name'])

list1 = [{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}]
print('list of sets: ', list1)
# print('list of sets: ', list1[0][1]) sets does not have indexing mechanism
# print('list of sets: ', list1[1][3])

# Heterogeneous Data
list1 = [100, 'vyshu', 14.5, False, [1, 2, 3, 4], (1, 2, 3, 4), {1: 2, 2: 3}, {1, 2, 3, 4}]
print("list with heterogeneous data: ", list1)
print("list with heterogeneous data: ", list1[4][3])

list2 = [1, 2.5, False]

# 4. list allows duplicate elements
list1 = [10, 10, 10, 20, 20]
print("duplicates in list: ", list1)

# 5. lists maintains insertion order
list1 = [1, 2, 3, 4, 5]
print("Insertion order: ", list1)













