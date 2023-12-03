# Day 3: Gear Ratios

## Problem Description

You and the Elf find a gondola lift station, but it's not working. The engineer needs your help to find a missing engine part. The engine schematic is a visual representation with numbers adjacent to symbols being part numbers. Your task is to sum up all the part numbers.

### Example

Consider the following engine schematic:

```plaintext
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
```

In this example, the sum of all part numbers is 530849.

## Part Two

The engineer finds the missing part, but there's another issue: one of the gears in the engine is wrong. Gears are denoted by `*` symbols adjacent to exactly two part numbers. Your task now is to find the gear ratio of every gear (product of the two adjacent part numbers) and sum them up.

### Example

Consider the same engine schematic:

```plaintext
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
```

In this example, there are two gears. The first has part numbers 467 and 35, so its gear ratio is 16345. The second has part numbers 617 and 58, resulting in a gear ratio of 451490. Adding up all the gear ratios produces 84900879.

## Solution

### File Structure

```
.
├── day-03
│   ├── input.txt
│   ├── solution.py
│   └── README.md
```

### Files

#### `input.txt`

Contains the engine schematic for the day's puzzle.

#### `part1_solution.py`

Contains the Python code solving part one of the puzzle. It calculates the sum of all part numbers in the engine schematic.

#### `part2_solution.py`

Contains the Python code solving part two of the puzzle. It calculates the sum of all gear ratios in the engine schematic.

#### `README.md`

Provides a detailed explanation of the puzzle and solutions for both parts.