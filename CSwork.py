#Imports
from random import random
from random import seed

#Set up randomness
seed(random())

#Set up variables
counter = 1
answer = 0
times = 10
a = 0
b = 0
correct = 0

print()
while counter <= times: #Do 10 times
	a = round(10 * random()) #Two random numbers
	b = round(10 * random())
	
	answer = int(input("What is " + str(a) + " + " + str(b) + "? "))
	
	if (answer == (a + b)): #Check if sum is correct
		print("Correct!")
		correct += 1
	else:
		print("Wrong - it was " + str(a + b))
	counter += 1

#Output results
print()
print("You did " + str(times) + " questions, and got " + str(100 * correct / times)) + "% correct!"