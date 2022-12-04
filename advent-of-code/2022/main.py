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

def day2_part1(data_file='data/day2.txt'):
    with open(data_file, 'r') as f:
        # Rock-paper-scissors symbols
        rps = ['A', 'B', 'C']
        xyz = ['X', 'Y', 'Z']
        rps_points = {'X': 1, 'Y': 2, 'Z': 3}
        
        # Head to head point calculation
        points = [3, 0, 6]
        h2h = {xyz[i]: {rps[(j + i) % 3]: points[j] for j in range(3)} for i in range(3)}
        
        # Total score
        score = 0
        matches = f.readlines()

        for m in matches:
            # Obtain opponent's and our decision
            op, dec = m.replace('\n', '').split(' ')
            score += h2h[dec][op] + rps_points[dec]

        return score


def day2_part2(data_file='data/day2.txt'):
    with open(data_file, 'r') as f:
        # Rock-paper-scissors symbols
        rps = ['A', 'B', 'C']
        xyz = ['X', 'Y', 'Z']
        rps_points = {'X': 1, 'Y': 2, 'Z': 3}
        
        # Head to head decision depending on result
        res_points = {'X': 0, 'Y': 3, 'Z': 6}
        h2h = {rps[i]: {xyz[j]: xyz[(j + i + 2) % 3] for j in range(3)} for i in range(3)}
        
        # Total score
        score = 0
        matches = f.readlines()

        for m in matches:
            # Obtain opponent decision and result
            op, res = m.replace('\n', '').split(' ')
            dec = h2h[op][res]
            score += res_points[res] + rps_points[dec]

        return score


def day3_part1(data_file='data/day3.txt'):
    with open(data_file, 'r') as f:
        rucksacks = f.readlines()
        prio = 0

        for r in rucksacks:
            r = r.replace('\n', '')
            # Divide in compartments
            c1, c2 = set(r[:len(r) // 2]), set(r[len(r) // 2:])

            # Search for item that appears in both
            item = list(c1 & c2)[0]

            # Update priority
            if ord(item) > ord('Z'):
                # Lower case
                prio += ord(item) - ord('a') + 1
            else:
                # Upper case
                prio += ord(item) - ord('A') + 27

        return prio


def day3_part2(data_file='data/day3.txt'):
    with open(data_file, 'r') as f:
        rucksacks = f.readlines()
        prio = 0
        groups = [(set(rucksacks[i*3].replace('\n', '')), 
                   set(rucksacks[i*3+1].replace('\n', '')), 
                   set(rucksacks[i*3+2].replace('\n', ''))) for i in range(len(rucksacks) // 3)]

        for e1, e2, e3 in groups:
            # Look for common in all three 
            item = list(e1 & e2 & e3)[0]

            # Update priority
            if ord(item) > ord('Z'):
                # Lower case
                prio += ord(item) - ord('a') + 1
            else:
                # Upper case
                prio += ord(item) - ord('A') + 27

        return prio


def day4_part1(data_file='data/day4.txt'):
    with open(data_file, 'r') as f:
        pairs = f.readlines()
        contained = 0
                                                                                
        for p in pairs:
            # Compare sections of Elf A and B
            sec_a, sec_b = p.replace('\n', '').split(',')

            lim_a = sec_a.split('-')
            lim_b = sec_b.split('-')
            
            # Check for overlapping of A in B
            if int(lim_a[0]) >= int(lim_b[0]) and int(lim_a[1]) <= int(lim_b[1]):
                contained += 1
            elif int(lim_b[0]) >= int(lim_a[0]) and int(lim_b[1]) <= int(lim_a[1]):
                contained += 1

        return contained


def day4_part2(data_file='data/day4.txt'):
    with open(data_file, 'r') as f:
        pairs = f.readlines()
        contained = 0
                                                                                
        for p in pairs:
            # Compare sections of Elf A and B
            sec_a, sec_b = p.replace('\n', '').split(',')

            lim_a = sec_a.split('-')
            lim_b = sec_b.split('-')
            
            # Check for containment 
            if int(lim_a[0]) >= int(lim_b[0]) and int(lim_a[1]) <= int(lim_b[1]):
                contained += 1
            elif int(lim_b[0]) >= int(lim_a[0]) and int(lim_b[1]) <= int(lim_a[1]):
                contained += 1
            elif int(lim_a[0]) <= int(lim_b[0]) and int(lim_a[1]) >= int(lim_b[0]):
                contained += 1
            elif int(lim_b[0]) <= int(lim_a[0]) and int(lim_b[1]) >= int(lim_a[0]):
                contained += 1

        return contained


if __name__ == '__main__':
    print('Result Day 1 Part 1: ', day1_part1())
    print('Result Day 1 Part 2: ', day1_part2())
    print('Result Day 2 Part 1: ', day2_part1())
    print('Result Day 2 Part 2: ', day2_part2())
    print('Result Day 3 Part 1: ', day3_part1())
    print('Result Day 3 Part 2: ', day3_part2())
    print('Result Day 4 Part 1: ', day4_part1())
    print('Result Day 4 Part 2: ', day4_part2())
