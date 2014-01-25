#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Constructing Suffix Tree from Suffix Array Problem
Assignment #: 09
Problem ID: H
URL: https://stepic.org/Bioinformatics-Algorithms-2/Suffix-Arrays-310/step/6
'''
from scripts import SuffixArrayToTree


def edges_from_suffix_array(text, suffix_array, lcp_array):
    '''Returns the edge subsrings associated with the suffix tree constructed from a suffix array.'''

    # Construct the suffix tree from the suffix array and lcp array.
    # See suffix_array_to_tree.py in the scripts folder for construction details.
    suffix_tree = SuffixArrayToTree(text, suffix_array, lcp_array)

    # Return all of the edges.
    # Note: As opposed to the the suffix tree construction problem (Assignment 9D),
    #       I've used a regular suffix tree data structure instead of a genearlized
    #       suffix tree, so no edge formatting changes need to be made.
    return [suffix_tree.edge_word(e) for e in suffix_tree.edges.values()]


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''

    # Read the input data.
    with open('data/stepic_9h.txt') as input_data:
        text = input_data.readline().strip()
        suffix_array, lcp_array = [map(int, line.strip().split(', ')) for line in input_data.readlines()]

    # Get the edges and sort them for improved readability.
    edges = sorted(edges_from_suffix_array(text, suffix_array, lcp_array))

    # Print and save the answer.
    print '\n'.join(edges)
    with open('output/Assignment_09H.txt', 'w') as output_data:
        output_data.write('\n'.join(edges))

if __name__ == '__main__':
    main()
