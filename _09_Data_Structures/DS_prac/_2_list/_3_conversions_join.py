'''
x = 10
li = list(x)
print('list: ', li)
'''
# Conversions
x = (10, 2, 3)
li = list(x)
print('list: ', li, type(li))

x = 10
print('To float: ', float(x), type(x))
x = 10.3
print("to int: ", int(x), type(x))
x = 0  # ***
print("to bool: ", bool(x), type(x))  # False <class 'int'>
x = -2  # ***
print("to bool: ", bool(x), type(x))  # True <class 'int'>
x = 1234  # ***
print('To str: ', str(x), type(x))  # 1234 <class 'int'>
x = str(x)
print('To str: ', x, type(x))  # 1234 <class 'str'>

str1 = 'Hello world'  # ***
print("Convert to list: ", list(str1), type(str1))
# ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'] <class 'str'>

list1 = [1, 3, 4, 5, 3, 4, 5]
# print("join on numbers: ", ''.join(list1))  #expected str instance, int found
print("list to string: ", list1, type(list1))
li = str(list1)
print("list to string: ", li, type(li))

list1 = ['1', '2', '3', '4', '5', '6']
num_str = ''.join(list1)
print(num_str, type(num_str))
num_str = ' '.join(list1)
print(num_str, type(num_str))
num_str = '*'.join(list1)
print(num_str, type(num_str))















