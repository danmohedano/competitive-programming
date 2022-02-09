import numpy as np


TEST_FILE = 'data/test.txt'


def day1_part1(data_file='data/day1.txt'):
    with open(data_file, 'r') as f:
        depths = f.readlines()
        depths = [int(x.replace('\n', '')) for x in depths]

        increases = 0
        for i in range(1, len(depths)):
            if depths[i] > depths[i - 1]:
                increases += 1

        return increases


def day1_part2(data_file='data/day1.txt'):
    with open(data_file, 'r') as f:
        depths = f.readlines()
        depths = [int(x.replace('\n', '')) for x in depths]

        increases = 0
        for i in range(1, len(depths) - 2):
            if depths[i + 2] > depths[i - 1]:
                increases += 1

        return increases


def day2_part1(data_file='data/day2.txt'):
    with open(data_file, 'r') as f:
        commands = f.readlines()
        commands = [c.replace('\n', '').split(' ') for c in commands]

        depth = 0
        horizontal = 0
        for c, val in commands:
            if c == 'forward':
                horizontal += int(val)
            elif c == 'down':
                depth += int(val)
            else:
                depth -= int(val)

        return depth * horizontal


def day2_part2(data_file='data/day2.txt'):
    with open(data_file, 'r') as f:
        commands = f.readlines()
        commands = [c.replace('\n', '').split(' ') for c in commands]

        depth = 0
        horizontal = 0
        aim = 0
        for c, val in commands:
            if c == 'forward':
                horizontal += int(val)
                depth += (aim*int(val))
            elif c == 'down':
                aim += int(val)
            else:
                aim -= int(val)

        return depth * horizontal


def day3_part1(data_file='data/day3.txt'):
    with open(data_file, 'r') as f:
        numbers = f.readlines()
        numbers = [np.array([-1 + 2*int(c) for c in n.replace('\n', '')]) for n in numbers]
        
        sum = np.zeros(len(numbers[0]))

        for n in numbers:
            sum += n

        gamma_rate = 0
        epsilon_rate = 0
        
        for i in range(len(sum)):
            if sum[i] > 0:
                gamma_rate = gamma_rate * 2 + 1
                epsilon_rate *= 2
            else:
                gamma_rate *= 2
                epsilon_rate = epsilon_rate * 2 + 1

        return gamma_rate * epsilon_rate       


def _sum_vectors(numbers):
    sum = np.zeros(len(numbers[0]))

    for n in numbers:
        sum += n
    
    return sum


def day3_part2(data_file='data/day3.txt'):
    with open(data_file, 'r') as f:
        numbers = f.readlines()
        numbers = [np.array([-1 + 2*int(c) for c in n.replace('\n', '')]) for n in numbers]
        
        sum = _sum_vectors(numbers)

        # Oxygen Rating
        oxygen_nums = numbers.copy()
        bit = 0

        while len(oxygen_nums) != 1:
            oxygen_nums = [n for n in oxygen_nums if (sum[bit] == 0 and n[bit] == 1) or (n[bit] == np.sign(sum[bit]))]
            sum = _sum_vectors(oxygen_nums)
            bit += 1
            

        # CO2 Rating
        co2_nums = numbers.copy()
        bit = 0

        sum = _sum_vectors(numbers)

        while len(co2_nums) != 1:
            co2_nums = [n for n in co2_nums if (sum[bit] == 0 and n[bit] == -1) or (n[bit] == (-1)*np.sign(sum[bit]))]
            sum = _sum_vectors(co2_nums)
            bit += 1

        oxygen_rate = int(''.join([str(c) for c in oxygen_nums[0]]).replace('-1', '0'), 2)
        co2_rate = int(''.join([str(c) for c in co2_nums[0]]).replace('-1', '0'), 2)

        return oxygen_rate*co2_rate


def _check_bingo(table, row, col):
    flag_col, flag_row = True, True

    # Check all rows of col
    for i in range(table.shape[0]):
        if table[i][col] == 0:
            flag_col = False

    # Check all columns in row
    for j in range(table.shape[1]):
        if table[row][j] == 0:
            flag_row = False

    return flag_col or flag_row


def _sum_unmarked(table, table_marks):
    sum = 0
    for i in range(table.shape[0]):
        for j in range(table.shape[1]):
            if table_marks[i][j] == 0:
                sum += table[i][j]

    return sum


