#!/usr/bin/env python3

import sys
import string


alphabet = "abcdefghijklmnopqrstuvwxyz"
missing = []
#def pangram():


# alphabet = {"a": None , "b": None , "c": None , "d": None , "e": None , "f": None ,
            #"g": None , "h": None , "i": None , "j": None , "k": None , "l": None ,
            #"m": None , "n": None , "o": None , "p": None , "q": None , "r": None ,
            #"s": None , "t": None , "u": None , "v": None , "w": None , "x": None ,
            #"y": None , "z": None
            #}

for line in sys.stdin:
    alphabet_list = [char for char in alphabet]
    line = line.strip().lower()
    line = "".join(char for char in line if char not in string.punctuation and char != " ")
    for char in line:
        if char in alphabet_list:
            alphabet_list.remove(char)
                  

    if len(alphabet_list) == 0:
        print("pangram")

    else:
        string_alphabet = "".join(char for char in alphabet_list)
        print(f'missing {string_alphabet}')
