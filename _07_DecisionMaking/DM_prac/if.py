# 17 ==, <=,<,>,>=,!=,and , or, not, in, not in, is , is not, %, +, -, *
# REQ: Print if Customer given number is equal to 10 or not
'''
State: Customer given number
Behavior: Print it
            ==>  if  is equal to 10

Functional Analysis:
---------------------
 1. Customer will give number        : STATE
 2. Check if it is equal to 10   : Behavior
 3. If val == 10 ==> Print it

Technical Analysis:
--------------------
  1. STATE    :  Datatypes/Datastructures   : Customer given number    : int
  2. BEHAVIOR :  Operators, DM, Loops       : Check if it is equal to 10
                      ==     if

  Entity  :    Customer
  State   :    given number
  Behavior:    Print it if number is  == 10
 English :  if the given number is equal to 10 then print it
 Python  :  if       num                  ==     10:
                    print("")
'''
# state
val = int(input("Enter number: "))
# Behaviour
if val == 10:
    print("Given number is equal to 10: ", val)

# REQ: Print if Customer given number is greater than 10
'''
State: Customer given number
Behavior: Print it 
            ==>  if  is greater than 10

Functional Analysis:
---------------------
 1. Customer will give number        : STATE 
 2. Check if it is greater than 10   : Behavior
 3. If val > 10 ==> Print it 

Technical Analysis: 
--------------------
  1. STATE    :  Datatypes/Datastructures   : Customer given number    : int
  2. BEHAVIOR :  Operators, DM, Loops       : Check if it is greater than 10    
                      >     if 

  Entity  :    Customer         
  State   :    given number 
  Behavior:    Print it if number is  > 10
 English :  if the given number is greater than 10 then print it 
 Python  :  if       num                  >     10:
                    print("") 
'''

# state
val = int(input("Enter number: "))
# Behaviour
if val > 10:
    print("Given number is greater than 10: ", val)

# REQ: Print if Customer given number is less than 10
'''
State: Customer given number
Behavior: Print it 
            ==>  if  is less than 10

Functional Analysis:
---------------------
 1. Customer will give number        : STATE 
 2. Check if it is greater than 10   : Behavior
 3. If val < 10 ==> Print it 

Technical Analysis: 
--------------------
  1. STATE    :  Datatypes/Datastructures   : Customer given number    : int
  2. BEHAVIOR :  Operators, DM, Loops       : Check if it is less than 10    
                      <     if 

  Entity  :    Customer         
  State   :    given number 
  Behavior:    Print it if number is  < 10
 English :  if the given number is greater than 10 then print it 
 Python  :  if       num                  <     10:
                    print("") 
'''
# State
val = int(input("Enter number: "))
# Behavior
if val < 10:
    print("Given number is less than 10:", val)

# REQ: Print if Customer given number is greater than or equal to 10
'''
State: Customer given number
Behavior: Print it 
            ==>  if  is greater than or equal to 10

Functional Analysis:
---------------------
 1. Customer will give number        : STATE 
 2. Check if it is greater than or equal to 10   : Behavior
 3. If val >= 10 ==> Print it 

Technical Analysis: 
--------------------
  1. STATE    :  Datatypes/Datastructures   : Customer given number    : int
  2. BEHAVIOR :  Operators, DM, Loops       : Check if it is greater than or equal to 10    
                      >=     if 

  Entity  :    Customer         
  State   :    given number 
  Behavior:    Print it if number is  >= 10
 English :  if the given number is greater than 10 then print it 
 Python  :  if       num                  >=     10:
                    print("") 
'''
# State
val = int(input("Enter the number: "))
# Behaviour
if val >= 10:
    print("Given number is greater than or equal to 10:", val)

# REQ: Print if Customer given number is less than or equal to 10
'''
State: Customer given number
Behavior: Print it 
            ==>  if  is less than or equal to 10

Functional Analysis:
---------------------
 1. Customer will give number        : STATE 
 2. Check if it is less than or equal to 10   : Behavior
 3. If val <= 10 ==> Print it 

Technical Analysis: 
--------------------
  1. STATE    :  Datatypes/Datastructures   : Customer given number    : int
  2. BEHAVIOR :  Operators, DM, Loops       : Check if it is less than or equal to 10    
                      <=     if 

  Entity  :    Customer         
  State   :    given number 
  Behavior:    Print it if number is  <= 10
 English :  if the given number is less than or equal to 10 then print it 
 Python  :  if       num                  <=     10:
                    print("") 
'''

# State
val = int(input("Enter the number: "))

# Behaviour
if val <= 10:
    print("Given number is less than or equal to 10:", val)

