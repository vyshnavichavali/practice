# Sequence Operations: Indexing, Slicing, Adding, Multiplying, Membership, len, min, max
msg = 'Hello World'
# Indexing
print("---------- Indexing----------")
print("4th index: ", msg[4])
print("5th index: ", msg[5])
print("6th index: ", msg[6])
print("7th index: ", msg[7])
print("8th index: ", msg[8])
print("9th index: ", msg[9])
print("10th index: ", msg[-1])


# Slicing
print("---------Slicing--------")
msg = 'python programming'
print("0 to 5: ", msg[0:5])
print("2 to 5: ", msg[2:5])
print("3 to 7: ", msg[3:7])
print("1 to 10: ", msg[1:10])
print("-9 to 5: ", msg[-9:5])  # no output
print("-9 to -5: ", msg[-9:-5])


# Adding
print("--------Adding-----------")
str1 = 'Hello'
str2 = 'world'
print("Addition is: ", str2+str1)
print("Addition is: ", str1 + ' ' + str2)


str1 = 'python'
str2 = 'program'
print("Addition: ", str1 + str2)
print("Addition: ", str2 + str1)


# Multiplying
print("-------- Multiplying --------")
str1 = 'piligrim'
print("Multiplication: ", str1*2)


# Membership
print("------- Membership --------")
print("H: ", 'H' in 'Hello')
print("L: ", 'L' in 'Hello')
print("ll: ", 'll' in 'Hello')
print("p: ", 'll' in 'python')
msg = 'Python'
print('H' in msg)
print('L' in msg)


print("------ length -------")
# length()
print("Length of string: ", len(msg))
# max()
print("max of string: ", max(msg))
# min()
print("min of string: ", min(msg))


msg = 'Welcome to python programming language'
print(msg)
print("---- String with for loop ----")
for char in msg:
    print(char)

print("---- String with for loop1----")
for char in msg[11:18]:
    print(char)

print("---- String with for loop2----")
for char in msg[-1::]:
    print(char)  # O/P ->e

print("---- String with for loop2----")
for char in msg[::-1]:
    print(char)  # O/P -> egaugnal gnimmargorp ------- emoclew


chars = ['P', 'H']
for char in chars:
    if char in 'HELLO PYTHON':
        print("TRUE")





