#Write a function called median that takes
#a list as an input and returns the median value of the list.
#The list can be of any size and the numbers are not
#guaranteed to be in any particular order.
#If the list contains an even number of elements,
#your function should return the average of the middle two.

def median(numbers):
	#print len(numbers)
	ord_list = sorted(numbers)

	if len(ord_list) % 2 != 0:
		#print 'i am a odd list'
		src = (len(ord_list)-1)/2

		#print ord_list
		median = ord_list[src]


	else:
		#print 'i am an even list'
		src1 = len(ord_list)/2
		src2 = (len(ord_list)/2)-1

		#index numbers in list
		num1 = ord_list[src1]
		num2 = ord_list[src2]

		#cast sum value of num1 and num2
		median = (float(num1) + num2)/2

	print ord_list
	return median












print median([76,45,7,4,5,6,7,8,78,89,89])


print "#####################"
print "######################"
print "######################"
print "######################"
print "####################"
print "######################"
print "####################"
print "######################"



print median([2,3,5,6,80,7,65,43,3,4,23,1,2,2,32,12])

