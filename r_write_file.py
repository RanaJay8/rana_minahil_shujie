# This line of code opens the file "pelican.txt" in append mode ("a"),
# meaning that any data written to the file will be added to the end of the file.
# If the file doesn't exist, it will be created.
# If the file does exist, new data will be appended to it without overwriting existing content.

file_handle = open("pelican.txt", "a")
file_handle.write("A wonderful bird is the pelican\n")
file_handle.close()

file_handle = open("pelican.txt", "a")
file_handle.write("His bill holds more than his belican\n")
file_handle.close()

# open file in append mode & adding the string to the file
with open("pelican.txt", "a") as file_handle:
    lines = ["He can take in his beak,\n","Enough food for a week,\n", "but I'm damned if I see how the helican.\n"]
    file_handle.writelines('\n'.join(lines)+ '\n')


# The \n is required so the limerick appears on different lines
# need to open and close the file handle each time .write is used
# when with is used, close will not be needed as it will do it automatically
# victoria? I have pressed print 4 times and it has added on an additional print to the bottom each time
