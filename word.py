# creates and returns word-trans object pair
import nltk

class Word:

	def __init__(self, word):
		self.word = word
		self.arpa = self.arpabet(word)
		self.ipa = self.ipa(self.arpa)

	def __str__(self):
		s = ''
		return "Word: " + self.word + " -> Arpabet: [" + s.join(self.arpa) + "]"

	def arpabet(self, word):
		"""Returns the Arpabet transcription of a given word as an array of symbols."""
		arpabet = nltk.corpus.cmudict.dict()

		return arpabet[word][0]

	def ipa(self, arpa):
		"""Returns the IPA transcription of a given word."""
		trans = []

		for symbol in arpa:
			if len(symbol) == 3:
				symbol = symbol[:-1]

			if symbol == 'F':
				trans.append('f')
			elif symbol == 'ER':
				trans.append('ə')

		return trans
