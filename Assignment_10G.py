#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Multiple Approximate Pattern Matching Problem
Assignment #: 10
Problem ID: G
URL: https://stepic.org/Bioinformatics-Algorithms-2/Epilogue-Mismatch-Tolerant-Read-Mapping-304/step/6
'''

# ---------------------------------------------------------------------
# NOTE: This problem has a long runtime.  Use PyPy to speed things up!
# ---------------------------------------------------------------------

from Assignment_09G import construct_suffix_array
from Assignment_10A import burrows_wheeler_transform
from Assignment_10F import multi_pattern_match_bw


def multi_approx_pattern_match(word, patterns, d):
    '''Returns the starting indices of all approximate matches to the given list of patterns using the seed method.'''
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

    # Detect and extend seeds to find the approximate pattern locations.
    matches = []
    for num, pattern in enumerate(patterns):
        seed_locations = seed_detection(bwt, suffix_array, first_occurrence, count, word, pattern, d)
        matches += [seed_index for seed_index in seed_locations if seed_extension(word, pattern, seed_index, d) is True]

    return matches


def seed_detection(bwt, suffix_array, first_occurrence, count, word, pattern, d):
    '''Determines seed locations, shifted to the starting index of each pattern.'''
    k = len(pattern)/(d+1)
    seeds = [pattern[j:j+k] for j in xrange(0, len(pattern), k)]
    seed_locations = set()
    for i, seed in enumerate(seeds):
        # Get all seed matches.
        shifted_matches = multi_pattern_match_bw(bwt, suffix_array, first_occurrence, count, seed)
        # Shift the results back to the starting pattern index.
        shifted_matches = [shifted - k*i for shifted in shifted_matches]
        # Remove starting indices corresponding to patterns that do not entirely overlap the word.
        shifted_matches = [shifted for shifted in shifted_matches if i >= 0 and i + len(pattern) <= len(word)]
        # Add them to a set so we don't get repeat starting indices for the same pattern.
        seed_locations |= set(shifted_matches)

    return seed_locations


def seed_extension(word, pattern, seed_index, d):
    '''Determines if a seed location can be extended to the approximate pattern, returning the corresponding Boolean.'''
    count = 0
    for i in xrange(len(pattern)):
        if pattern[i] != word[seed_index+i]:
            count += 1
            if count > d:  # Can't extend if we have more than d mismatches.
                return False
    return True


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/stepic_10g.txt') as input_data:
    # with open('D:/test2.txt') as input_data:
        word = input_data.readline().strip()
        patterns = input_data.readline().strip().split()
        d = int(input_data.readline())

    # Get the pattern count using the given Burrows-Wheeler Transform.
    pattern_locations = multi_approx_pattern_match(word, patterns, d)
    pattern_locations = map(str, sorted(pattern_locations))

    # Print and save the answer.
    print ' '.join(pattern_locations)
    with open('output/Assignment_10G.txt', 'w') as output_data:
        output_data.write(' '.join(pattern_locations))

if __name__ == '__main__':
    main()
