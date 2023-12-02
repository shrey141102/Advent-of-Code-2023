# Cube Bag Game Solver

This is a Python script to solve the Elf's cube bag game puzzle. The puzzle involves analyzing recorded games where the Elf reveals subsets of cubes from a bag. Two questions need to be answered:

## Question 1: Determine Possible Games

The first question asks which games would have been possible if the bag had been loaded with specific cube quantities. The script reads the recorded games, checks if each game is possible with the given cube quantities, and calculates the sum of the IDs of possible games.

### Usage
```bash
python game_solver.py input.txt
```

Replace `input.txt` with the actual path to your input file.

## Question 2: Find Minimum Set of Cubes

The second question asks for the minimum set of cubes that could have been in the bag for each game. The script calculates the minimum cube set for each game and then sums up the powers of these sets.

### Usage
```bash
python game_solver.py input.txt --part two
```

Replace `input.txt` with the actual path to your input file.

## Input Format
The input file should contain the recorded games in the specified format, similar to the provided example. Each line represents a game with its ID and the subsets of cubes revealed in semicolon-separated format.

### Example Input
```plaintext
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
```

## Output
The script outputs the answer to each question.

### Example Output
```plaintext
Part One Answer: 2162
Part Two Answer: 72513
```

Feel free to use this script to solve the Elf's cube bag game puzzle and enjoy your journey to the water source!