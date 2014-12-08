# -*- coding: utf-8 -*-
# author:      Luisa Neves
# project:     Phonemic Analysis
# file:        analysis.py - module to analyzed the parsed
#              input
# description: Analyzes a body of data and the two target 
#              phonemes in order to describe the distribution
#              and features of the two phonemes with respect
#              to the data set.
import math

def analyze(phoneme1, phoneme2, words):
    """Driver to call various analytical functions on the data set."""
    env1 = []
    env2 = []
    majority = math.ceil(len(words)/2)

    for word in words:
        e1 = environment(phoneme1, word)
        e2 = environment(phoneme2, word)
        for pair in e1:
            if pair is not None: env1.append(pair)
        for pair in e2:
            if pair is not None: env2.append(pair)

    # print('\nEnvironment of [' + phoneme1 + ']:')
    print(prettyEnvironment(env1))

    # print('\nEnvironment of [' + phoneme2 + ']:')
    print(prettyEnvironment(env2))

    if overlap(env1, env2, majority):
        if meaning():
            # print('[' + phoneme1 + '] and [' + phoneme2 + '] are in free variation.')
            print('free variation')
            print('')
        else:
            # print('[' + phoneme1 + '] and [' + phoneme2 + '] are in contrastive distribution.')
            # print('The two phonemes are allophones of different phonemes.')
            print('contrastive distribution')
            print('allophones of separate phonemes')
    else:
        # print('[' + phoneme1 + '] and [' + phoneme2 + '] are in complementary distribution.')
        # print('The two phonemes are allophones of the same phoneme.')
        print('complementary distribution')
        print('allophones of the same phoneme')
        # reasoning - elsewhere vs. pattern (?)

    return None

def environment(phoneme, word):
    """Returns the environment of the given phoneme as a list."""
    env = []
    temp = []
    index = -1

    if phoneme in word:
        while True:
            index = word.find(phoneme, index + 1)

            if index is -1:
                # phoneme not found
                break
            else:
                # insert character found before phoneme
                env.append('#') if index is 0 else env.append(word[index-1])

                # insert character found after phoneme
                env.append('#') if index is (len(word)-1) else env.append(word[index+1])
    else:
        env = None

    if env is not None and len(env) > 2:
        for i in range(len(env)):
            if i % 2 is 0:
                temp.append(env[i:i+2])
    else:
        temp.append(env)

    env = temp
    return env

def prettyEnvironment(env):
    """Returns a pretty-printed (LIN110 exercise) version of the environment for a phoneme."""
    resultString = ""
    pairsSoFar = []
    for pair in env:
        # only print(it if this is not a duplicate pair
        if pair not in pairsSoFar:
            resultString += pair[0] + "_" + pair[1] + ", "
            pairsSoFar.append(pair)
    # delete the last command and space
    return resultString[:-2]


def overlap(env1, env2, majority):
    """Returns true if the environments of the two phonemes overlap."""
    count = 0

    for pair1 in env1:
        for pair2 in env2:
            if pair1 == pair2: count += 1

    if count >= majority: return True

    return False

def meaning():
    """Returns true if substituting one phoneme for the other produces the same meaning."""

    return False