def day4_part1(data_file='data/day4.txt'):
    with open(data_file, 'r') as f:
        data = f.readlines()
        
        # Random numbers
        order = [int(n) for n in data[0].replace('\n', '').split(',')]
        
        # Load boards
        boards = []
        board_dicts = []
        board_marks = []

        for b_i in range(2, len(data), 6):
            board = np.zeros([5, 5])
            board_mark = np.zeros([5, 5])
            board_dict = {}

            for row_i, row in enumerate(data[b_i:b_i + 6]):
                for col_i, ele in enumerate(row.replace('\n', '').split()):
                    board[row_i][col_i] = int(ele)
                    board_dict[int(ele)] = (row_i, col_i)

            boards.append(board)
            board_dicts.append(board_dict)
            board_marks.append(board_mark)

        # Iterate through numbers
        for n in order:
            # Iterate through boards
            for b, b_dict, b_mark in zip(boards, board_dicts, board_marks):
                # If number in bingo card
                if n in b_dict:
                    pos_x, pos_y = b_dict[n]
                    b_mark[pos_x][pos_y] = 1
                    if _check_bingo(b_mark, pos_x, pos_y):
                        return int(_sum_unmarked(b, b_mark) * n)

        return None


def day4_part2(data_file='data/day4.txt'):
    with open(data_file, 'r') as f:
        data = f.readlines()
        
        # Random numbers
        order = [int(n) for n in data[0].replace('\n', '').split(',')]
        
        # Load boards
        boards = []
        board_dicts = []
        board_marks = []

        for b_i in range(2, len(data), 6):
            board = np.zeros([5, 5])
            board_mark = np.zeros([5, 5])
            board_dict = {}

            for row_i, row in enumerate(data[b_i:b_i + 6]):
                for col_i, ele in enumerate(row.replace('\n', '').split()):
                    board[row_i][col_i] = int(ele)
                    board_dict[int(ele)] = (row_i, col_i)

            boards.append(board)
            board_dicts.append(board_dict)
            board_marks.append(board_mark)

        # Iterate through numbers
        won_boards = []
        total_boards = len(boards)
        for n in order:
            # Iterate through boards
            for b_i, (b, b_dict, b_mark) in enumerate(zip(boards, board_dicts, board_marks)):
                # If number in bingo card
                if n in b_dict:
                    pos_x, pos_y = b_dict[n]
                    b_mark[pos_x][pos_y] = 1
                    if _check_bingo(b_mark, pos_x, pos_y) and b_i not in won_boards:
                        won_boards.append(b_i)

                    if len(won_boards) == total_boards:
                        return int(n * _sum_unmarked(b, b_mark))

        return None


def day5_part1(data_file='data/day5.txt'):
    with open(data_file, 'r') as f:
        data = f.readlines()
        
        grid = np.zeros([1000, 1000])
        overlaps = 0

        for line in data:
            p1, p2 = line.replace('\n', '').split(' -> ')
            p1 = [int(x) for x in p1.split(',')]
            p2 = [int(x) for x in p2.split(',')]

            # Ignore diagonal lines
            if p1[0] != p2[0] and p1[1] != p2[1]:
                continue

            for i in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
                for j in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
                    if grid[i][j] == 1:
                        overlaps += 1
                    grid[i][j] += 1

        return overlaps


def day5_part2(data_file='data/day5.txt'):
    with open(data_file, 'r') as f:
        data = f.readlines()

        grid = np.zeros([1000, 1000])
        overlaps = 0

        for line in data:
            p1, p2 = line.replace('\n', '').split(' -> ')
            p1 = [int(x) for x in p1.split(',')]
            p2 = [int(x) for x in p2.split(',')]

            n_points = max(abs(p1[0] - p2[0]) + 1, abs(p1[1] - p2[1]) + 1)
            sign_x = np.sign(p2[0] - p1[0])
            sign_y = np.sign(p2[1] - p1[1])
            if sign_x == 0:
                sign_x = 1
            if sign_y == 0:
                sign_y = 1
            x_points = list(range(p1[0], p2[0] + sign_x, sign_x))
            y_points = list(range(p1[1], p2[1] + sign_y, sign_y))

            if len(x_points) == 1:
                x_points *= n_points
            if len(y_points) == 1:
                y_points *= n_points

            for i, j in zip(x_points, y_points):
                if grid[j][i] == 1:
                    overlaps += 1
                grid[j][i] += 1

        return overlaps


def day6_part1(data_file='data/day6.txt'):
    with open(data_file, 'r') as f:
        data = f.readlines()
        
        ages = {i: 0 for i in range(9)}

        for age in data[0].replace('\n', '').split(','):
            ages[int(age)] += 1

        for _ in range(80):
            # Evolution each day: decrease every age by 1, 
            prev = 0
            for j in range(8, -1, -1):
                prev, ages[j] = ages[j], prev

            # Ages 0 reproduce
            ages[6] += prev
            ages[8] += prev
        
        return sum(ages.values())


def day6_part2(data_file='data/day6.txt'):
    with open(data_file, 'r') as f:
        data = f.readlines()
        
        ages = {i: 0 for i in range(9)}

        for age in data[0].replace('\n', '').split(','):
            ages[int(age)] += 1

        for _ in range(256):
            # Evolution each day: decrease every age by 1, 
            prev = 0
            for j in range(8, -1, -1):
                prev, ages[j] = ages[j], prev

            # Ages 0 reproduce
            ages[6] += prev
            ages[8] += prev
        
        return sum(ages.values())


