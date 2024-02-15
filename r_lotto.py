#randrange()	Returns a random number between the given range
#randint()	    Returns a random number between the given range

import random
print(random.randrange(1,51))

# can also use
print(random.randint(1,50))

# The main difference between randrange() and randint() lies in how they specify the range of random numbers.
# randrange() excludes the stop value, randint() includes both the start and stop values.
# randrange() allows for a step parameter, enabling you to generate random numbers with specific increments.

# Used a loop 'for' to generate 6 random numbers in one list
lotto_numbers =[random.randint(1,50) for _ in range(6)]
print(lotto_numbers)
print(type(lotto_numbers))