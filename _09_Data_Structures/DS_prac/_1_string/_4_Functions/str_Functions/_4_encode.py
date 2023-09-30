# decode(): Decodes the string using the code registered for encoding
# strict(): It handles the error in the string like if there is any char in string that cannot be encoded

str1 = 'hello world'
str2 = str1.encode('UTF-8', 'strict')
print("------------decode()-----------")
print("decode(): Decode the string using the code registered for encoding..")
print("Encoded string: ", str2)
print("decoded string: ", str2.decode('UTF-8', 'strict'))

str1 = 'hello'
str2 = str1.encode()
print("Normal: ", str1)
print("encoded: ", str2)
print("Decoded:", str2.decode())







