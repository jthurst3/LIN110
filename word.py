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
          if symbol[-1].isdigit(): symbol = symbol[:-1] # remove Arpabet stress indicator

          # VOWELS
          # monopthongs
          if symbol == 'AO':
              trans.append('ɔ')
          elif symbol == 'AA':
              trans.append('ɑ')
          elif symbol == 'IY':
              trans.append('i')
          elif symbol == 'UW':
              trans.append('u')
          elif symbol == 'EH':
              trans.append('ɛ')
          elif symbol == 'IH':
              trans.append('ɪ')
          elif symbol == 'UH':
              trans.append('ʊ')
          elif symbol == 'AH': # overlap with AX (?)
              trans.append('ʌ')
          elif symbol == 'AX':
              trans.append('ə')
          elif symbol == 'AE':
              trans.append('æ')

          # dipthongs
          elif symbol == 'EY':
              trans.append('eɪ')
          elif symbol == 'AY':
              trans.append('aɪ')
          elif symbol == 'OW':
              trans.append('oʊ')
          elif symbol == 'AW':
              trans.append('aʊ')
          elif symbol == 'OY':
              trans.append('ɔi')

          # R-colored vowels
          elif symbol == 'ER':
              trans.append('ɝ')
          elif symbol == 'AXR':
              trans.append('ɚ')
          elif symbol == 'EH': # and next symbol == 'R'
              trans.append('ɛr')
          elif symbol == 'UH': # and next symbol == 'R'
              trans.append('ʊr')
          elif symbol == 'AO': # and next symbol == 'R'
              trans.append('ɔr')
          elif symbol == 'AA': # and next symbol == 'R'
              trans.append('ɑr')
          elif symbol == 'IH': # and next symbol == 'R'
              trans.append('ɪr')
          elif symbol == 'IY': # and next symbol == 'R'
              trans.append('ɪr')
          elif symbol == 'AW': # and next symbol == 'R'
              trans.append('aʊr')

          # CONSONANTS
          # stops
          elif symbol == 'P':
              trans.append('p')
          elif symbol == 'B':
              trans.append('b')
          elif symbol == 'T':
              trans.append('t')
          elif symbol == 'D':
              trans.append('d')
          elif symbol == 'K':
              trans.append('k')
          elif symbol == 'G':
              trans.append('g')

          # affricates
          elif symbol == 'CH':
              trans.append('tʃ')
          elif symbol == 'JH':
              trans.append('dʒ')

          # fricatives
          elif symbol == 'F':
              trans.append('f')
          elif symbol == 'V':
              trans.append('v')
          elif symbol == 'TH':
              trans.append('θ')
          elif symbol == 'DH':
              trans.append('ð')
          elif symbol == 'S':
              trans.append('s')
          elif symbol == 'Z':
              trans.append('z')
          elif symbol == 'SH':
              trans.append('ʃ')
          elif symbol == 'ZH':
              trans.append('ʒ')
          elif symbol == 'HH':
              trans.append('h')

          # nasals
          elif symbol == 'M':
              trans.append('m')
          elif symbol == 'EM':
              # trans.append('m̩')
              trans.append('m')
          elif symbol == 'N':
              trans.append('n')
          elif symbol == 'EN':
              # trans.append('n̩')
              trans.append('n')
          elif symbol == 'NG':
              trans.append('ŋ')
          elif symbol == 'ENG':
              # trans.append('ŋ̍')
              trans.append('ŋ')


          # liquids
          elif symbol == 'L':
              trans.append('ɫ')
          elif symbol == 'EL':
              # trans.append('ɫ̩')
              trans.append('ɫ')
          elif symbol == 'R':
              trans.append('ɹ')
          elif symbol == 'DX':
              trans.append('ɾ')
          elif symbol == 'NX':
              # trans.append('ɾ̃')
              trans.append('ɾ')


          # semivowels
          elif symbol == 'Y':
              trans.append('j')
          elif symbol == 'W':
              trans.append('w')
          elif symbol == 'Q':
              trans.append('ʔ')
    
      # print "hello"
      # print trans
      # print ''.join(trans)
      # convert to unicode
      # ustr = u'';
      # for t in trans:
      #   ustr += t.decode('unicode-escape')
      return ''.join(trans)
