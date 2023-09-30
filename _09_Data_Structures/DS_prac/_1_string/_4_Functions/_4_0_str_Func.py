'''
print() id() type() input()
int() float() bool() str()

'''

# State
marks = 15

# Behaviour
if marks >= 35:
    print("Pass")
else:
    print("Fail")

# String Methods ---> capitalize(), center(), count(), encode(), decode(), isalnum()
# isalpha(), isdigit(), isspace(), islower(), isupper()
# String Functions ----> len()
'''
1.capitalize(): 'hello'-->'Hello'
Only first letter will be capitalized
If input is 'Hello'--> 'Hello'
If input is 'hello'--> 'Hello'
'''
print("----------1.capitalize() -----------")
str1 = 'hello'
print("Normal string: ", str1)
str1.capitalize()
print("String after capitalize1: ", str1)

# one time use
print("String after capitalize2: ", str1.capitalize())
print("String after capitalize3: ", str1)

# for reuse
str2 = str1.capitalize()
print("String after capitalize4: ", str1, str2)

# 3 Ways
print("---------- Way 1 ----------")
# REQ 1: Current string should be used as is, new string "one time"
str1 = 'hello'
print("String Before capitalize: ", str1)
print("string after capitalize: ", str1.capitalize())  # one time usage
print("string: ", str1)

# REQ 2: current string should be used as is, new string used in multiple ways
str1 = 'hello'
print("Before capitalize: ", str1)
str2 = str1.capitalize()  # can be used multiple times
print("After capitalize: ", str2)
print("original string: ", str1)

# REQ 3: current should get modified
str1 = 'hello'
print("Before: ", str1)
str1 = str1.capitalize()
print("After capitalize: ", str1)

# 1st: New string: one time usage
str1 = 'hello'
print("string1: ", str1)
print("string2: ", str1.capitalize())  # one time usage
print("string3: ", str1)

# 2nd: Both old, new strings in multiple places
str1 = 'hello'
str2 = str1.capitalize()
print("old string: ", str1)
print("new string: ", str2)

# 3rd: old string no need to use
str1 = 'hello'
str1 = str1.capitalize()
print("string: ", str1)

# 2. center(): Returns the space-padded string with the original string centerd to a total width of columns
str = '2. center()'
print(str.center(50, '-'))
print("Center(): Returns the space-padded string with the original string centered to a total width of columns")
str1 = 'hello world'
print("Normal string: ", str1)
print("string after center function with width 24 and fillchar with $: ", str1.center(24, '$'))
print("string after center function with width 30 and fillchar with -: ", str1.center(30, '-'))

# count(): counts how many times char occurs in a string or in a substring of a string
str = '3. count()'
print(str.center(50, '-'))
print("count(): counts how many times th char occurs in a string or in a substring of a string")
str1 = 'hello world'
print("Normal string: ", str1)
print("count how many number of l's present the string: ", str1.count('l'))
print("count how many number of l's present the string: ", str1.count('l', 0, 5))
print("number of e's in the string: ", str1.count('e'))
print("number of e's in the string: ", str1.count('e', 6, 8))

# 4. decode(): Decodes the string using the code registered with encode
# strict: It handles the error in the string like if there is any char in the string that cannot be encoded
str1 = 'hello world'
str2 = str1.encode('UTF-8', 'strict')
print("-------------4. encode()-----------")
print("decode(): Decodes the string using the code registered with encode")
print("Encoded string: ", str2)
print("Decoded string: ", str2.decode('UTF-8', 'strict'))

# 5. encode(): Returns the encoded version of the string
str1 = 'hello world'
print("-------------------5. encode()------------------")
print("Encode: Returns the encoded version of the string")

print("normal string: ", str1)
print("Encoded string: ", str1.encode('UTF-8', 'strict'))

