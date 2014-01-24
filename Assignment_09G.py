#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Constructing Suffix Array Problem
Assignment #: 09
Problem ID: G
URL: https://stepic.org/Bioinformatics-Algorithms-2/Suffix-Arrays-310/step/3
'''


def construct_suffix_array(word):
    '''Constructs a suffix array from the given word.'''

    # Check that the word ends in the out of alphabet character '$'.
    word += ['', '$'][word[-1] != '$']

    # A lambda function to compare suffixes without generating the entire suffix.
    # Idea: To compare the suffixes word[i:] and word[j:] compare the letter at the ith and jth index.
    #       Return -1 if the ith letter comes before the jth letter, 1 if jth letter comes before the ith letter.
    #       If the indices match, repeat the process with the letter at the (i+1)th and (j+1)th index.
    suffix_comp = lambda i,j: [1, -1][word[i] < word[j]] if word[i] != word[j] else suffix_comp(i+1,j+1)

    # Sort the integer array using the suffix comparison function.
    suffix_array = sorted(xrange(len(word)), cmp=suffix_comp)

    return suffix_array


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''

    # Read the input data.
    with open('data/stepic_9g.txt') as input_data:
        text = input_data.read().strip()

    # Construct the suffix array and map the elements to a string for output writing.
    suffix_array = map(str, construct_suffix_array(text))

    # Print and save the answer.
    print ', '.join(suffix_array)
    with open('output/Assignment_09G.txt', 'w') as output_data:
        output_data.write(', '.join(suffix_array))

if __name__ == '__main__':
    main()
