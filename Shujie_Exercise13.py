# 3 Write a line of code to create a file handle to open and append to a file called pelican.txt

pelican_poem = open('spelican.txt', 'r')
print(pelican_poem.read())
# To open a file use the built-in open() function
# 'r' means to read the file
# There's nothing in the file yet

# 4 Append the line into the file using write method
pelican_write = open('spelican.txt', 'w')
# 'w' is the write mode
pelican_write.write("A wonderful bird is the pelican\n")
# .write to write the lyrics into the file
# \n to write the line on a new line

# 5 Write the second line
pelican_write.write("His bill holds more than his belican\n")

# 6 Create a list with the new lines
lines = ["He can take in his beak,\n", "Enough food for a week,\n", "But I'm damned if I see how the helican.\n"]
# \n to write each line on a new line

# 7 Append the list to the file using writelines method
pelican_write.writelines(lines)