# 6. isalnum(): returns true if the string is alphanumeric
str1 = 'abdomen68780'
str2 = 'shush'
str3 = 'ngirejg\tkfwkkm'
str4 = 'hello world'
print('---------------- 6.isalnum() ----------------')
print('isalnum: returns true if string is alphanumeric')
print("abdomen68780 is alphanumeric: ", str1.isalnum())
print("shush is alphanumeric: ", str2.isalnum())
print("ngirejg\tkfwkkm is alphanumeric: ", str3.isalnum())
print("hello world is alphanumeric: ", str4.isalnum())

# 7. isalpha(): Returns true if all substrings are alphabets
str1 = 'vyshu'
str2 = 'hello8763'
print("---------------7. ialpha---------------")
print("alpha(): Returns true if the all substrings are alphabets")
print("vyshu contains alphabets: ", str1.isalpha())
print("hello863 contains alphabets: ", str2.isalpha())

# 8.isdigit(): Returns true if all characters in the strings are numbers
# It accepts the decimals
str1 = '1446541568'
str2 = '658631564eqrq'
print("--------------8. isdigit()------------")
print("isdigit1(): returns true if all characters in the string are numbers")
print("1446541568 contains numbers: ", str1.isdigit())
print("658631564eqrq contains numbers: ", str2.isdigit())

# 9. islower(): Returns true if all characters are in lowercase
str1 = 'vyshu'
str2 = 'Vyshu'
print("--------------9. islower()-------------")
print("islower(): Returns true if all the characters are in lowercase")
print("vyshu is in lowercase: ", str1.islower())
print("Vyshu is in lowercase: ", str2.islower())


# 10. isupper(): Returns true if chars in the string in uppercase
str1 = 'VYSHU'
str2 = 'knkrre'
print("--------------10.isupper()-----------------")
print("isupper(): Returns True if the chars in the string in uppercase")
print("VYSHU is in uppercase: ", str1.isupper())
print("knkree is in uppercase: ", str2.isupper())


# 11. isspace(): Returns true if all the chars in the string have whitespaces
str1 = 'hello world'
str2 = 'hello\tworld'
str3 = '  '
print("-------------11. isspace()------------")
print("isspace(): Returns true if the string contains the whitespaces ")
print("hello world contains spaces: ", str1.isspace())
print("hello\tworld contains spaces: ", str2.isspace())
print("   contains spaces: ", str3.isspace())

# 12.join(): joins the strings with mentioned seperator
sep = '_'
str1 = 'welcome to python'
print("-----------------12. join()---------------")
print("join(): joins the chars in the string with mentioned seperator")
print("join welcome to python with '-': ", sep.join(str1))

# 13.len(): Returns the length of the string
str1 = 'rghrigjrfr'
str2 = 'efkjwijeeeeeeeee'
print("-----------------13.len()--------------")
print("len(): Returns the length of the string")
print("Length of rghrigjrfr is: ", len(str1))
print("Length of efkjwijeeeeeeeee is: ", len(str2))

# lower(), strip(), lstrip(),
# 14. lower(): converts string to all lowercase characters
str2 = 'heLLo woRld'
print("----------------14. lower()-----------------")
print("lower(): Converts string to all lowercase characters")
print("Asha in lower characters is: ", "Asha".lower())
print("heLLo woRld in lower characters is: ", str2.lower())


# 15. lstrip(): removes mentioned char (left)
str1 = 'The dress looks fab'
str2 = '***Wow! what a great move**'
print("--------------15. lstrip()--------------")
print('lstrip(): removes mentioned char     (left)')
print("lstrip of ' ' in the dress looks fab: ", str1.lstrip(' '))
print("lstrip of * in ***Wow! what a great move**: ", str1.lstrip("*"))


# 16.strip(): performs both lstrip() and rstrip() on string.
str5 = ' The dress looks fab '
str6 = '***Wow! what a ** great move**'
print("--------------16. strip()-------------------")
print('strip(): performs both lstrp() and rstrip() on string')
print("strip of ' ' in the dress looks fab: ", str5.strip(''))
print("strip of * in ***Wow! what a ** great move**: ", str6.strip('8'))


