def day7_part1(data_file='data/day7.txt'):
    with open(data_file, 'r') as f:
        data = f.readlines()
        
        positions = {}

        for pos in data[0].replace('\n', '').split(','):
            pos = int(pos)
            if pos in positions:
                positions[pos] += 1
            else:
                positions[pos] = 1

        min_fuel = np.inf
        for i in range(min(positions.keys()), max(positions.keys()) + 1):
            fuel = 0
            for pos, n in positions.items():
                fuel += (abs(i - pos) * n)

            min_fuel = min(fuel, min_fuel)

        return min_fuel        


def day7_part2(data_file='data/day7.txt'):
    with open(data_file, 'r') as f:
        data = f.readlines()
        
        positions = {}

        for pos in data[0].replace('\n', '').split(','):
            pos = int(pos)
            if pos in positions:
                positions[pos] += 1
            else:
                positions[pos] = 1

        min_fuel = np.inf
        for i in range(min(positions.keys()), max(positions.keys()) + 1):
            fuel = 0
            for pos, n in positions.items():
                dist = abs(i - pos)
                fuel += (dist * (dist + 1) // 2 * n)

            min_fuel = min(fuel, min_fuel)

        return min_fuel 


def day8_part1(data_file='data/day8.txt'):
    with open(data_file, 'r') as f:
        data = f.readlines()
        """
        0 - 6 : abcefg
        1 - 2 : cf (unique)
        2 - 5 : acdeg
        3 - 5 : acdfg
        4 - 4 : bcdf (unique)
        5 - 5 : abdfg
        6 - 6 : abdefg
        7 - 3 : acf (unique)
        8 - 7 : abcdefg (unique)
        9 - 6 : abcdfg
        """
        appearances = 0
        for line in data:
            patterns, output = line.replace('\n', '').split(' | ')
            for n in output.split(' '):
                if len(n) in [2, 4, 3, 7]:
                    appearances += 1

        return appearances


def _infer_digit(a, cf, bd, digit):
    length = len(digit)
    if length == 2:
        return "1"
    elif length == 3:
        return "7"
    elif length == 4:
        return "4"
    elif length == 7:
        return "8"

    if length == 6:
        # 0, 6, 9
        if bd[0] not in digit or bd[1] not in digit:
            return "0"
        elif cf[0] not in digit or cf[1] not in digit:
            return "6"
        else:
            return "9"
    else:
        # 2, 3, 5
        if bd[0] in digit and bd[1] in digit:
            return "5"
        elif cf[0] in digit and cf[1] in digit:
            return "3"
        else:
            return "2"


def day8_part2(data_file='data/day8.txt'):
    with open(data_file, 'r') as f:
        data = f.readlines()
        """
        0 - 6 : abcefg
        1 - 2 : cf (unique)
        2 - 5 : acdeg
        3 - 5 : acdfg
        4 - 4 : bcdf (unique)
        5 - 5 : abdfg
        6 - 6 : abdefg
        7 - 3 : acf (unique)
        8 - 7 : abcdefg (unique)
        9 - 6 : abcdfg
        """
        sum_outputs = 0
        for line in data:
            patterns, output = line.replace('\n', '').split(' | ')
            output_value = []

            patterns_dict = {i: [] for i in [2, 3, 4, 5, 6, 7]}

            for p in patterns.split(' '):
                patterns_dict[len(p)].append(p)

            a = [x for x in patterns_dict[3][0] if x not in patterns_dict[2][0]]
            cf = [x for x in patterns_dict[2][0]]
            bd = [x for x in patterns_dict[4][0] if x not in patterns_dict[2][0]]

            for out in output.split(' '):
                output_value.append(_infer_digit(a, cf, bd, out))

            sum_outputs += int(''.join(output_value))

        return sum_outputs


if __name__ == '__main__':
    print('Result Day 1 Part 1: ', day1_part1())
    print('Result Day 1 Part 2: ', day1_part2())
    print('Result Day 2 Part 1: ', day2_part1())
    print('Result Day 2 Part 2: ', day2_part2())
    print('Result Day 3 Part 1: ', day3_part1())
    print('Result Day 3 Part 2: ', day3_part2())
    print('Result Day 4 Part 1: ', day4_part1())
    print('Result Day 4 Part 2: ', day4_part2())
    print('Result Day 5 Part 1: ', day5_part1())
    print('Result Day 5 Part 2: ', day5_part2())
    print('Result Day 6 Part 1: ', day6_part1())
    print('Result Day 6 Part 2: ', day6_part2())
    print('Result Day 7 Part 1: ', day7_part1())
    print('Result Day 7 Part 2: ', day7_part2())
    print('Result Day 8 Part 1: ', day8_part1())
    print('Result Day 8 Part 2: ', day8_part2())
