#!/user/bin/python

# Question 1
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
print(cheese)

# cheese += 'Oke'
# The above code will not add Oke to the list as it is not in list form
# it will concatenate O, k and e to the list as separate values as it is given in a string form
# using [] will add it Oke to the list as a value
cheese += ['Oke']
print(cheese)

# can also use the .append method to do this
# cheese.append('Oke')
# print(cheese)

# to add two new values to the list with a single command
cheese += ['Parmesan', 'Cheddar']
print(cheese)

# can also use the .extend method
# cheese.extend(['Parmesan', 'Cheddar'])
# print(cheese)

# Question 2

# a) the code below prints 5 as the variable tup is a string value
#    therefore, len counts number of characters in the string which is 5

# tup = 'Hello'
# print(len(tup))

# b) this code prints 1 as the variable tup here is a tuple because of the ','
#    so len counts how many values within the tuple which is 1

# tup = 'Hello',
# print(len(tup))

