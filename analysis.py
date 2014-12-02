# author: 	   Luisa Neves
# project:     Phonemic Analysis
# file: 	   analysis.py - module to analyzed the parsed
#			   input
# description: 

# returns array containing symbol before and after
# the given phoneme in the given word
def environment(phoneme, word):
	env = []
	index = -1

	if phoneme in word:
		while True:
			index = word.find(phoneme, index + 1)
			print(index)

			if index == -1: 
				break
			else:
				# insert character found before phoneme
				if index == 0:
					env.append('#')
				else:
					env.append(word[index-1])

				# insert character found after phoneme
				if index == (len(word)-1):
					env.append('#')
				else:
					env.append(word[index+1])
		
	else:
		env = [None, None]

	return env