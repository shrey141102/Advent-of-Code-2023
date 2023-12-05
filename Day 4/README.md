# Advent of Code - Day 4: Scratchcards

## Problem Statement

In this puzzle, you are given a set of scratchcards, each containing two lists of numbers: a list of winning numbers and a list of numbers you have. Your goal is to calculate the total points or the total number of scratchcards you end up with based on the rules mentioned.

### Part One

For each scratchcard, you earn points based on the number of matching winning numbers. The first match earns one point, and each subsequent match doubles the point value. Calculate the total points for all scratchcards.

### Part Two

Instead of points, scratchcards now allow you to win more scratchcards equal to the number of winning numbers you have. Copies of scratchcards are scored like normal scratchcards and have the same card number as the card they copied. This process repeats until no more copies can be won. Calculate the total number of scratchcards you end up with, including the original set.

## Input

The input consists of multiple scratchcards, each with two lists of numbers: winning numbers and numbers you have.

## Output

### Part One

Output the total points earned for all scratchcards.

### Part Two

Output the total number of scratchcards you end up with, including the original set.

## Example

### Part One

**Input:**
```
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
```

**Output:**
```
13
```

### Part Two

**Input:**
```
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
```

**Output:**
```
30
```

## Notes

- Ensure that your solution accounts for the rules mentioned in both parts of the problem.
- The provided examples are for illustration purposes; your solution should work for any valid input.