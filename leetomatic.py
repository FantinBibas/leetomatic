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


def get_transformations(dictionary, character, auto_casing, base_letter):
    if character.lower() in dictionary.keys():
        for transformation in dictionary[character.lower()]:
            yield transformation
    if base_letter:
        if auto_casing:
            yield character.lower()
            yield character.upper()
        else:
            yield character


def leetomatic(dictionary, word, auto_casing=True, base_letter=True):
    if len(word) == 0:
        yield word
    else:
        character = word[0]
        transformations = get_transformations(dictionary, character, auto_casing, base_letter)
        if len(word) == 1:
            yield from transformations
        else:
            for prefix, suffix in itertools.product(transformations, leetomatic(dictionary, word[1:])):
                yield prefix + suffix


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
