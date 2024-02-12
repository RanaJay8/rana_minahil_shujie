#!user/bin/python

# use 'r' to read the file
limerick = open('pelican.txt', 'r').read()

# use type function to find data type
# it is a string
print(f"The type of this data is {type(limerick)}")

# print the contents of the entire file
print(f'Lyrics:\n {limerick}')

# to convert the contents into a list use .splitlines() method
# this method is used to split a string into a list of strings
# it splits them at line boundaries - \n
# assign this list to a variable
# use len function to return the length of the list - counts each item
limerick_as_list = open('pelican.txt', 'r').read().splitlines()
print(f"Number of lines: {len(limerick_as_list)}")

# use a file object iterator to print exact contents of the file
# using a for loop iterates over each line of text in opened file
# use print function to print out each line of text
# the [:-1] uses slicing and removes last character from line
# in this case it is '\n'
# this ensures that no additional newline is added when printing
for line in open('pelican.txt', 'r'):
    print(line[:-1])
