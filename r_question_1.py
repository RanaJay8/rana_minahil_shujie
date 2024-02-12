cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']

# cheese += 'Oke'
print(cheese)

# using += causes it to be interpreted as a concat and will return oke by character. This is becuase the operator is
# being used with a string.

# Use append to add to the end.
# Use insert to add in where ever but will need to specify the position
cheese.append('Oke')
print(cheese)

# Use extend method to add more than one item to the list
cheese.extend(['Brie', 'Haloumi'])
print(cheese)