#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Longest Repeat Problem
Assignment #: 09
Problem ID: C
URL: https://stepic.org/Bioinformatics-Algorithms-2/Preprocessing-the-Genome-Instead-295/step/8
'''

from scripts import GeneralizedSuffixTree


# The problem statement says to use a suffix trie, but (generalized) suffix trees are much more efficient.
def longest_repeat_substring(word, n):
    '''Returns the longest substring that appears at least n times in the given word.'''

    # Construct the suffix tree.
    gst = GeneralizedSuffixTree(word)

    # Find all nodes with at least n children.
    # The number of children a node has tells us how many times is associated substring appears within the string.
    candidate_nodes = filter(lambda i: len(gst.nodes[i].children) >= n, xrange(len(gst.nodes)))

    # Get the longest substring that appears at least n times.
    # Recall: node depth = proper length of substring, i.e. the length discounting the out of alphabet characters.
    best_node = max(candidate_nodes, key=lambda i: gst.node_depth(i))

    return gst.node_substring(best_node)


def main():
    '''Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/stepic_9c.txt') as input_data:
        text = input_data.read().strip()

    # Get the longest substring that appears more than once in the given string.
    longest_repeat = longest_repeat_substring(text, 2)

    # Print and save the answer.
    print longest_repeat
    with open('output/Assignment_09C.txt', 'w') as output_data:
        output_data.write(longest_repeat)

if __name__ == '__main__':
    main()
