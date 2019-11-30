#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

# cite( https://anindifferentport.wordpress.com/2013/08/31/googles-python-class-wordcount-exercise/ )

# def get_filename():
#     user_file = raw_input("Enter filename: alice.txt")
#     return open(pythonize_url('C:\Development\Python\google_python/' + user_file), 'r')
     
def file_to_string(alice):
    with open(alice, "r") as file:
        return file.read().lower().split()

def generate_word_count(alice):
    list_of_strings = file_to_string(alice)
    unique_words = set()
    for word in list_of_strings:
        unique_words.add(word)
    word_count = [(word, list_of_strings.count(word)) for word in unique_words]
    return sorted(word_count, key=lambda x: x[1], reverse=True)

def print_words(alice):
    word_count = generate_word_count(alice)
    for item in word_count:
        print(item[0], item[1] )   

def print_top(alice):
    word_count = generate_word_count(alice)
 
    if len(word_count) < 20:
        num_words = len(word_count)
    else:
        num_words = 20
 
    for i in range(num_words):
        print word_count[i][0], word_count[i][1]
###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.


def main():
    if len(sys.argv) != 3:
        print 'usage: python wordcount.py {--count | --topcount} file'
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print 'unknown option: ' + option
        sys.exit(1)


if __name__ == '__main__':
    main()
