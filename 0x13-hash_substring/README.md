# Rabin-Karp String Matching Algorithm

This is a Python implementation of the Rabin-Karp string matching algorithm. The Rabin-Karp algorithm is used for finding all occurrences of a pattern string within a larger text string.

## Features

- Efficient string matching using polynomial hashing
- Precomputation of hash values for improved performance
- Handles large texts and patterns

## Functions

1. `poly_hash(s, prime, multiplier)`: Computes the polynomial hash of a string.
2. `precompute_hashes(text, pattern_len, prime, multiplier)`: Precomputes hash values for all substrings of the text with length equal to the pattern length.
3. `rabin_karp(text, pattern)`: Implements the Rabin-Karp algorithm to find all occurrences of the pattern in the text.

## Usage

To use the Rabin-Karp algorithm:

1. Run the script.
2. Enter the pattern string when prompted.
3. Enter the text string when prompted.
4. The script will output the starting positions of all occurrences of the pattern in the text.

Example 1:

Input:

aba

abacaba

Output:

0 4

Example 2:

Input:

aaaaa

baaaaaaa

Output:

1 2 3

Note that the occurrences of the pattern in the text can be overlapping.

## Time Complexity

The average and best-case time complexity of the Rabin-Karp algorithm is O(n+m), where n is the length of the text and m is the length of the pattern.

## Space Complexity

The space complexity is O(n-m+1) for storing the precomputed hash values.
