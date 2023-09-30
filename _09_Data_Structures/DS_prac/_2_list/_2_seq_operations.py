list1 = [23, 4, 545, 34, 23, 34]
print('list: ', list1)

# 1. Sequence operations
print("------------1. Indexing-----------")
'''
    [34, 35, 33, 87, 45, 67, 47]
      0   1   2   3   4   5   6
'''
print("list1 indexing: ", list1[3])
print("list1 indexing: ", list[4])

print("-------------2. Slicing-------------")
# list1 = [23, 4, 545, 34, 23, 34]
print("list Slicing: ", list1[0:4])
print("list Slicing: ", list1[0:4:2])
print("list Slicing: ", list1[::-1])  # Reverse of list1
print("list Slicing: ", list1[0:-1:2])
print("list Slicing: ", list1[-1::])  # 34
print("list Slicing: ", list1[::1])
print("list Slicing: ", list1[::2])
print("list Slicing: ", list1[::])  # list as it is will be printed

print("-------------3. Adding-------------")
print("Adding two lists:", [2, 3, 4]+[4, 5, 6])  # concatenation
list1 = [3, 4, 5]
list2 = [6, 7, 8]
print("Adding two lists:", list1+list2)  # concatenation

print("--------------4. Multiplying-----------")
print("Multiplying 2 lists: ", [4, 5, 6, 4] * 4)  # [4, 5, 6, 4, 4, 5, 6, 4, 4, 5, 6, 4, 4, 5, 6, 4]
list1 = [3, 4, 3, 4]
num = 2
print("Multiplying 2 lists: ", list1*num)  # [3, 4, 3, 4, 3, 4, 3, 4]

print("------------5. Membership(in, not in)---------------")
# Returns True or False
print('check whether the 3 is in list1 or not: ', 3 in list1)
print('check the 4 is not in list1: ', 4 not in list1)

print("--------------6. length---------------------")
list1 = [3, 56, 3, 4, 34, 45, 56]
list2 = [45, 34, 34, 23, 6, 34, 56, 45, 500]
print('check length of the list: ', len(list1))
print('check length of the list: ', len(list2))

print("----------------7. max-----------------")
print("Get max from the list: ", max(list1))
print("Get max from the list: ", max(list2))

print("-----------------8.min-----------------")
print("Get min from the list: ", min(list1))
print("Get min from the list: ", min(list2))



