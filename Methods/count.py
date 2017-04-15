##################################################################################
#############################   STEP BY STEP #####################################
##################################################################################
#1) Define a function called count that has two arguments called sequence and item.
#2) Return the number of times the item occurs in the list.
#3) Count the times that the item is in the list



def count(sequence, item):
	#landing increment variable
	occ = 0
	exist = 0
	#check if exists in list
	for j in sequence:
		if j == item:
			exist += 1
			break

		else:
			exist = 0
		return exist


	#count times of item
	if exist >= 0:
		for i in sequence:
			if i == item:
				#print 'equals'
				occ += 1
	else:
		print "ERROR: the element does not exists"

	msg = 'i m in the list this times: '
	return msg + str(occ)

print count(['a','f','f','a','a','a','a'], 'a')
