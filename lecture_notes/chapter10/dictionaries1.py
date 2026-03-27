# dictionaries1.py

# TODO 1: Make an empty dictionary called age, then print it and print its
# length.
age = {} # empty dictionary
print(age)
print(len(age))

# TODO 2: Re-make the age dictionary, and this time add the following as
# key:value pairs:
# - Marge is 34
# - Homer is 36
# - Bart is 10
#
# Then print the dictionary and its length.
age = {'Marge':34, 'Homer':36, 'Bart':10}
print(age)
print(len(age))

# TODO 3: Print Marge, Homer's, and Bart's ages. What if you try to print Lisa's age?
print(age['Marge'])
print(age['Homer'])
# print(age['Maggie'])

# TODO 4: Add Lisa's age (she's 8) to the dictionary. The other names and ages
# should stay the same.
age['Lisa'] = 8
print(age)
print(age['Lisa'])

# TODO 5: Increase Marge's age as follows: set it to 35, and then increase it by
# 1 using +=. Print the dictionary.
# {'Marge': 34, 'Homer': 36, 'Bart': 10}
age['Marge'] = 35
age['Marge'] += 1
print(age)


# TODO 6: Young Homer, who is 12, shows up. He has exactly the same name as the
# current Homer. What happens if you add the young Homer to the dictionary?
# Print the result.
# {'Marge': 36, 'Homer': 36, 'Bart': 10, 'Lisa': 8}
# age['Young Homer'] = 12
# print(age)


# TODO 7: Print just the names of the dictionary.
print(age.keys())

# TODO 8: Print just the ages of the dictionary.
print(age.values())

# TODO 9: Print the key:value pairs of the dictionary as list of pairs.
print(age.items())

# TODO 10: How an you test if Marge is a name in the dictionary? What about Maggie?
print('Marge' in age.keys()) # slow
print('Marge' in age) # fast
print('Maggie' in age)
print('Maggie' not in age)
print(age)

# TODO 11: How can you test if someone is 10 years old? 50 years old?
# {'Marge': 36, 'Homer': 36, 'Bart': 10, 'Lisa': 8}
print(10 in age.values())
print(50 in age.values())

# TODO 12: Check the course notes on dictionaries to learn about how they use
# hashing to allow super-fast key lookups (but slow value lookups).
