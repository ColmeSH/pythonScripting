#fixing list comprehension
cubes_by_four = [ i**3 for i in range(1,11) if (i**3) % 4 == 0]
print cubes_by_four
