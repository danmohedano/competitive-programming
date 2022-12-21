import numpy as np
import queue
import functools


TEST_FILE = "data/test.txt"


def day1_part1(data_file="data/day1.txt"):
    with open(data_file, "r") as f:
        calories = f.readlines()
        max_calories = 0
        current_calories = 0

        for item in calories:
            if item == "\n":
                # Store max amount of calories
                max_calories = max(max_calories, current_calories)
                current_calories = 0
            else:
                current_calories += int(item)

        # One last comparison in case the last elf is the max
        max_calories = max(max_calories, current_calories)

        return max_calories


def day1_part2(data_file="data/day1.txt"):
    with open(data_file, "r") as f:
        calories = f.readlines()
        max_calories = [0, 0, 0]
        current_calories = 0

        for item in calories:
            if item == "\n":
                # Compare amount with smallest of top3
                max_calories[0] = max(max_calories[0], current_calories)
                max_calories = sorted(max_calories)
                current_calories = 0
            else:
                current_calories += int(item)

        # Last comparison in case the last elf is in top3
        max_calories[0] = max(max_calories[0], current_calories)

        return sum(max_calories)


def day2_part1(data_file="data/day2.txt"):
    with open(data_file, "r") as f:
        # Rock-paper-scissors symbols
        rps = ["A", "B", "C"]
        xyz = ["X", "Y", "Z"]
        rps_points = {"X": 1, "Y": 2, "Z": 3}

        # Head to head point calculation
        points = [3, 0, 6]
        h2h = {
            xyz[i]: {rps[(j + i) % 3]: points[j] for j in range(3)}
            for i in range(3)
        }

        # Total score
        score = 0
        matches = f.readlines()

        for m in matches:
            # Obtain opponent's and our decision
            op, dec = m.replace("\n", "").split(" ")
            score += h2h[dec][op] + rps_points[dec]

        return score


def day2_part2(data_file="data/day2.txt"):
    with open(data_file, "r") as f:
        # Rock-paper-scissors symbols
        rps = ["A", "B", "C"]
        xyz = ["X", "Y", "Z"]
        rps_points = {"X": 1, "Y": 2, "Z": 3}

        # Head to head decision depending on result
        res_points = {"X": 0, "Y": 3, "Z": 6}
        h2h = {
            rps[i]: {xyz[j]: xyz[(j + i + 2) % 3] for j in range(3)} for i in range(3)
        }

        # Total score
        score = 0
        matches = f.readlines()

        for m in matches:
            # Obtain opponent decision and result
            op, res = m.replace("\n", "").split(" ")
            dec = h2h[op][res]
            score += res_points[res] + rps_points[dec]

        return score


