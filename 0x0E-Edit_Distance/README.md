# Edit Distance Problem

The Edit Distance Problem has many applications in computational biology, natural language processing, spell checking, and many other areas. For example, biologists often compute edit distances when they search for disease-causing mutations.

The edit distance between two strings is defined as the minimum number of single-symbol insertions, deletions, and substitutions to transform one string into the other one.

## Input Format
Two strings consisting of lowercase Latin letters, each on a separate line.

## Output Format
The edit distance between them.

## Sample
### Input:
short<br>
ports
### Output:
3

The second string can be obtained from the first one by deleting 's', substituting 'h' for 'p', and inserting 's'. This can be compactly visualized by the following alignment:<br>
`s h o r t -` −<br>
`- p o r t s`
