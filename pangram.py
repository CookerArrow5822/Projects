#!/usr/bin/env python3
# this code is made to check if a sentence contains all letters of the alphabet, if so it will print "pangram"
# if not it will list what letters the sentence is missing

#importing sys and string
import sys
import string

#string of the alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"
missing = []
#for all of the lines read in stdin one by one 
for line in sys.stdin:
    #creates a list of all the letters of the alphabet        
    alphabet_list = [char for char in alphabet
    #strips the whitespaces of the line of input and makes it lower        
    line = line.strip().lower()
    # creates a new string while removing all punctuation and spaces      
    line = "".join(char for char in line if char not in string.punctuation and char != " ")
    # goes through each character in the line one by one and if found in the alphabet list removes it from the alphabet list        
    for char in line:
        if char in alphabet_list:
            alphabet_list.remove(char)
                  
    #if all of the letters in the alphabet has been found print "pangram"        
    if len(alphabet_list) == 0:
        print("pangram")
    #if all letters are not found then prints what characters are missing        
    else:
        string_alphabet = "".join(char for char in alphabet_list)
        print(f'missing {string_alphabet}')
