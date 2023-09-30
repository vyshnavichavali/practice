"""Functions: items(), keys(), values(), get() clear() """

dict = {'id': 10, 'name': 'vyshu'}
del dict['name']
print("Remaining details present: ", dict)

person = {'name': 'Alice', 'age': 28, 'gender': 'Female', 'city': 'New York'}
items = person.items()
print("items are:", items)

keys = person.keys()
print('keys are: ', keys)

values = person.values()
print('values are: ', values)

val = person.get('age', 0)
print(val)

person.clear()
print(person)

person = {'name': 'Alice',
          'age': 28,
          'gender': 'Female',
          'city': 'New York'}

for keys, values in person.items():
    print(f"{keys}: {values}")





