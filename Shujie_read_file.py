# Q2 2 Use open and read method to display the context of the txt file

pelican_poem = open('spelican.txt', 'r').read()
print(pelican_poem)
# 'r' to read the file

# 3 & 4 What data type is the output?

print(f"The return data type is {type(pelican_poem)}")
# The data printed is a string

# 5 Write some code to turn the txt file into a list and output the number of items within the list

pelican_string = pelican_poem
print(pelican_string)
pelican_list = pelican_string.split('\n')
# created a new variable to contain the poem as a list
# by splitting the string at where the \n new line is turns it into a list
print(pelican_list)
print(f"The return data type is now {type(pelican_list)}")
print(f"The length of the list is {len(pelican_list)}")
print('\n')

# 6 loop iterate over and print the contents of the file

# For loop
for i in range(10):
    # range is however many times to repeat the poem, in this case 10
    repeat_line = pelican_poem
    print(repeat_line[:-1])
#     slicing it removes the blank line
# Infinite for loop will require an importing itertoools module

print('\n\n')

# While loop
# Repeat the poem 10 times with a while loop
i = 0
while i < 10:
    repeat_line = pelican_poem
    print(repeat_line[:-1])
    i += 1

# # While loop - infinite loop
# repeat_line = pelican_poem
# while True:
#     print(repeat_line[:-1])
