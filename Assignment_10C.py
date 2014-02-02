#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: BW Matching
Assignment #: 10
Problem ID: C
URL: https://stepic.org/Bioinformatics-Algorithms-2/Pattern-Matching-with-the-Burrows-Wheeler-Transform-300/step/8
'''

from Assignment_10B import enumerate_word


def get_pattern_count_bw(bwt, patterns):
    '''Precomputes the necessary information for bw_matching and passes each pattern to bw_matching.'''
    # First column is just the BWT sorted.  Perform character enumeration on the first and last column characters.
    first_column = enumerate_word(sorted(bwt))
    last_column = enumerate_word(bwt)

    # Get the LastToFirst values.
    last_to_first = map(lambda i: first_column.index(last_column[i]), xrange(len(bwt)))

    # Pass the information and patters along to the BWMatching algorithm.
    return [bw_matching(bwt, last_to_first, pattern) for pattern in patterns]


def bw_matching(bwt, last_to_first, pattern):
    '''
    Follows the BW Matching algorithm given on Stepic to count the number of occurences of a given pattern in the original text.
    URL: https://stepic.org/Bioinformatics-Algorithms-2/Pattern-Matching-with-the-Burrows-Wheeler-Transform-300/step/7
    '''
    top, bottom = 0, len(bwt) - 1
    while top <= bottom:
        if pattern != '':
            symbol = pattern[-1]
            pattern = pattern[:-1]
            if symbol in bwt[top:bottom+1]:
                top_index = top + bwt[top:bottom+1].index(symbol)
                bottom_index = bottom - bwt[top:bottom+1][::-1].index(symbol)
                top = last_to_first[top_index]
                bottom = last_to_first[bottom_index]
            else:
                return 0
        else:
            return bottom - top + 1


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/stepic_10c.txt') as input_data:
        bwt = input_data.readline().strip()
        patterns = input_data.readline().strip().split()

    # Get the pattern count using the given Burrows-Wheeler Transform..
    pattern_count = map(str, get_pattern_count_bw(bwt, patterns))

    # Print and save the answer.
    print ' '.join(pattern_count)
    with open('output/Assignment_10C.txt', 'w') as output_data:
        output_data.write(' '.join(pattern_count))


if __name__ == '__main__':
    main()
