# Extended Stack Interface

## Input Format
The input consists of several queries. The first line of the input contains an integer `q` representing the number of queries. Each of the following `q` lines specifies a query in one of the following formats:
- `push v`: Push the value `v` onto the stack.
- `pop`: Pop the top element from the stack.
- `max`: Find and output the maximum value currently present in the stack.

The goal is to ensure that all operations (Push, Pop, and Max) work in constant time.

## Output Format
For each `max` query, output the maximum value of the stack on a separate line.

## Sample Input/Output

### Sample 1.
**Input:**

5

push 2

push 1

max

pop

max

**Output:**

2

2
### Sample 2.
**Input:**

10

push 2

push 3

push 9

push 7

push 2

max

max

max

pop

max

**Output:**

9

9

9

9
