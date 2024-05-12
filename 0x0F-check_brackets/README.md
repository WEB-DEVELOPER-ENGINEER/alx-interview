# Bracket Checker

## Overview

This program is designed to help you identify errors in your text related to the usage of brackets. It scans through a given string and checks if the brackets are correctly matched and nested. The supported brackets include `()`, `[]`, and `{}`. The solution utilizes the stack data structure to efficiently solve the problem.

## Input

The input consists of a string `S` containing various characters such as letters, digits, punctuation marks, and brackets.

## Output

- If the brackets in the input code are used correctly, it outputs "Success".
- If there's an unmatched closing bracket, it returns the 1-based index of that bracket.
- If there's an unmatched opening bracket without a corresponding closing bracket, it returns the 1-based index of that opening bracket.

## Examples

- Input: `[]`, Output: `Success`
- Input: `{[}`, Output: `3`
