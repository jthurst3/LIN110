# -*- coding: utf-8 -*-
# author:      Luisa Neves
# project:     Phonemic Analysis
# file:        word.py - class to return a Word object
# description: Given an English word, this file returns a
#              new Word object, which consists of the original
#              English word and the Arpabet transcription of 
#              the word.
import nltk


class Word:

    def __init__(self, word):
        self.word = word
        self.arpa = self.arpabet(word)
        # self.ipa = self.ipa(self.arpa)

    def __str__(self):
        s = ''
        return "Word: " + self.word + " -> Arpabet: [" + s.join(self.arpa) + "]"

    def arpabet(self, word):
        """Returns the Arpabet transcription of a given word as an array of symbols."""
        arpabet = nltk.corpus.cmudict.dict()

        return arpabet[word][0]

    # MAY NOT WORK FOR INTENDED GOALS
    # def ipa(self, arpa):
    #   """Returns the IPA transcription of a given word."""
    #   trans = []

    #   for symbol in arpa:
    #       if len(symbol) == 3:
    #           symbol = symbol[:-1]

    #       if symbol == 'F':
    #           trans.append('f')
    #       elif symbol == 'ER':
    #           trans.append('ə')

    #   return trans
