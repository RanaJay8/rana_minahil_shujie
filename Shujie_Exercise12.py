# Collection

# 1 What is wrong with this?

cheese = ['Cheddar', 'stilton', 'Cornish Yarg']
cheese += 'Oke'
print(cheese)
# += take my cheese list and concatenate oke at the end
# 'oke' is a tuples which is why it added the letters individually
cheese += ['Oke']
# to add 'Oke' onto the list, we need to make ['Oke'] a list with square brackets
cheese += ['Mozzarella', 'Ricotta']
# to add 2 new cheeses, added them through a list with square brackets separated with a comma
print(cheese)

# 2 What is going on?

tup = 'Hello'
print(len(tup))
print(type(tup))
# This is a string, which is why it is able to calculate the length

tup = 'Hello',
print(len(tup))
print(type(tup))
# By having a comma at the end, it turns it into a tuple
# It calculates it as one object
