score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def scrabble_score(word):
	#1)split word in array
	l = word.split()
	#print l


	#2)cut spaces in word
	ns = ""
	cut = ns.join(l)
	#print cut

	#landing variable result
	result = 0

	#iterate cut
	for char in cut:
		for key in score:
			#score[key] is the value of the key
			#check
			if char == key:
				#print 'io sono char:' + char + ' io invece sono key: ' + key
				result += score[key]
	return result


txt = raw_input('tell me the text that i can count for you: ')

print scrabble_score(txt)
