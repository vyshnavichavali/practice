# While
# If there is no certain number of iterations then we use while loop
# Req: Print 1 to 5 numbers
# State
count = 1

# Behaviour
while count <= 5:
    print(count)
    count += 1

# Req: print multiples of 5 upto specified limit
limit = int(input("Enter the limit: "))
count = 5
while count <= limit:
    print(count)
    count += 5

limit = int(input("Enter the limit: "))
count = 4
while count <= limit:
    print(count)
    count += 4

# simple password loop
password = 'secret'
while True:
    user_input = input("enter password:")
    if user_input == password:
        print("Access guarented")
        break
    else:
        print("Access Denied")



















