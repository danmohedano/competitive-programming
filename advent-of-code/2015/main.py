import numpy as np


TEST_FILE = 'data/test.txt'


def day1_part1(data_file='data/day1.txt'):
    with open(data_file, 'r') as f:
        line = f.readlines()[0]
        floor = 0

        for c in line:
            floor += 1 if c == '(' else -1

        return floor


def day1_part2(data_file='data/day1.txt'):
    with open(data_file, 'r') as f:
        line = f.readlines()[0]
        floor = 0
        pos = 0

        for c in line:
            floor += 1 if c == '(' else -1
            pos += 1
            if floor < 0:
                break

        return pos


def day2_part1(data_file='data/day2.txt'):
    with open(data_file, 'r') as f:
        lines = f.readlines()
        total = 0

        for l in lines:
            dims = [int(x) for x in l.split('x')]
            areas = [dims[0]*dims[1], dims[0]*dims[2], dims[1]*dims[2]]
            total += (sum(areas) * 2) + min(areas)

        return total

def day2_part2(data_file='data/day2.txt'):
    with open(data_file, 'r') as f:
        lines = f.readlines()
        total = 0

        for l in lines:
            dims = sorted([int(x) for x in l.split('x')])
            wrap = 2 * (dims[0] + dims[1])
            bow = dims[0] * dims[1] * dims[2]

            total += wrap + bow

        return total        


if __name__ == '__main__':
    print('Result Day 1 Part 1: ', day1_part1())
    print('Result Day 1 Part 2: ', day1_part2())
    print('Result Day 2 Part 1: ', day2_part1())
    print('Result Day 2 Part 2: ', day2_part2())
