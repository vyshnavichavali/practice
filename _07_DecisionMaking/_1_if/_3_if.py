x = 12  # Hardcoding manner
print(x, type(x))

'''
# to handle string
x = input("Enter number : ")  # Dynamic way of giving input value "12"
print(x, type(x))
'''
# to handle integer


# REQ: If given number is greater than or equal to 10, then print "Two digit number"

# STATE
num = int(input("Enter number : "))  # Dynamic way of giving input value  int("12")
# BEHAVIOR
if num >= 10:  # x > 9
    print("Two digit number")

print("-----End of program------")

# REQ: Check whether given number is 2 digit or not

num = int(input("Enter number : "))

if num >= 10:
    print("Two Digit Number")
else:
    print("Not a 2 digit")






# conditions:
# True   ==>   True, nonzero, nonNone
# False  ==>   False, zero, None

if 10 > 5:
    print("Value is smaller")

if 10 % 2:
    print("Division result is 0")

if 10+20:
    print("Addition is 30")

if True and True:
    print("Logical and True 1")

if 10 > 2 and 10 % 2 == 0:
    print("Logical and True 2")


if False or True:
    print("Logical or True")



if 10>2:
    print("Line1")
    print("Line2")
    print("Line3")
    print("Line4")
    print("Line5")
    print("Line6")
    print("Line7")
print("End of program")


if type(10) == float:  # <class int> --> nonzero
    print("Type is integer")

'''
one condition : if 
two conditions : if else
three conditions : if elif else
four conditions : if elif elif else
'''

is_present = False
if not is_present:
    print("Please attend the class !")

# job
#with sal 3L, without sal(Internship)
'''
Internship employee:
---------------------
emp_id - 12345
name  - 'Madhu Nettem'
company - 'ORACLE'
sal - None  # Not Applicable NA  null

Contract employee:
----------------
emp_id - 12345
name  - 'Madhu Nettem'
company - 'ORACLE'
sal - 12000 
is_perm = False
gratuity = None
'''

if 10 < 20 and 5 > 1:
    print("Yes the values are greater")

if 10+20 and 31-30:
    print("Logically executed")

if 10-10:
    print("Assighment is completed")

x = {1, 2, 3}

# If given value doesnt exit in set, print : Value doesnot exist

val = int(input("Enter value10 : "))

if not val in x:
    print("Value doesnot exist")
