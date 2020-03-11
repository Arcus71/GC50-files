#Imports
from random import random #Required
from random import seed #Optional

#Set up randomness (optional)
seed(0)

#Set up bounds
UB = int(input("Enter an upper bound: "))
LB = int(input("Enter a lower bound: "))

#Iterations
it = int(input("Iterations: "))
c = 0

print()
while c < iterations:
   print(round((UB-LB)*random()) + LB) #Write a random number from LB to UB
   c += 1