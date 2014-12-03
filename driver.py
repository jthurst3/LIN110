# author:      Luisa Neves
# course: 	   LIN110
# project: 	   Phonemic Analysis
# file:		   driver.py - main function
# description: Given a body of words and two phonemes,
#			   this program will determine the status
#			   of distribution of the phonemes.
#			   All printing in run() and analyze()
import scanner

def main():
	with open('input.txt', 'r') as f:
		data = f.readlines()
		data = [i.strip('\n') for i in data]

	scanner.run(data[0], data[1:])

main()