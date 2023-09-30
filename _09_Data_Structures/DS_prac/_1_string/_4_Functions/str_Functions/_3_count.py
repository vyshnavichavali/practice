# count(): count how many times
# str occurs in string or in a substring of string
str1 = 'hello world hai'
print('------------- count() --------------')
print('count(): count how many times str occurs in string or in a substring of a string')
print('slicing: ', str1[0:4])
print("count of: o-> ", str1.count('o'))
print("count of: l-> ", str1.count('l'))
print("count of: d-> ", str1.count('d'))
print("count of: h-> ", str1.count('h'))

print("count of: l-> ", str1.count('l', 0, 4))
print("count of: h-> ", str1.count('h', 0, 7))
print("count of: o-> ", str1.count('o', 4, 9))
print("count of: o-> ", str1.count('o', 0, 5))
print("count of:  -> ", str1.count(' ', 0, 6))
print("count of:  -> ", str1.count(' ', 0, 12))
print("count of:  -> ", str1.count(' ', 0, 65))










