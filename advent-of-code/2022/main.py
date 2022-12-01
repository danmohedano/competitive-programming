import numpy as np


TEST_FILE = 'data/test.txt'


def day1_part1(data_file='data/day1.txt'):
    with open(data_file, 'r') as f:
        calories = f.readlines()
        max_calories = 0
        current_calories = 0

        for item in calories:
            if item == '\n':
                # Store max amount of calories
                max_calories = max(max_calories, current_calories)
                current_calories = 0
            else:
                current_calories += int(item)

        # One last comparison in case the last elf is the max
        max_calories = max(max_calories, current_calories)

        return max_calories


def day1_part2(data_file='data/day1.txt'):
    with open(data_file, 'r') as f:
        calories = f.readlines()
        max_calories = [0, 0, 0]
        current_calories = 0

        for item in calories:
            if item == '\n':
                # Compare amount with smallest of top3
                max_calories[0] = max(max_calories[0], current_calories)
                max_calories = sorted(max_calories)
                current_calories = 0
            else:
                current_calories += int(item)

        # Last comparison in case the last elf is in top3
        max_calories[0] = max(max_calories[0], current_calories)

        return sum(max_calories)


if __name__ == '__main__':
    print('Result Day 1 Part 1: ', day1_part1())
    print('Result Day 1 Part 2: ', day1_part2())
