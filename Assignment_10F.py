#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Multiple Pattern Matching Problem
Assignment #: 10
Problem ID: F
URL: https://stepic.org/Bioinformatics-Algorithms-2/Burrows-and-Wheeler-Set-Up-Checkpoints-303/step/4
'''

from Assignment_09G import construct_suffix_array
from Assignment_10A import burrows_wheeler_transform


def get_multi_pattern_count(word, patterns):
    '''Precomputes the necessary information and passes each pattern to multiple pattern matching function.'''
    # Construct the Burrows-Wheeler Transform and Suffix Array.
    bwt = burrows_wheeler_transform(word)
    suffix_array = construct_suffix_array(word)

    # Create the count dictionary.
    symbols = set(bwt)
    current_count = {ch:0 for ch in symbols}
    count = {0:{ch:current_count[ch] for ch in symbols}}
    for i in xrange(len(bwt)):
        current_count[bwt[i]] += 1
        count[i+1] = {ch:current_count[ch] for ch in symbols}

    # Get the index of the first occurrence of each character in the sorted Burrows-Wheeler Transformation.
    sorted_bwt = sorted(bwt)
    first_occurrence = {ch:sorted_bwt.index(ch) for ch in set(bwt)}

    # Pass the information and patters along to the BWMatching algorithm.
    matches = []
    for pattern in patterns:
        matches += multi_pattern_match_bw(bwt, suffix_array, first_occurrence, count, pattern)
    return matches


def multi_pattern_match_bw(bwt, suffix_array, first_occurrence, count, pattern):
    '''
    Returns the starting index of each occurrence of pattern in the given word using a
    slightly modified version of the Better BW Matching algorithm from Assignment 10D.
    '''
    top, bottom = 0, len(bwt) - 1
    while top <= bottom:
        if pattern != '':
            symbol = pattern[-1]
            pattern = pattern[:-1]
            if symbol in bwt[top:bottom+1]:
                top = first_occurrence[symbol] + count[top][symbol]
                bottom = first_occurrence[symbol] + count[bottom+1][symbol] - 1
            else:
                return []
        else:
            return [suffix_array[i] for i in xrange(top, bottom+1)]


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/stepic_10f.txt') as input_data:
        word = input_data.readline().strip()
        patterns = [line.strip() for line in input_data.readlines()]

    # Get the pattern locations.  Sort for convenience, then map to strings.
    pattern_locations = get_multi_pattern_count(word, patterns)
    pattern_locations = map(str, sorted(pattern_locations))

    # Print and save the answer.
    print ' '.join(pattern_locations)
    with open('output/Assignment_10F.txt', 'w') as output_data:
        output_data.write(' '.join(pattern_locations))

if __name__ == '__main__':
    main()
