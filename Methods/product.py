#Define a function called product that takes a list of integers as input
#and returns the product of all of the elements in the list.

def product(numbers):
	mult = 1

	for i in numbers:
		mult *= i

	return mult
print product([1,3,7,5,3])

