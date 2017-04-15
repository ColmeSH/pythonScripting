#Define a function called purify that takes in a list of numbers,
#removes all odd numbers in the list, and returns the result.

def purify(numbers):

	#validate the input
	if type(numbers) == list:
		#print 'ok'
		oth_list = []
		for i in range(len(numbers)):
			#check the number odd
			if numbers[i] % 2 == 0:
				#print str(numbers[i]) + " i m a odd number"

				#append in oth_list value
				oth_list.append(numbers[i])

		return oth_list
	else:
		print 'ERROR: insert a list'

print purify([1,2,3,4,7,9,8,90])
#example of error
#print purify(2)
