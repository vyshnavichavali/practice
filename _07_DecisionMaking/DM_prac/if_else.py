# ==, <=,<,>,>=,!=,and , or, not, in, not in, is , is not, %, +, -

# REQ: Print if Customer given number is equal to 10 or not
# state
val = int(input("Enter number: "))
# Behaviour
if val == 10:
    print("Given number is equal to 10: ", val)
else:
    print("Given number is not equal to 10:", val)

# REQ: Print if Customer given number is greater than 10
# state
val = int(input("Enter number: "))

# Behaviour
if val > 10:
    print("Given number is greater than 10: ", val)

else:
    print("Given number is not grater than 10:", val)

# REQ: Print if Customer given number is less than 10
# State
val = int(input("Enter number: "))
# Behavior
if val < 10:
    print("Given number is less than 10:", val)
else:
    print("Given number is not less than 10: ", val)

# REQ: Print if Customer given number is greater than or equal to 10
# State
val = int(input("Enter the number: "))
# Behaviour
if val >= 10:
    print("Given number is greater than or equal to 10:", val)
else:
    print("Given number is neither grater than nor equal to 10: ", val)

# REQ: Print if Customer given number is less than or equal to 10
# State
val = int(input("Enter the number: "))

# Behaviour
if val <= 10:
    print("Given number is less than or equal to 10:", val)
else:
    print("Given number is neither less than nor equal to 10:", val)

# REQ: Print if Customer given number is not equal to 10
# STATE
val = int(input("Enter the value:"))

# Behavior
if val != 10:
    print("Given number is not equal  to 10: ", val)
else:
    print("Given number is greater than or less than 10 but not equal to 10:", val)

# Req: check weather the student is pass or fail
# State
score = 85
is_passing = score >= 60 and score <= 100

if is_passing:
    print("You passed the exam.")
else:
    print("You did not pass the exam.")



# REQ: Check whether the number is between 0 and 30 or not
# STATE
val = 28

# Behaviour
if val > 30 or val < 0:
    print("Number is between 0 and 30")
else:
    print("Number is not between 0 and 30")

# REQ: Check whether the employee has permission or not
# State
has_permission = False

# Behaviour
if not has_permission:
    print("Access denied")
else:
    print("Access granted")


# Whether the given value is in the list
# State
list = [1, 2, 3, 4]
val = 4
if val in list:
    print("The value is present in the list")
else:
    print("The number is not present in the list")

# If the given number is not in the list
# State
list = [1, 2, 3, 4]
val = 9
if val not in list:
    print("The given number is not in the list")
else:
    print("The given number is present in the list")

# REQ: print whether the both lists refers same object
# State
list1 = [1, 2, 3]
list2 = list1

# Behaviour
if list1 is list2:
    print("list1 and list2 refer to the same object")
else:
    print("list1 and list2 not refers to the same object")

# REQ: print whether x and y do not refers to same object
#State
list1 = [1, 2, 3]
list2 = [1, 2, 3]

# Behaviour
if list1 is not list2:
    print("list1 and list2 not refer to the same object")
else:
    print("list1 and list2 refer to the same object")


# Req Check whether the given number is even or odd
#State
val = 10

# Behaviour
if val % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# Req: Check whether the sum is greater than 1 or not
#State
num1 = 5
num2 = 3
sum_result = num1 + num2

# Behaviour
if sum_result > 10:
    print("The sum is greater than 10")
else:
    print("The sum is not greater than 10")

# Req: Check whether the difference is less than 1 or not
# State
num1 = 15
num2 = 8
difference = num1 - num2

# Behaviour
if difference < 5:
    print("The difference is less than 5")
else:
    print("The difference is greater than or equal to 5")

# Req: Check whether the product is 28
# State
val1 = 4
val2 = 7
product = val1 * val2

# Behaviour
if product == 28:
    print("The product is 28")
else:
    print("The product is not 28")