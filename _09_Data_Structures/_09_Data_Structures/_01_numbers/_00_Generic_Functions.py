'''
STATE    - Data types/structures/Objects
BEHAVIOR - Functions/Methods (Operators, DM, Loops)

Requirement:
===============
    - Operation : CRUD
    - State     : Datatypes/Datastructures
    - Behavior  : Functions/Methods
'''
# REQ: Print first 20 even numbers between 1 to 100
'''
Tasks:
=========
1. Numbers between 1 to 100
2. Even numbers
3. First 20 even
'''
# STATE
st = int(input("Enter start value : "))
end = int(input("Enter end value : "))

# BEHAVIOR 3

count = 0
for val in range(st, end+1):
    if val % 2 == 0:
        print("Value : ", val)
        count += 1
        if count == 20:
            break


''''''
'''

# DATA TYPES
numbers  - int float complex
boolean  - bool
String   - 'A'  '1'  

# DATA STRUCTURES
String ** : '100'  '193.4' 'hello' 'Madhu' 'Python' '74060900500'
List **
Tuple 
Dictionary **
Set

Collections module : NamedTuple OrderedDict DefaultDict FrozenSet Counter 
'''
'''
# Generic Functions
---------------------
print()  :  Prints the given value
input()  :  Receives input from end user keyboard
type()   :  Gives type of variable/value
id()     :  Gives address of the variable/value in integer format

Problem: Find solution for f(x) = 2x+1, when x = 10
         1.REQ              3.Behavior       2.State   
Solution:
            As given x = 10
            Given expression is f(x) = 2x + 1
            Substitute value 10 in x variable
           f(10) = 2(10)+1
                 = 20 + 1
                 = 21

                    STATE    : x = 10
                    BEHAVIOR : 2x + 1

print("----------------")
f(x) = 2x+1
f(f(x)) = 3x+2. 
Get output if x = 10

Answer:
--------
f(10) = 2(10)+1 = 21
print("----------------")
f(f(x)) = 3x+2
        = 3(21)+2
        = 63+2
        = 65
'''
