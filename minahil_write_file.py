#!user/bin/python

# open the file in append mode using:
# built-in open function - open()
# to open it in append mode - "a"
file_handle = open('pelican.txt', "a")


file_handle.write('A wonderful bird is the pelican \n')
file_handle.write('His bill holds more than his belican \n')

# \n ensures there are new lines
lines = ["He can take his beak, \n", "Enough food for a week \n", "But I'm damned if I can see how the helican. \n"]
file_handle.writelines(lines)
