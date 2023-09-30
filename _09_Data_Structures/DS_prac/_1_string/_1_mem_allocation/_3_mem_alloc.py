x = 10
print(x, type(x), id(x))

msg = 'Hello world'

print("value is: ", msg)
print("print d: ", msg[10], msg[-1])
print("1st index: ", msg[1])
print("5th index: ", msg[5])
print("9th index: ", msg[9])
print("10th index: ", msg[-1])

x = 10
print("value of x: ", x)
x = 20
print("value of x: ", x)

msg = 'Hello world'
print("Message1 is: ", msg, id(msg))

msg = 'Python'
print("Message1 is: ", msg, id(msg))


x = 10
x = x+2
msg = 'hello'
print("Message2:", msg)
msg = msg + 'world'
print("Message2: ", msg)