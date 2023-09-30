# Immutability: Once content is created use as is or delete it but we cant modify it
"""
Immutable: All Datatypes : int, float, boolean, string, tuple
Mutable: list, dict, set
"""
x = 10
print("Value: ", x, id(x))

x = 20
print("Value: ", x, id(x))

print('-----------------------------')

msg = 'Hello'
print("Message: ", msg, id(msg))

msg = "world"
print("Message: ", msg, id(msg))

print('-----------------------------')

msg = 'Hello'
print("Message: ", msg, id(msg))
msg = msg+'world'
print("Message: ", msg, id(msg))

print('-----------------------------')

x = 10
x = 20
print("value is: ", x)
x = x+20
print("value is: ", x)

'''
Mutable:
--------
List,dict, set
'''
msg = "Hello"
print("Before: ", msg)
msg = msg + 'Welcome'
print("After: ", msg)

x = 10
print("First: ", x)
x = 20
print("second: ", x)
print("-------------------------")
x = 10
print(x)
x = x + 10
print(x)
print('--------------------------')
msg = 'Hello'
print("Message: ", msg)
msg = 'world'
print("Message: ", msg)
print("--------------------------")
msg = 'Hello'
print("Message: ", msg)
msg = msg + 'world'
print("Message: ", msg)

print("----------------------------")
msg = 'Hello world'
msg = msg.replace('H', 'j')  # jello world
print(msg)













