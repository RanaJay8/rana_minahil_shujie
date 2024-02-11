import random
# To generate randomised numbers, import random

# Generate and display 6 unique random numbers between 1 and 50

# help(random)
# The help() function will print various randomising number methods

# random.sample is a method that returns a random sampling
Lotto_numbers = random.sample(range(1, 50), 6)
# Using the range argument to generate numbers between 1 and 50
# the k value will return a specific amount of items in the list
# random.sample also works with lists of items
print(f"Lotto numbers of the week: {Lotto_numbers}")
# Using an f-string to print the results


# Using a for loop
Lotto = []
for i in range(6):
    # specifying the range as 6 will generate 6 numbers
    Lotto.append(random.randint(1, 50))
#   random.randint method returns an integer number from a specific range
print(f"Lotto numbers of the week: {Lotto}")


# Using a while loop
Lotto_while = []
Generate_6_numbers = 0
# initialise the count to 0
while Generate_6_numbers < 6:
    Lotto_while.append(random.randint(1,50))
    Generate_6_numbers += 1
#   Generate numbers until there's 6 of them
print(f"Lotto numbers of the week: {Lotto_while}")
