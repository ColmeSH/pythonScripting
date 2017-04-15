#let's start off by writing a function to
#print out the list of grades, one element at a time.


grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(list):
	for elem in list:
		print elem

print_grades(grades)
