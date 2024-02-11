# Q2 2 Use open and read method to display the context of the txt file

pelican_poem = open('spelican.txt', 'r')
print(pelican_poem.read())
# 'r' to read the file

# 3 & 4 What data type is the output?

print(f"The return data type is {type(pelican_poem.read())}")
# The data printed is a string

# 5 Write some code to turn the txt file into a list and output the number of items within the list

# doesn't work, check back on it-------------------------

pelican_string = pelican_poem.readline()
print(pelican_string)
pelican_list = pelican_string.split()
# created a new variable to contain the poem as a list
# by splitting the string at where the \n new line is turns it into a list
print(pelican_list)
print(f"The return data type is now {type(pelican_list)}")
print(f"The length of the list is {len(pelican_list)}")

# 6 loop iterate over and print the contents of the file

for i in range(5):
    # read the next 5 lines
    repeat_line = pelican_poem.readline()
    # print(line, repeat_line, end='')
    # line 20 will also the same as line 22
    print(i, repeat_line[:-1])
#     slicing it removes the blank linegit