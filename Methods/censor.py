#Write a function called censor that takes two strings,
#text and word, as input.
#It should return the text with the word you chose replaced with asterisks.
def censor(text, word):
	#1)validation input
	txt = text.lower()
	#print txt

	#2)split text
	splt = txt.split()
	#print splt

	#3)search word in splitted list
	src = splt.index(word)
	#print src

	#var result
	new_result = ""

	#check
	for i in splt:
		if i == splt[src]:
			splt[src] = '*' * len(word)
			#print splt[src]

	new_result = " ".join(splt)

	return new_result




print 'My favourite language is Python'
inp = raw_input('what \'s your word that you wanna replace? ')
print censor('My favourite language is Python', inp.lower())
