"""Compute term frequencies for an input file using an aspect-oriented style."""

import operator
import re
import string
import sys
import time


def extract_words(path_to_file):
    """Take file and assigns its contents to a list of words."""
    # TODO: Refer to the book for the source code of this function
    # TODO: Remember the correct way to encode regular expressions


def frequencies(word_list):
    """Take a list of words and creates a table of the frequencies for word appearance."""
    calculated_word_freqs = {}
    for word in word_list:
        if word in calculated_word_freqs:
            calculated_word_freqs[word] += 1
        else:
            calculated_word_freqs[word] = 1
    return calculated_word_freqs


def sort(word_freq):
    """Sort the word frequencies in the provided list."""
    return sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)


def profile(f):
    """Define a profiling aspect that can time a provided function."""
    # TODO: Add the profilewrapper function


if __name__ == "__main__":
    # define the function join points at which the aspect will be woven
    tracked_functions = [extract_words, frequencies, sort]
    # weave the profiling aspect into the tracked functions
    for func in tracked_functions:
        globals()[func.__name__] = profile(func)
    # perform the computation while also running the profiling aspect
    word_freqs = sort(frequencies(extract_words(sys.argv[1])))
    # display the top-25 word frequencies
    for (w, c) in word_freqs[0:25]:
        print(w, " - ", c)