# REQ: Print if Customer given number is not equal to 10
'''
State: Customer given number
Behavior: Print it 
            ==>  if  is not equal to 10

Functional Analysis:
---------------------
 1. Customer will give number        : STATE 
 2. Check if it is not equal to 10   : Behavior
 3. If val != 10 ==> Print it 

Technical Analysis: 
--------------------
  1. STATE    :  Datatypes/Datastructures   : Customer given number    : int
  2. BEHAVIOR :  Operators, DM, Loops       : Check if it is not equal to 10    
                      !=     if 

  Entity  :    Customer         
  State   :    given number 
  Behavior:    Print it if number is  != 10
 English :  if the given number is not equal to 10 then print it 
 Python  :  if       num                  !=     10:
                    print("") 
'''
# STATE
val = int(input("Enter the value:"))

# Behavior
if val != 10:
    print("Given number is not equal  to 10: ", val)


# REQ: Print if Customer given number is less than or equal to 10
'''
State: Customer given number
Behavior: Print it 
            ==>  if  is less than or equal to 10

Functional Analysis:
---------------------
 1. Customer will give number        : STATE 
 2. Check if it is less than or equal to 10   : Behavior
 3. if num <= 10 ==> Print it 

Technical Analysis: 
--------------------
  1. STATE    :  Datatypes/Datastructures   : Customer given number    : int
  2. BEHAVIOR :  Operators, DM, Loops       : Check if it is less than or equal to 10    
                 and, >=,<= if 

  Entity  :    Customer         
  State   :    given number 
  Behavior:    Print it if number is  <= 10
 English :  if the given number is less than or equal to 10 then print it 
 Python  :  if       num                  <=     10:
                    print("") 
'''

# State
val = int(input("Enter the number"))

# Behaviour
if val >= 5 and val <= 10:
    print("Given number is less than or equal to 10:", val)

num = int(input("Enter a number: "))  # Customer given number

# REQ: Check if the number is either greater than or equal to 5 or less than or equal to 10
'''
State: Customer given number
Behavior: Print it 
            ==>  if  is either greater than or equal to 5 or less than or equal to 10

Functional Analysis:
---------------------
 1. Customer will give number        : STATE 
 2. Check if it is less than or equal to 10   : Behavior
 3. if num >= 5 or num <= 10: ==> Print it 

Technical Analysis: 
--------------------
  1. STATE    :  Datatypes/Datastructures   : Customer given number    : int
  2. BEHAVIOR :  Operators, DM, Loops       : Check if it is either greater than or equal to 5 or less than or equal to 10   
                  or,>=,<=  if 

  Entity  :    Customer         
  State   :    given number 
  Behavior:    Print it if number is  >=5 or <= 10
 English :  if the given number is either greater than or equal to 5 or less than or equal to 10 then print it 
 Python  :  if     num >= 5 or num <= 10
                    print("") 
'''

# STATE
val = int(input("Enter the number"))

# Behaviour
if num >= 5 or num <= 10:
    print("The number is either greater than or equal to 5 or less than or equal to 10:", num)

# REQ: Check if the number is NOT greater than 10
'''
State: Customer given number
Behavior: Print it 
            ==>  if number is NOT greater than 10

Functional Analysis:
---------------------
 1. Customer will give number        : STATE 
 2. Check if it is NOT greater than 10   : Behavior
 3. if not (num > 10): ==> Print it 

Technical Analysis: 
--------------------
  1. STATE    :  Datatypes/Datastructures   : Customer given number    : int
  2. BEHAVIOR :  Operators, DM, Loops       : Check if it is either greater than or equal to 5 or less than or equal to 10   
                   not, >      if 

  Entity  :    Customer         
  State   :    given number 
  Behavior:    Print it if number is  not (val > 10):
English :  if the given number is NOT greater than 10 then print it 
Python  :  if not (val > 10):
                    print("") 
'''
# State
val = int(input("Enter the number: "))

# Behaviour
if not (val > 10):
    print("The number is less than or equal to 10: ", val)

# Whether the given value is in the list
# State
list = [1, 2, 3, 4]
val = 4
if val in list:
    print("The value is present in the list")

# If the given number is not in the list
# State
list = [1, 2, 3, 4]
val = 9
if val not in list:
    print("The given number is not in the list")

# REQ: print whether the both lists refers same object
# State
list1 = [1, 2, 3]
list2 = list1

# Behaviour
if list1 is list2:
    print("list1 and list2 refer to the same object")


# REQ: print whether x and y do not refers to same object
# State
list1 = [1, 2, 3]
list2 = [1, 2, 3]

# Behaviour
if list1 is not list2:
    print("list1 and list2 not refer to the same object")


# Req: Check whether the given number is even
# State
val = 10

# Behaviour
if val % 2 == 0:
    print("The number is even")

# Req: Check whether the sum is greater than 1 or not
# State
num1 = 5
num2 = 3
sum_result = num1 + num2

# Behaviour
if sum_result > 10:
    print("The sum is greater than 10")

# Req: Check whether the difference is less than 1 or not
# State
val1 = 15
val2 = 8
difference = val1 - val2

# Behaviour
if difference < 5:
    print("The difference is less than 5")

# Req: Check whether the product is 28
# State
val1 = 4
val2 = 7
product = val1 * val2

# Behaviour
if product == 28:
    print("The product is 28")





