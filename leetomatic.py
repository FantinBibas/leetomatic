#!/usr/bin/env python3

import itertools
import sys


characters_transformations = {
    'a': ['4', '@', 'q'],
    'e': ['3', '€'],
    'h': ['#'],
    'i': ['1', '!', '|'],
    'l': ['1', '!', '|'],
    'o': ['0'],
    's': ['5'],
    't': ['7'],
    'z': ['2'],
}


def leetomatic(dictionnary, word, auto_casing=True, base_letter=True):
    if len(word) == 0:
        return [word]
    character = word[0]
    transformations = dictionnary[character.lower()] if character.lower() in dictionnary.keys() else []
    if base_letter:
        if auto_casing:
            transformations.append(character.lower())
            transformations.append(character.upper())
        else:
            transformations.append(character)
    if len(word) == 1:
        return transformations
    return [prefix + suffix for prefix, suffix in itertools.product(transformations, leetomatic(dictionnary, word[1:]))]


def usage(name):
    print("USAGE:\n\t" + name + "\t[-h] word\n\nDESCRIPTION:")
    print("\t-h\tdisplay this help and exit")
    print("\tword\tword to transform")


def main(argv):
    if '-h' in argv[1:] or len(argv) != 2:
        usage(argv[0])
        return 0 if '-h' in argv[1:] else 1
    for possibility in leetomatic(characters_transformations, argv[1]):
        print(possibility)
    return 0


if __name__ == '__main__':
    exit(main(sys.argv))
