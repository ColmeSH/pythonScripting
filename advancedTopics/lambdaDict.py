#lambda expression and iterate in dictionary
movies = {
	"Monty Python and the holy grail":"great",
	"Monty Python\'s life of brian":"good",
	"Monty Python\'s meaning of life":"okay",
}



filt = filter(lambda x: x==x ,movies)
print filt
