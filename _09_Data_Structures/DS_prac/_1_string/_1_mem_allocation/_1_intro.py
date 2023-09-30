x = 10
str1 = "Hello"
print(str1)

ch = 'A'
print(ch)

ch = '1'
print(ch, type(ch))
# print("Addition: ", ch+2)  # can only concate str with str
print("Addition :", int(ch)+2)

ch = '1.6'
print(ch, type(ch))
print("Addition :", float(ch)+3.6)

ch = '#'
print(ch, type(ch))

print("--------type conversions----------")
x = 9
y = "3"
print("type of x and y: ", x, y, type(x), type(y))
print("converting str to int: ", x+int(y))

if type(x) == type(y):
    print("Additon :", x+y)
else:
    print("Addition is not possible")

x = 30
x = str(x)
print("String x:", x)


# my_string = 'He said, 'Hello!''
# error that we cant use single quote with single quote
my_string = 'He said, "Hello!"'
print(my_string)



