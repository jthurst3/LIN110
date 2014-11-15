# parse_trees.py
# Given a CFG and a sentence, general all possible parse trees for the sentence
# Uses NLTK (Natural Language toolkit) and CYK algorithm
# Jamie Alexander, Luisa Neves, Ben Ouattara, J. Hassler Thurston
# November 15, 2014

import nltk
# from nltk.corpus import treebank


def generate_parse_tree(sentence):
    tokens = nltk.word_tokenize(sentence)
    return tokens


if __name__ == '__main__':
    print generate_parse_tree("the boy walked")
