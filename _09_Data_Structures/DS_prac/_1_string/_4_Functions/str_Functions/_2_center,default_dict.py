# center(): Returns a space-padded string with the original string centered
# to a total of width columns
print("------------center()-----------")
print("center(): returns center padded string with mentioned length")

str1 = 'hello world'
str2 = 'hello world welcome'
print("Normal string:", str1)
print("length after padding: ", len(str1.center(28, '$')))
print("string after center function with width 28 & fillchar as $: ", str1.center(28, '$'))
print("string after center function with width 28 & fillchar as ^: ", str1.center(28, '^'))
print("string after center function with width : ", str1.center(24))
print("----------------------------------------------------------------------------------")


from collections import defaultdict
# Defining the dict and passing lambda as default_factory argument
d = defaultdict(str)
d['a'] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])
print(d["d"])

from collections import defaultdict  # importing the defaultdict
d = defaultdict(lambda: 5)
d['apple'] = 1
d['banana'] = 2

print(d['apple'])
print(d['orange'])



