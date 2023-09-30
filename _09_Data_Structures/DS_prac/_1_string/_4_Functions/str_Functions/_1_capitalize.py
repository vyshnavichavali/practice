"""
For a particular value
                    1. Print it
                    2. Assign to variable
                    3. Perform operation
"""
# sort()
# It changes the original list
list1 = [10, 60, 20, 40, 30, 50]
print("Before sort: ", list1)
list1.sort()
print("After sort: ", list1)

# sorted
# It does not changes the original list
list2 = [10, 54, 45, 85, 45, 48]
print("Before sorted:", list2)
list3 = sorted(list2)
print("After sorted: ", list2)


100  # Garbage collection

print(200)  # single time usage

x = 300  # multiple times
print("Value :", x)

'Hello World'  # Garbage collection

print(10)  # one time usage

x = 10
print("Value of x: ", x)  # multiple usage
print("x one more time: ", x)
x = 10 + 20  # Operation

# capitalize(): Returns a string with the first character as uppercase
# hello --> Hello
print("------------- capitalize() --------------")
print("capitalize() : capitalizes first letter of given input string")

str1 = 'hello'
print("Normal string: ", str1)  # hello
str1.capitalize()  # Hello   (No action here)
print("string after capitalize1: ", str1)  # hello
print("string after capitalize2: ", str1.capitalize())  # Hello (One time usage)
print("string after capitalize3: ", str1)   # hello

# Assigning to new variable
str2 = str1.capitalize()  # If we want both old and new values(hello, Hello)
print("string after capitalize4: ", str1)  # hello
print("string after capitalize5: ", str2)  # Hello

# Assigning to same variable

str1 = str1.capitalize()  # If we dont want ild value
print("string after capitalize4: ", str1)  # Hello

'''3 Ways'''
print("-------Way 1---------")
# current string should be used as is, new string used "one time"
str1 = 'hello'
print("string: ", str1)
print("capitalize: ", str1.capitalize())  # print(10)
print("String: ", str1)

# current string should be used as is, new string used in "multiple places"
x = 10
y = x ** 3
print("-----------Way 2------------")
str1 = 'hello'          # x = 10
print("string: ", str1)
str2 = str1.capitalize()   # y = x + 5
print("string: ", str1)
print("string: ", str2)   # print(x)

# current string should get modified
print("------Way 3------")
x = 10
x = x ** 2
str1 = 'hello'
print("string: ", str1)
str1 = str1.capitalize()  # Hello
print("string: ", str1)













