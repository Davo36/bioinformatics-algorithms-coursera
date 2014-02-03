#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Partial Suffix Array
Assignment #: 10
Problem ID: E
URL: https://stepic.org/Bioinformatics-Algorithms-2/Where-are-the-Matched-Patterns-302/step/3
'''

from Assignment_09G import construct_suffix_array


def construct_partial_suffix_array(word, k):
    '''Constructs a suffix array from the given word.'''
    # Check that the word ends in the out of alphabet character '$'.
    word += ['', '$'][word[-1] != '$']

    # Construct the suffix array for the given word.
    suffix_array = construct_suffix_array(word)

    # Return the position and value of elements that are multiples of k.
    return [(i, s) for i, s in enumerate(suffix_array) if s % k == 0]


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/stepic_10e.txt') as input_data:
        text = input_data.readline().strip()
        k = int(input_data.readline().strip())

    # Construct the suffix array and map the elements to a string for output writing.
    partial_suffix_array = construct_partial_suffix_array(text, k)

    # Print and save the answer.
    print '\n'.join([','.join(map(str, pair)) for pair in partial_suffix_array])
    with open('output/Assignment_10E.txt', 'w') as output_data:
        output_data.write('\n'.join([','.join(map(str, pair)) for pair in partial_suffix_array]))

if __name__ == '__main__':
    main()
