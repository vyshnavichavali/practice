print("-------Generic functions--------")
# print() id() type()
x = 10
print(x, id(x), type(x))
sal = 4.8
print(sal, id(sal), type(sal))

print("----------- int function ----------")
# int --> int()
x = 10.4
print("Before: ", x, type(x))
x = int(x)
print("After: ", x, type(x))

print("----------- float function ------------")
x = 10
print("Before: ", x, type(x))
x = float(x)
print("After: ", x, type(x))

print("----------- bool function -----------")
x = 0
print("Before: ", x, type(x))
x = bool(x)
print("After: ", x, type(x))

print("------------- string function --------------")
num = 123445
print("Before: ", num, type(num))
num = str(num)
print("After: ", num, type(num))

