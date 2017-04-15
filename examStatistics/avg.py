grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


#function sum
def grades_sum(scores):
	total = 0
	for item in scores:
		total += item
	return total


grades_sum(grades)



#function avg
def grades_average(l):
	#call function sum that store in variable
	total = grades_sum(l)

	#divide by float length of list
	total /= float(len(l))

	return total
print grades_average(grades)
