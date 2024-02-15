#!user/bin/python

import random


# help(random)

# define new function which generates a random set of numbers within a given range
# this is done using the random.sample() method
# into this function you can give a range which is 1-51 here as it is exclusive of the upper bound
# and after the range you can input an amount - i.e. how many random elements to select
# in this case it is 6
# random.sample() returns the values in a list form - built-in
# general format: random.sample(range(), amount)
def generate_lottery_numbers():
    return random.sample(range(1, 51), 6)


# the below line calls the function created and assigns the return value to a variable
# lottery_numbers
lottery_numbers = generate_lottery_numbers()
print("Lottery Numbers:", lottery_numbers)

lotto_numbers = random.sample(range(1, 51), 6)
print(lotto_numbers)
