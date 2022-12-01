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


def day3_part1(data_file='data/day3.txt'):
    with open(data_file, 'r') as f:
        line = f.readlines()[0]

        houses = set()
        pos = (0, 0)
        houses.add(pos)

        for c in line:
            new_pos = [pos[0], pos[1]]
            if c == '>':
                new_pos[0] += 1
            elif c == '<':
                new_pos[0] -= 1
            elif c == 'v':
                new_pos[1] += 1
            else:
                new_pos[1] -= 1

            pos = tuple(new_pos)
            houses.add(pos)

        return len(houses)


def day3_part2(data_file='data/day3.txt'):
    with open(data_file, 'r') as f:
        line = f.readlines()[0]

        houses = set()
        pos = [(0, 0), (0, 0)]
        santa = 0
        houses.add(pos[0])

        for c in line:
            new_pos = [pos[santa][0], pos[santa][1]]
            if c == '>':
                new_pos[0] += 1
            elif c == '<':
                new_pos[0] -= 1
            elif c == 'v':
                new_pos[1] += 1
            else:
                new_pos[1] -= 1

            pos[santa] = tuple(new_pos)
            houses.add(pos[santa])
            santa = (santa + 1) % 2

        return len(houses)


if __name__ == '__main__':
    print('Result Day 1 Part 1: ', day1_part1())
    print('Result Day 1 Part 2: ', day1_part2())
    print('Result Day 2 Part 1: ', day2_part1())
    print('Result Day 2 Part 2: ', day2_part2())
    print('Result Day 3 Part 1: ', day3_part1())
    print('Result Day 3 Part 2: ', day3_part2())
