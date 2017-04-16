#anonymous function in python or lambda expression
languages = ["Html","javascript","Python","Ruby","PHP"]

##### WITH FILTER FUNCTION
#print filter(lambda x: x == "Python" ,languages)


#lambda expression
squares = [i**2 for i in range(1,11)]
#print squares

#filter func
filt = filter(lambda x: x>=30 and x<=70,squares)
print filt
