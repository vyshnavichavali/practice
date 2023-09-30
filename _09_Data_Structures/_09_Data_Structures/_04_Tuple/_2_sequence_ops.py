tup1 = (1, 2, 3, 4, 5, 6, 7)

# Sequence operations
# ----------------------
# 1. Indexing # RETRIEVAL
print("Indexing : ", tup1[2])

# 2. Slicing
print("Slicing : ", tup1[0:2])

# 3. Adding
x = 10
y = 20
z = x + y

x = 10
x = x + 20

t1 = (1, 2, 3)
t2 = (4, 5, 6)
print("Tuple1 : ", t1)
print("Adding : ", t1 + t2)  # One time usage  (1,2,3,4,5,6)
t1 = t1 + t2
print("Tuple1 : ", t1)   # 2 or more times

print(10)

x = 10
print(x)

# 4. Multiplying
t1 = (1, 2, 3)
print("Mulitiply : ", t1*3)

# 5. Membership
t1 = (1, 2, 3, 4)
print("Membership : ", 1 in t1)
print("Length : ", len(t1))
print("Max : ", max(t1))
print("Min : ", min(t1))

#len() max() min()
