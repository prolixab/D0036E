# Exercise 1
# Write a program that reads a file, breaks each line into words, strips whitespace and punctuation from the words, and converts them to lowercase.
# Hint: The string module provides a string named whitespace, which contains space, tab, newline, etc., and punctuation which contains the punctuation characters. Let’s see if we can make Python swear:
# >>> import string
# >>> string.punctuation
# '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# Also, you might consider using the string methods strip, replace and translate.
import string


def strip_whitespace(word):
    for char in word:
        if char in string.whitespace:
            word = word.replace(char, "")
    return word


def strip_punctuation(word):
    for char in word:
        if char in string.punctuation:
            word = word.replace(char, "")
    return word


final_words = []

f = open("macbeth.txt", "r")
for line in f:
    word_array = line.split()
    for word in word_array:
        word = strip_whitespace(word)
        word = strip_punctuation(word)
        word = word.lower()
        final_words.append(word)

print(final_words)
