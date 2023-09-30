msg = 'hello world '
# 01234567810 Indexing mechanism
print("-----message1-------", msg)

msg2 = "Python Programming"
print("-----message2----", msg2)

'''
Operations on sequence:
-----------------------
Indexing 
Slicing
Adding
Multiplying
Checking for Membership
len() min() max()
'''

msg = 'hello world'
print("Messagge is: ", msg)

# Indexing
print("1st index of msg: ", msg[1])
print("last index of msg:", msg[-1])
print("4th index of msg:", msg[4])

# Slicing start(index) stop(position) step(diff) str[start:stop:step]
# sequence[start   :stop    :step]
#          indexing:position:diff
msg = 'hello world'
'''
                       -9-8-7-6-5-4-3-2-1     : Negative Indexing
                    H e l l o   w o r l d
                    0 1 2 3 4 5 6 7 8 9 10    : Indexing
                    1 2 3 4 5 6 7 8 9 10 11   : Position
'''

print("Slicing positive:", msg[0:4])  # 0 index 4 position
print("Slicing positive:", msg[6:11])  # print from index 6 to positoin 11
print("Slicing Negative:", msg[-6:-1])
print("Slicing with start stop step:", msg[0:9:3])  # o/p:hlw  I/N:hello world
print("Slicing without any positions: ", msg[::])  # o/p:hello world  I/N:hello world


# Adding Concatination
str1 = 'Hello'
str2 = 'world'
print("Entire string: ", str1+str2)

final_message = " Welcome to " + msg
print("Concatenation:", final_message)  # O/P Welcome to hello world



# Multiplying
print("Multiplication : ", msg*4)  # O/P hello worldhello worldhello worldhello world
print("Multiplication :", final_message * 4)  # O/P Welcome to hello world Welcome to hello world Welcome to hello world Welcome to hello world


# Checking For Membership (in, not in) True or false will be the output
print("----Membership----: ", "hello" in msg)  # O/P True
print("----Membership----: ", "o" in msg)  # O/P True
print("----Membership----: ", "k" in msg)  # O/P False


print("----Membership----: ", "k" not in msg)  # O/P True

# max()
msg = 'hello world'
print("Max value in string: ", max(msg))  # O/P -> w
print("Max value in string: ", max('abcd'))  # O/P -> d
print("Max value in string: ", max('ABCD'))  # O/P -> D
print("Max value in string  : ", max('ABDFSDfdsasdas'))  # O/P -> s
print("Max value in string  : ", max('abfd212rd'))  # O/P -> r
print("Max value in string  : ", max('@$##@15454$#!%'))  # O/P -> @
print("Max value in string  : ", max('1234213e'))  # O/P -> e


# min()
str1 = 'Python'
print("Min value in string: ", min(str1))  # O/P -> P
print("Min value in string: ", min('jhuhg4567%$^&*'))  # O/P -> $






