def day3_part1(data_file="data/day3.txt"):
    with open(data_file, "r") as f:
        rucksacks = f.readlines()
        prio = 0

        for r in rucksacks:
            r = r.replace("\n", "")
            # Divide in compartments
            c1, c2 = set(r[: len(r) // 2]), set(r[len(r) // 2 :])

            # Search for item that appears in both
            item = list(c1 & c2)[0]

            # Update priority
            if ord(item) > ord("Z"):
                # Lower case
                prio += ord(item) - ord("a") + 1
            else:
                # Upper case
                prio += ord(item) - ord("A") + 27

        return prio


def day3_part2(data_file="data/day3.txt"):
    with open(data_file, "r") as f:
        rucksacks = f.readlines()
        prio = 0
        groups = [
            (
                set(rucksacks[i * 3].replace("\n", "")),
                set(rucksacks[i * 3 + 1].replace("\n", "")),
                set(rucksacks[i * 3 + 2].replace("\n", "")),
            )
            for i in range(len(rucksacks) // 3)
        ]

        for e1, e2, e3 in groups:
            # Look for common in all three
            item = list(e1 & e2 & e3)[0]

            # Update priority
            if ord(item) > ord("Z"):
                # Lower case
                prio += ord(item) - ord("a") + 1
            else:
                # Upper case
                prio += ord(item) - ord("A") + 27

        return prio


def day4_part1(data_file="data/day4.txt"):
    with open(data_file, "r") as f:
        pairs = f.readlines()
        contained = 0

        for p in pairs:
            # Compare sections of Elf A and B
            sec_a, sec_b = p.replace("\n", "").split(",")

            lim_a = sec_a.split("-")
            lim_b = sec_b.split("-")

            # Check for overlapping of A in B
            if int(lim_a[0]) >= int(lim_b[0]) and int(lim_a[1]) <= int(lim_b[1]):
                contained += 1
            elif int(lim_b[0]) >= int(lim_a[0]) and int(lim_b[1]) <= int(lim_a[1]):
                contained += 1

        return contained


def day4_part2(data_file="data/day4.txt"):
    with open(data_file, "r") as f:
        pairs = f.readlines()
        contained = 0

        for p in pairs:
            # Compare sections of Elf A and B
            sec_a, sec_b = p.replace("\n", "").split(",")

            lim_a = sec_a.split("-")
            lim_b = sec_b.split("-")

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


def day5_part1(data_file="data/day5.txt"):
    with open(data_file, "r") as f:
        arrangement = f.readlines()
        n_stacks = 0

        # Read number of stacks
        for l in arrangement:
            if "[" not in l:
                no_space = " ".join(l.split())
                n_stacks = max([int(x) for x in no_space.split(" ")])
                break

        stacks = [[] for i in range(n_stacks)]

        # Read stacks
        for l in arrangement:
            if "[" not in l:
                break

            for i in range(n_stacks):
                # Read crate of each stack (if there is one)
                if l[i * 4] == "[":
                    stacks[i].insert(0, l[i * 4 + 1])

        # Read instructions
        for l in arrangement:
            if "move" in l:
                n_moved, origin, dest = [
                    int(x)
                    for x in l.replace(" ", "")
                    .replace("move", "")
                    .replace("from", ",")
                    .replace("to", ",")
                    .split(",")
                ]
                # Correct indices
                origin -= 1
                dest -= 1
                # Move crates from origin to destination
                stacks[dest] += reversed(
                    stacks[origin][len(stacks[origin]) - n_moved :]
                )
                stacks[origin] = stacks[origin][: len(stacks[origin]) - n_moved]

        top_stacks = ""
        for s in stacks:
            if len(s) > 0:
                top_stacks += s[-1]

        return top_stacks


def day5_part2(data_file="data/day5.txt"):
    with open(data_file, "r") as f:
        arrangement = f.readlines()
        n_stacks = 0

        # Read number of stacks
        for l in arrangement:
            if "[" not in l:
                no_space = " ".join(l.split())
                n_stacks = max([int(x) for x in no_space.split(" ")])
                break

        stacks = [[] for i in range(n_stacks)]

        # Read stacks
        for l in arrangement:
            if "[" not in l:
                break

            for i in range(n_stacks):
                # Read crate of each stack (if there is one)
                if l[i * 4] == "[":
                    stacks[i].insert(0, l[i * 4 + 1])

        # Read instructions
        for l in arrangement:
            if "move" in l:
                n_moved, origin, dest = [
                    int(x)
                    for x in l.replace(" ", "")
                    .replace("move", "")
                    .replace("from", ",")
                    .replace("to", ",")
                    .split(",")
                ]
                # Correct indices
                origin -= 1
                dest -= 1
                # Move crates from origin to destination
                stacks[dest] += stacks[origin][len(stacks[origin]) - n_moved:]
                stacks[origin] = stacks[origin][: len(stacks[origin]) - n_moved]

        top_stacks = ""
        for s in stacks:
            if len(s) > 0:
                top_stacks += s[-1]

        return top_stacks


def day6_part1(data_file="data/day6.txt"):
    with open(data_file, "r") as f:
        datastream = f.readlines()[0].replace("\n", "")
        header = []

        for marker in range(len(datastream)):
            c = datastream[marker]
            if c not in header:
                header.append(c)
                if len(header) == 4:
                    return marker + 1
            else:
                new_start = header.index(c)
                header = header[new_start + 1:]
                header.append(c)

        return 0


def day6_part2(data_file="data/day6.txt"):
    with open(data_file, "r") as f:
        datastream = f.readlines()[0].replace("\n", "")
        header = []

        for marker in range(len(datastream)):
            c = datastream[marker]
            if c not in header:
                header.append(c)
                if len(header) == 14:
                    return marker + 1
            else:
                new_start = header.index(c)
                header = header[new_start + 1:]
                header.append(c)

        return 0


def get_dir(tree, dirs):
    final_dir = tree["/"]["content"]
    for d in dirs:
        final_dir = final_dir[d]["content"]

    return final_dir


def add_dir(tree, pwd, new_dir):
    parent = get_dir(tree, pwd)
    parent[new_dir] = {"content": {}, "size": 0}


def add_file(tree, pwd, size, name):
    parent = get_dir(tree, pwd)
    parent[name] = {"size": size}


def calc_sizes_recursive(current_dir):
    for ele in current_dir["content"]:
        if "content" in current_dir["content"][ele]:
            # Recursively go into sub-dir
            current_dir["size"] += calc_sizes_recursive(current_dir["content"][ele])
        else:
            # If file, just update size
            current_dir["size"] += current_dir["content"][ele]["size"]

    return current_dir["size"]


def calc_sizes(tree):
    tree["/"]["size"] = calc_sizes_recursive(tree["/"])


def find_limited_dirs_max(current_dir, max_size):
    sizes = []
    if current_dir["size"] <= max_size:
        sizes.append(current_dir["size"])

    # Iterate through contained dirs
    for ele in current_dir["content"]:
        if "content" in current_dir["content"][ele]:
            # If sub-dir, check size
            sizes += find_limited_dirs_max(current_dir["content"][ele], max_size)

    return sizes


def day7_part1(data_file="data/day7.txt"):
    with open(data_file, "r") as f:
        commands = f.readlines()
        # Tree definition: {'dir_name': {'content': {'dir_name': ...}, 'size': x}
        # File definition: 'file_name': {'size': x}

        global_tree = {"/": {"content": {}, "size": 0}}
        path = []

        # Build directory tree
        for c in commands:
            tokens = c.replace("\n", "").split(" ")
            if tokens[0] == "$":
                # Shell command
                if tokens[1] == "cd":
                    # cd command
                    new_dir = tokens[2]
                    if new_dir == "/":
                        path = []
                    elif new_dir == "..":
                        path = path[:-1]
                    elif new_dir not in path:
                        add_dir(global_tree, path, new_dir)
                        path.append(new_dir)
                    else:
                        path.append(new_dir)
                else:
                    # ls command does nothing
                    continue
            elif tokens[0] == "dir":
                # Directory definition
                new_dir = tokens[1]
                add_dir(global_tree, path, new_dir)
            else:
                # File definition
                add_file(global_tree, path, int(tokens[0]), tokens[1])

        calc_sizes(global_tree)
        sizes = find_limited_dirs_max(global_tree["/"], 100000)
        return sum(sizes)


def find_limited_dirs_min(current_dir, min_size):
    sizes = []
    if current_dir["size"] >= min_size:
        sizes.append(current_dir["size"])

    # Iterate through contained dirs
    for ele in current_dir["content"]:
        if "content" in current_dir["content"][ele]:
            # If sub-dir, check size
            sizes += find_limited_dirs_min(current_dir["content"][ele], min_size)

    return sizes


def day7_part2(data_file="data/day7.txt"):
    with open(data_file, "r") as f:
        commands = f.readlines()
        # Tree definition: {'dir_name': {'content': {'dir_name': ...}, 'size': x}
        # File definition: 'file_name': {'size': x}

        global_tree = {"/": {"content": {}, "size": 0}}
        path = []

        # Build directory tree
        for c in commands:
            tokens = c.replace("\n", "").split(" ")
            if tokens[0] == "$":
                # Shell command
                if tokens[1] == "cd":
                    # cd command
                    new_dir = tokens[2]
                    if new_dir == "/":
                        path = []
                    elif new_dir == "..":
                        path = path[:-1]
                    elif new_dir not in path:
                        add_dir(global_tree, path, new_dir)
                        path.append(new_dir)
                    else:
                        path.append(new_dir)
                else:
                    # ls command does nothing
                    continue
            elif tokens[0] == "dir":
                # Directory definition
                new_dir = tokens[1]
                add_dir(global_tree, path, new_dir)
            else:
                # File definition
                add_file(global_tree, path, int(tokens[0]), tokens[1])

        calc_sizes(global_tree)
        needed_space = 30000000
        free_space = 70000000 - global_tree["/"]["size"]
        sizes = find_limited_dirs_min(global_tree["/"], needed_space - free_space)
        return min(sizes)


def day8_part1(data_file="data/day8.txt"):
    with open(data_file, "r") as f:
        trees = f.readlines()
        trees = np.array([[int(t) for t in x.replace("\n", "")] for x in trees])
        grid = np.zeros(trees.shape)
        grid[0, :] = 1
        grid[-1, :] = 1
        grid[:, 0] = 1
        grid[:, -1] = 1

        # Iterate through all trees to check
        for i in range(1, trees.shape[0] - 1):
            for j in range(1, trees.shape[1] - 1):
                tree = trees[i][j]
                if (
                    max(trees[i, j + 1:]) < tree
                    or max(trees[i, :j]) < tree
                    or max(trees[:i, j]) < tree
                    or max(trees[i + 1:, j]) < tree
                ):
                    grid[i, j] = 1

        return int(np.sum(grid))


def trees_seen(los, tree):
    seen = 0
    for i in range(len(los)):
        seen += 1
        if los[i] >= tree:
            break

    return seen


def day8_part2(data_file="data/day8.txt"):
    with open(data_file, "r") as f:
        trees = f.readlines()
        trees = np.array([[int(t) for t in x.replace("\n", "")] for x in trees])
        grid = np.zeros(trees.shape)

        # Iterate through all trees to check
        for i in range(1, trees.shape[0] - 1):
            for j in range(1, trees.shape[1] - 1):
                tree = trees[i][j]
                score_up = trees_seen(np.flip(trees[:i, j]), tree)
                score_down = trees_seen(trees[i + 1:, j], tree)
                score_right = trees_seen(trees[i, j + 1:], tree)
                score_left = trees_seen(np.flip(trees[i, :j]), tree)
                grid[i][j] = score_up * score_down * score_right * score_left

        return int(np.max(grid))


def day9_part1(data_file="data/day9.txt"):
    with open(data_file, "r") as f:
        moves = f.readlines()

        visited_positions = [[0, 0]]
        head = np.array([0, 0])
        tail = np.array([0, 0])

        dir_vecs = {'L': np.array([-1, 0]), 'R': np.array([1, 0]),
                    'U': np.array([0, 1]), 'D': np.array([0, -1])}

        for move in moves:
            direction, count = move.replace("\n", "").split(" ")
            count = int(count)
            update = dir_vecs[direction]

            for _ in range(count):
                # Repeat move n times
                head += update

                # Check if tail needs repositioning
                if max(abs(head - tail)) > 1:
                    # Check repositioning vector
                    sign_vec = np.sign(head - tail)
                    tail += sign_vec

                    if list(tail) not in visited_positions:
                        visited_positions.append(list(tail))

        return len(visited_positions)


def day9_part2(data_file="data/day9.txt"):
    with open(data_file, "r") as f:
        moves = f.readlines()

        visited_positions = [[0, 0]]
        knots = [np.array([0, 0]) for i in range(10)]

        dir_vecs = {'L': np.array([-1, 0]), 'R': np.array([1, 0]),
                    'U': np.array([0, 1]), 'D': np.array([0, -1])}

        for move in moves:
            direction, count = move.replace("\n", "").split(" ")
            count = int(count)
            update = dir_vecs[direction]

            for _ in range(count):
                # Repeat move n times
                knots[0] += update

                # Check if tails need repositioning
                for i in range(9):
                    head = knots[i]
                    tail = knots[i + 1]
                    if max(abs(head - tail)) > 1:
                        # Check repositioning vector
                        sign_vec = np.sign(head - tail)
                        tail += sign_vec

                        if i == 8 and list(tail) not in visited_positions:
                            visited_positions.append(list(tail))

        return len(visited_positions)


def day10_part1(data_file="data/day10.txt"):
    with open(data_file, "r") as f:
        instructions = f.readlines()
        reg = 1
        cycle = 1
        signal_strength = 0

        def check_cycle(cycle, reg):
            if (cycle - 20) % 40 == 0:
                return reg * cycle

            return 0

        for inst in instructions:
            inst = inst.replace("\n", "")
            if inst == 'noop':
                signal_strength += check_cycle(cycle, reg)
                cycle += 1
            else:
                value = int(inst.split(" ")[1])
                signal_strength += check_cycle(cycle, reg)
                cycle += 1
                signal_strength += check_cycle(cycle, reg)
                cycle += 1
                reg += value

        return signal_strength


def day10_part2(data_file="data/day10.txt"):
    with open(data_file, "r") as f:
        instructions = f.readlines()
        reg = 1
        cycle = 0

        def draw_crt(reg, cycle):
            print_pos = cycle % 40
            if print_pos == 0:
                print('\n', end='')
            if reg - 1 <= print_pos <= reg + 1:
                print('#', end='')
            else:
                print('.', end='')

        for inst in instructions:
            inst = inst.replace("\n", "")
            if inst == 'noop':
                draw_crt(reg, cycle)
                cycle += 1
            else:
                value = int(inst.split(" ")[1])
                draw_crt(reg, cycle)
                cycle += 1
                draw_crt(reg, cycle)
                cycle += 1
                reg += value

        print('\n', end='')
        return 0


def day11_part1(data_file="data/day11.txt"):
    with open(data_file, "r") as f:
        monkey_desc = f.readlines()

        class Monkey:
            def __init__(self):
                self.items = []
                self.operation = ""
                self.test = 0
                self.dest_true = 0
                self.dest_false = 0
                self.inspected = 0

        l_read = 0
        monkeys = []

        # Read monkey descriptions
        while l_read < len(monkey_desc):
            monkey = Monkey()
            items = monkey_desc[l_read + 1].replace('\n', '').split(':')[1].split(',')
            monkey.items = [int(x) for x in items]
            monkey.operation = monkey_desc[l_read + 2].replace('\n', '').split(':')[1].split('=')[1]
            monkey.test = int(monkey_desc[l_read + 3].replace('\n', '').split(':')[1].split(' ')[3])
            monkey.dest_true = int(monkey_desc[l_read + 4].replace('\n', '').split(':')[1].split(' ')[4])
            monkey.dest_false = int(monkey_desc[l_read + 5].replace('\n', '').split(':')[1].split(' ')[4])

            l_read += 7
            monkeys.append(monkey)

        # Rounds
        for _ in range(20):
            for m_idx in range(len(monkeys)):
                m = monkeys[m_idx]
                for old in m.items:
                    m.inspected += 1
                    new = eval(m.operation)
                    new = new // 3
                    if new % m.test == 0:
                        monkeys[m.dest_true].items.append(new)
                    else:
                        monkeys[m.dest_false].items.append(new)
                    
                # Remove items from monkey
                m.items = []

        inspected = sorted([m.inspected for m in monkeys])
        
        return inspected[-1] * inspected[-2]


def day11_part2(data_file="data/day11.txt"):
    with open(data_file, "r") as f:
        monkey_desc = f.readlines()

        class Monkey:
            def __init__(self):
                self.items = []
                self.operation = ""
                self.test = 0
                self.dest_true = 0
                self.dest_false = 0
                self.inspected = 0

        l_read = 0
        monkeys = []

        # Read monkey descriptions
        while l_read < len(monkey_desc):
            monkey = Monkey()
            items = monkey_desc[l_read + 1].replace('\n', '').split(':')[1].split(',')
            monkey.items = [int(x) for x in items]
            monkey.operation = monkey_desc[l_read + 2].replace('\n', '').split(':')[1].split('=')[1]
            monkey.test = int(monkey_desc[l_read + 3].replace('\n', '').split(':')[1].split(' ')[3])
            monkey.dest_true = int(monkey_desc[l_read + 4].replace('\n', '').split(':')[1].split(' ')[4])
            monkey.dest_false = int(monkey_desc[l_read + 5].replace('\n', '').split(':')[1].split(' ')[4])

            l_read += 7
            monkeys.append(monkey)

        # Compute LCM of all tests
        tests = [m.test for m in monkeys]
        lcm = int(np.lcm.reduce(tests))

        # Rounds
        for _ in range(10000):
            for m_idx in range(len(monkeys)):
                m = monkeys[m_idx]
                for old in m.items:
                    m.inspected += 1
                    new = eval(m.operation)
                    new = new % lcm
                    if new % m.test == 0:
                        monkeys[m.dest_true].items.append(new)
                    else:
                        monkeys[m.dest_false].items.append(new)
                    
                # Remove items from monkey
                m.items = []

        inspected = sorted([m.inspected for m in monkeys])
        
        return inspected[-1] * inspected[-2]


def day12_part1(data_file="data/day12.txt"):
    with open(data_file, "r") as f:
        map = [x.replace('\n', '') for x in f.readlines()]
        heights = [[0 for _ in range(len(map[0]))] for _ in range(len(map))]
        start = None
        end = None

        def valid_neighbors(node, heights):
            valid = []
            possible = []
            for i in range(-1, 2, 1):
                # Vertical
                v = (max(min(node[0] + i, len(heights) - 1), 0), node[1])
                # Horizontal
                h = (node[0], max(min(node[1] + i, len(heights[0]) - 1), 0))
                if v != node and v not in possible:
                    possible.append(v)
                if h != node and h not in possible:
                    possible.append(h)
        
            for n in possible:
                if heights[n[0]][n[1]] <= heights[node[0]][node[1]] + 1 and n not in valid:
                    valid.append(n)

            return valid

        # Read heights and starting/end points 
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == 'S':
                    heights[i][j] = 0
                    start = (i, j)
                elif map[i][j] == 'E':
                    heights[i][j] = ord('z') - ord('a')
                    end = (i, j)
                else:
                    heights[i][j] = ord(map[i][j]) - ord('a')

        # Perform dijkstra
        d_prev = {}
        d_dist = {}
        s = {}
        pq = queue.PriorityQueue() 

        # Initialize structures
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                d_prev[(i, j)] = None
                d_dist[(i, j)] = np.Inf
                s[(i, j)] = False

        # Push starting node to Queue
        d_dist[start] = 0
        pq.put((d_dist[start], start))

        # Dijkstra loop
        while not pq.empty():
            _, v = pq.get()
            if v == end:
                break
            if not s[v]:
                s[v] = True
                # If the node has not been checked 
                valid = valid_neighbors(v, heights)

                for next in valid:
                    # If better path found, update it
                    if d_dist[next] > d_dist[v] + 1:
                        d_dist[next] = d_dist[v] + 1
                        d_prev[next] = v
                        pq.put((d_dist[next], next))

        return d_dist[end]


def day12_part2(data_file="data/day12.txt"):
    with open(data_file, "r") as f:
        map = [x.replace('\n', '') for x in f.readlines()]
        heights = [[0 for _ in range(len(map[0]))] for _ in range(len(map))]
        possible_starts = []
        end = None

        def valid_neighbors(node, heights):
            valid = []
            possible = []
            for i in range(-1, 2, 1):
                # Vertical
                v = (max(min(node[0] + i, len(heights) - 1), 0), node[1])
                # Horizontal
                h = (node[0], max(min(node[1] + i, len(heights[0]) - 1), 0))
                if v != node and v not in possible:
                    possible.append(v)
                if h != node and h not in possible:
                    possible.append(h)
        
            for n in possible:
                if heights[n[0]][n[1]] <= heights[node[0]][node[1]] + 1 and n not in valid:
                    valid.append(n)

            return valid

        # Read heights and starting/end points 
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == 'S':
                    heights[i][j] = 0
                    possible_starts.append((i, j))
                elif map[i][j] == 'E':
                    heights[i][j] = ord('z') - ord('a')
                    end = (i, j)
                else:
                    heights[i][j] = ord(map[i][j]) - ord('a')
                    if heights[i][j] == 0:
                        possible_starts.append((i, j))

        # Iterate dijkstra for all possible starts
        shortest_path = np.Inf

        for start in possible_starts:
            # Perform dijkstra
            d_prev = {}
            d_dist = {}
            s = {}
            pq = queue.PriorityQueue() 

            # Initialize structures
            for i in range(len(heights)):
                for j in range(len(heights[0])):
                    d_prev[(i, j)] = None
                    d_dist[(i, j)] = np.Inf
                    s[(i, j)] = False

            # Push starting node to Queue
            d_dist[start] = 0
            pq.put((d_dist[start], start))

            # Dijkstra loop
            while not pq.empty():
                _, v = pq.get()
                if v == end:
                    break
                if not s[v]:
                    s[v] = True
                    # If the node has not been checked 
                    valid = valid_neighbors(v, heights)

                    for next in valid:
                        # If better path found, update it
                        if d_dist[next] > d_dist[v] + 1:
                            d_dist[next] = d_dist[v] + 1
                            d_prev[next] = v
                            pq.put((d_dist[next], next))

            shortest_path = min(shortest_path, d_dist[end])

        return shortest_path

def day13_compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif left == right: 
            return 0
        else:
            return -1
    elif isinstance(left, list) and isinstance(right, list):
        for i in range(min(len(left), len(right))): 
            res = day13_compare(left[i], right[i])
            if res == 0:
                continue
            else: 
                return res

        if len(left) < len(right):
            return 1
        elif len(left) == len(right):
            return 0
        else:
            return -1
    else:
        if isinstance(left, int): 
            return day13_compare([left], right)
        else:
            return day13_compare(left, [right])


def day13_part1(data_file="data/day13.txt"):
    with open(data_file, "r") as f:
        lines = f.readlines()
        correct_order = 0
 
        for i in range((len(lines) + 1) // 3):
            left = eval(lines[3 * i].replace('\n', ''))
            right = eval(lines[3 * i + 1].replace('\n', ''))

            if day13_compare(left, right) == 1:
                correct_order += (i + 1)

        return correct_order
            

def day13_part2(data_file="data/day13.txt"):
    with open(data_file, "r") as f:
        lines = f.readlines()
        packets = []
        packets.append([[2]])
        packets.append([[6]])
 
        for l in lines:
            if l != '\n':
                packets.append(eval(l.replace('\n', '')))

        sorted_packets = sorted(packets, reverse=True, key=functools.cmp_to_key(day13_compare))

        return (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)


def day14_sim_sand(start_x, grid):
    correct = True
    x, y = start_x, 0

    while True:
        # Go down
        try:
            if not grid[y + 1, x]:
                y += 1
            elif not grid[y + 1, x - 1]:
                y += 1
                x -= 1
            elif not grid[y + 1, x + 1]:
                y += 1
                x += 1
            else:
                # Rest
                grid[y, x] = 1
                if y == 0:
                    correct = False
                break
        except:
            correct = False
            break

    return correct
 

def day14_part1(data_file="data/day14.txt"):
    with open(data_file, "r") as f:
        rock_paths = [[(int(y.split(',')[0]), int(y.split(',')[1]))for y in x.replace('\n', '').split(' -> ')] for x in f.readlines()]
        max_x, min_x = 0, 500
        max_y = 0 

        # Search for min and max coordinates
        for rock in rock_paths:
            for line in rock:
                max_x = max(line[0], max_x)
                min_x = min(line[0], min_x)
                max_y = max(line[1], max_y)
        
        start_x = 500 - min_x
        grid = np.zeros([max_y + 1, max_x - min_x + 1])

        for rock in rock_paths:
            for i in range(len(rock) - 1):
                ini_x, ini_y = rock[i]
                end_x, end_y = rock[i + 1]
                range_x = range(ini_x, end_x + 1) if ini_x <= end_x else range(end_x, ini_x + 1)
                range_y = range(ini_y, end_y + 1) if ini_y <= end_y else range(end_y, ini_y + 1)

                for x in range_x:
                    for y in range_y:
                        grid[y, x - min_x] = 1

        sand_grains = 0
        rest = True
        while rest:
            sand_grains += 1
            rest = day14_sim_sand(start_x, grid)

        return sand_grains - 1


def day14_part2(data_file="data/day14.txt"):
    with open(data_file, "r") as f:
        rock_paths = [[(int(y.split(',')[0]), int(y.split(',')[1]))for y in x.replace('\n', '').split(' -> ')] for x in f.readlines()]
        max_x, min_x = 0, 500
        max_y = 0 

        # Search for min and max coordinates
        for rock in rock_paths:
            for line in rock:
                max_x = max(line[0], max_x)
                min_x = min(line[0], min_x)
                max_y = max(line[1], max_y)
        
        max_y += 2
        min_x = min_x - max_y
        max_x = max_x + max_y
        start_x = 500 - min_x
        grid = np.zeros([max_y + 1, max_x - min_x + 1])
        grid[-1, :] = 1

        for rock in rock_paths:
            for i in range(len(rock) - 1):
                ini_x, ini_y = rock[i]
                end_x, end_y = rock[i + 1]
                range_x = range(ini_x, end_x + 1) if ini_x <= end_x else range(end_x, ini_x + 1)
                range_y = range(ini_y, end_y + 1) if ini_y <= end_y else range(end_y, ini_y + 1)

                for x in range_x:
                    for y in range_y:
                        grid[y, x - min_x] = 1
        

        sand_grains = 0
        rest = True
        while rest:
            sand_grains += 1
            rest = day14_sim_sand(start_x, grid)

        return sand_grains


class Day15Interval:
    def __init__(self):
        self.intervals = []

    def sort(self):
        self.intervals = sorted(self.intervals)

    def check_overlap(self, a, b):
        # a contains b
        if a[0] <= b[0] and a[1] >= b[1]:
            return True

        # b contains a
        if b[0] <= a[0] and b[1] >= a[1]:
            return True

        # Partial overlap
        if (a[0] <= b[0] and a[1] >= b[0]) or (b[1] >= a[0] and b[1] <= a[1]):
            return True

        return False

    def add_interval(self, left, right):
        overlap = []
        for inter in self.intervals:
            if self.check_overlap(inter, (left, right)):
                overlap.append(inter)

        new_interval = [left, right]
        for o in overlap:
            # Treat overlaps
            self.intervals.remove(o)
            new_interval[0] = min(new_interval[0], o[0])
            new_interval[1] = max(new_interval[1], o[1])

        self.intervals.append(new_interval)
        self.sort()

    def remove_point(self, val):
        # Remove a point from the intervals
        found = None
        for inter in self.intervals:
            if inter[0] <= val <= inter[1]:
                found = inter
                break

        if not found:
            return
        
        self.intervals.remove(found)
        int_left = [inter[0], val - 1]
        int_right = [val + 1, inter[1]]

        if int_left[0] <= int_left[1]:
            self.intervals.append(int_left)
        if int_right[0] <= int_right[1]:
            self.intervals.append(int_right)

        self.intervals.sort()

    def _empty_sum(self):
        s = 0
        for i in self.intervals:
            s += (i[1] - i[0] + 1)

        return s

    def sum(self, left=None, right=None):
        if not left and not right:
            return self._empty_sum()

        s = 0
        for i in self.intervals:
            if (i[0] < left and i[1] < left) or (i[0] > right and i[1] > right):
                continue

            s += (min(i[1], right) - max(i[0], left) + 1)

        return s

    def find_empty_space(self):
        spaces = []
        for j in range(len(self.intervals) - 1):
            if self.intervals[j][1] == self.intervals[j + 1][0] - 2:
                spaces.append(self.intervals[j][1] + 1)

        return spaces

    def __str__(self):
        return str(self.intervals)


def day15_part1(data_file="data/day15.txt"):
    with open(data_file, "r") as f:
        lines = f.readlines() 
        desired_row = 2000000
        sensors = []
        beacons = []

        for l in lines:
            tokens = l.replace('\n', '').split(' ')
            sensor_x, sensor_y = int(tokens[2][2:-1]), int(tokens[3][2:-1])
            beacon_x, beacon_y = int(tokens[8][2:-1]), int(tokens[9][2:])
            sensors.append((sensor_x, sensor_y))
            beacons.append((beacon_x, beacon_y))
            
        interval = Day15Interval()
        for s, b in zip(sensors, beacons):
            dist = abs(s[0] - b[0]) + abs(s[1] - b[1])
            range_size = dist - abs(s[1] - desired_row)
            if range_size < 0:
                # Not affected
                continue
            
            left = s[0] - range_size
            right = s[0] + range_size

            # Add new invalid interval
            interval.add_interval(left, right)

            # Remove point if beacon is in the problematic row
            if b[1] == desired_row:
                interval.remove_point(b[0])

        return interval.sum()


def day15_part2(data_file="data/day15.txt"):
    with open(data_file, "r") as f:
        lines = f.readlines() 
        distress_min, distress_max = 0, 4000000
        sensors = []
        beacons = []

        for l in lines:
            tokens = l.replace('\n', '').split(' ')
            sensor_x, sensor_y = int(tokens[2][2:-1]), int(tokens[3][2:-1])
            beacon_x, beacon_y = int(tokens[8][2:-1]), int(tokens[9][2:])
            sensors.append((sensor_x, sensor_y))
            beacons.append((beacon_x, beacon_y))

        for desired_row in range(distress_min, distress_max):
            interval = Day15Interval()
            # Check row for just one spot empty
            for s, b in zip(sensors, beacons):
                dist = abs(s[0] - b[0]) + abs(s[1] - b[1])
                range_size = dist - abs(s[1] - desired_row)
                if range_size < 0:
                    # Not affected
                    continue
                
                left = s[0] - range_size
                right = s[0] + range_size

                # Add new invalid interval
                interval.add_interval(left, right)

            if interval.sum(distress_min, distress_max) == distress_max - distress_min:
                return interval.find_empty_space()[0] * 4000000 + desired_row

        return 0


if __name__ == "__main__":
   #print("Result Day 1 Part 1: ", day1_part1())
   #print("Result Day 1 Part 2: ", day1_part2())
   #print("Result Day 2 Part 1: ", day2_part1())
   #print("Result Day 2 Part 2: ", day2_part2())
   #print("Result Day 3 Part 1: ", day3_part1())
   #print("Result Day 3 Part 2: ", day3_part2())
   #print("Result Day 4 Part 1: ", day4_part1())
   #print("Result Day 4 Part 2: ", day4_part2())
   #print("Result Day 5 Part 1: ", day5_part1())
   #print("Result Day 5 Part 2: ", day5_part2())
   #print("Result Day 6 Part 1: ", day6_part1())
   #print("Result Day 6 Part 2: ", day6_part2())
   #print("Result Day 7 Part 1: ", day7_part1())
   #print("Result Day 7 Part 2: ", day7_part2())
   #print("Result Day 8 Part 1: ", day8_part1())
   #print("Result Day 8 Part 2: ", day8_part2())
   #print("Result Day 9 Part 1: ", day9_part1())
   #print("Result Day 9 Part 2: ", day9_part2())
   #print("Result Day 10 Part 1: ", day10_part1())
   #print("Result Day 10 Part 2: ", day10_part2())
   #print("Result Day 11 Part 1: ", day11_part1())
   #print("Result Day 11 Part 2: ", day11_part2())
   #print("Result Day 12 Part 1: ", day12_part1())
   #print("Result Day 12 Part 2: ", day12_part2())
   #print("Result Day 13 Part 1: ", day13_part1())
   #print("Result Day 13 Part 2: ", day13_part2())
   #print("Result Day 14 Part 1: ", day14_part1())
   #print("Result Day 14 Part 2: ", day14_part2())
    print("Result Day 15 Part 1: ", day15_part1())
    print("Result Day 15 Part 2: ", day15_part2())
