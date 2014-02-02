#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Better BW Matching
Assignment #: 10
Problem ID: D
URL: https://stepic.org/Bioinformatics-Algorithms-2/Speeding-Up-Burrows-Wheeler-Pattern-Matching-301/step/6
'''


def get_pattern_count_beter_bw(bwt, patterns):
    '''Precomputes the necessary information for bw_matching and passes each pattern to bw_matching.'''
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
    return [better_bw_matching(bwt, first_occurrence, count, pattern) for pattern in patterns]


def better_bw_matching(bwt, first_occurrence, count, pattern):
    '''
    Follows the Better BW Matching algorithm given on Stepic to count the number of occurences of a given pattern in the original text.
    URL: https://stepic.org/Bioinformatics-Algorithms-2/Speeding-Up-Burrows-Wheeler-Pattern-Matching-301/step/5
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
                return 0
        else:
            return bottom - top + 1


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/stepic_10d.txt') as input_data:
        bwt = input_data.readline().strip()
        patterns = input_data.readline().strip().split()

    # Get the pattern count using the given Burrows-Wheeler Transform.
    pattern_count = map(str, get_pattern_count_beter_bw(bwt, patterns))

    # Print and save the answer.
    print ' '.join(pattern_count)
    with open('output/Assignment_10D.txt', 'w') as output_data:
        output_data.write(' '.join(pattern_count))

if __name__ == '__main__':
    main()
