# Floor division
''' Rounds the result down to the nearest whole number
or integer, which is less than or equal to the normal division result '''
x = 10
y = 20
res = x//y
print("Floor Division is:", res)

print("-------------Floor Division of numbers-------------")
print("----Based on count------")
# 2 numbers
x = 10
y = 20
result = x // y
print("Floor Division is:", result)

print("----Based on type----")

# Both are positive
x = 10
y = 20
res = x // y
print("Floor Division is:", res)

# Both are negative
x = -3
y = -4
res = x // y
print("Floor Division is:", res)

# one positive and one negative
x = 3
y = -4
res = x // y
print("Floor Division is:", res)

# zero and positive number
x = 0
y = 20
res = x // y
print("Floor Division is:", res)

# positive number and zero
'''
x = 3
y = 0
res = x // y
print("Floor Division is:", res)'''

# Zero,Neg Number
'''
x = 0
y = -3
res = x // y
print("Floor Division is : ", res)'''

# Pos Number, Zero
'''
x = 3
y = 0
res = x // y
print("Floor Division is : ", res)'''

# Neg Number, Zero
# ZeroDivisionError
'''
x = -30
y = 0
res = x // y
print("Floor Division is : ", res)'''
print("-------Based on datatype------")

# Both Integers
x = 5
y = 10
res = x // y
print("Floor Division is : ", res)

# Both Float
x = 6.3
y = 2.4
res = x // y
print("Floor Division is : ", res)

# Int , Float
x = 20
y = 10.7
res = x // y
print("Floor Division is : ", res)

# Float, Int
x = 25.6
y = 1
res = x // y
print("Floor Division is : ", res)




