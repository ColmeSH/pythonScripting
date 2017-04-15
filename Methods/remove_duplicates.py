#Write a function remove_duplicates that takes in a list
#and removes elements of the list that are the same.

def remove_duplicates(numbers):

	#validate array input
	if type(numbers) == list:

		correct_list = []
		for i in numbers:
			if i not in correct_list:
				correct_list.append(i)
			else:
				print 'i am duplicate number' + str(i)


	return correct_list
print remove_duplicates([40,50,60,50,60,55,40])

#error input
#remove_duplicates(1)



#features
#1)count how many times number is in list



