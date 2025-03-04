#!/usr/bin/env python3
# this program takes any number (1 - 100) and transfers it into words
import sys
# loads numbers needed to complete the exercise
def load_number_words():
    number_words = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
        16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
        20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
        70: "seventy", 80: "eighty", 90: "ninety", 100: "one hundred"
    }
# assigning each number it's english word value in the dictionary
    for i in range(21, 100):
        if i not in number_words:
            tens = (i // 10) * 10
            ones = i % 10
            number_words[i] = number_words[tens] + ("-" + number_words[ones] if ones else "")
    return number_words
# calls the function and returns the number of words as a joined string seperated by a " "
def nums_to_words(line, number_words):
    return " ".join(number_words[int(num)] for num in line.strip().split())


number_words = load_number_words()
for line in sys.stdin:
    print(nums_to_words(line, number_words))
