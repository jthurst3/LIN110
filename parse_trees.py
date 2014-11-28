# parse_trees.py
# Given a CFG and a sentence, general all possible parse trees for the sentence
# Uses NLTK (Natural Language toolkit) and CYK algorithm
# Jamie Alexander, Luisa Neves, Ben Ouattara, J. Hassler Thurston
# November 15, 2014

from nltk import word_tokenize
from nltk.grammar import parse_cfg
from nltk import ChartParser
from nltk.tree import Tree

import sys
# from nltk.corpus import treebank

# grammar that we're using in class
class_grammar_1 = parse_cfg("""
    Start -> S
    S -> NP VP | NP aux VP
    NP -> N | Det N | Adj N | Det Adj N | N PP | Det N PP | Adj N PP | Det Adj N PP
    VP -> V | V NP | V PP | V NP PP
    PP -> P NP
    Aux -> 'is' | 'does'
    Det -> 'the' | 'a' | 'an' | 'my'
    N -> 'apple' | 'banana' | 'orange' | 'elephant' | 'pajamas' | 'i'
    V -> 'eats' | 'kills' | 'writes' | 'saw' | 'shot'
    Adj -> 'red' | 'blue' | 'quick' | 'slow'
    P -> 'with' | 'by' | 'in'
    """)


def generate_parse_tree(sentence):
    # first, convert the sentence to lowercase
    lower = sentence.lower()
    # then generate the parse trees
    tokens = word_tokenize(lower)
    parser = ChartParser(class_grammar_1)
    print type(class_grammar_1), type(parser)
    try:
        return parser.parse(tokens)
    except Exception:
        print "Sentence '" + sentence + "' cannot be parsed using the given grammar."
        return Tree('Error', ['No Solution'])


# main method of the parse tree program
# takes in a sentence in the command-line, outputs all possible parse trees of the sentence
if __name__ == '__main__':
    # generate the parse tree for the sentence they inputed
    trees = generate_parse_tree(sys.argv[1])
    for tree in trees:
        print "tree: "
        print tree
