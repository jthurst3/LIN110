# author: 	   Luisa Neves
# project:     Phonemic Analysis
# file: 	   scanner.py - module to scan the input
# description: Parses an input file to determine and
#			   separate the two target phonemes and
#			   the list of words. Also calls the analysis
#			   functions.
from analysis import analyze
from word import Word


def run(phonemes, words):
    """Driver to call parsing and comparing functions."""
    phoneme1, phoneme2 = parse_phoneme(phonemes)

    print(phoneme1)
    print(phoneme2)
    print(words)

	print('Target phonemes: [' + phoneme1 + '], [' + phoneme2 + ']')
	print('Data set: ')
	print(words)

	# for each word in words, return word-trans pair
	# wt_pairs = [Word(w) for w in words]

	# for w in wt_pairs: print(w)

	analyze(phoneme1, phoneme2, words)

def parse_phoneme(line):
    """Parses first line of the file into the two target phonemes."""
    phonemes = line.partition(' ')
    phoneme1 = phonemes[0]
    phoneme2 = phonemes[2]
    return(phoneme1, phoneme2)
