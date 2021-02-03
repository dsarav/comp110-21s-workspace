"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730318366"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
how_much: int = int(randint(1,10))

if how_much < 5:
    if how_much < 2:
        print("You'll make straight As this semester!")
    else:
        print("A fresh start is on your way!")
else:
    if how_much < 8:
        print("A lifetime friend shall soon be made.")
    else: 
        print ("All the effort you are making will ultimately pay off.")

print ("Now, go spread positive vibes!")