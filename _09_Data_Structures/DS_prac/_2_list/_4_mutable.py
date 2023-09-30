# string is immutable
msg = 'Hello'
print("Before string: ", msg)
msg = msg + 'world'
print("After string: ", msg)

# list is mutable
list1 = [34, 56, 76, 37, 27, 3, 77, 35]
'''       0   1   2   3   4   5  6   7
          35  35  36  37  38  39 40  41
'''
print('Before list: ', list1, id(list1), id(list1[0]), id(list1[1]),
      id(list1[2]))
list1[1] = 100  # replaces the existing value with new value
print('After list: ', list1, id(list1), id(list1[0]), id(list1[1]),
      id(list1[2]))
list1.insert(1, 43)  # shifts the value and inserts in the position we need
print('After list: ', list1, id(list1), id(list1[0]), id(list1[1]),
      id(list1[2]))

'''
output for above code
Before list:  [34, 56, 76, 37, 27, 3, 77, 35] 2342257053504 140733557765960 140733557766664 140733557767304
After list:  [34, 100, 76, 37, 27, 3, 77, 35] 2342257053504 140733557765960 140733557768072 140733557767304
After list:  [34, 43, 100, 76, 37, 27, 3, 77, 35] 2342257053504 140733557765960 140733557766248 140733557768072
'''









