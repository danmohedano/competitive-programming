import numpy as np


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


if __name__ == "__main__":
    print("Result Day 1 Part 1: ", day1_part1())
    print("Result Day 1 Part 2: ", day1_part2())
    print("Result Day 2 Part 1: ", day2_part1())
    print("Result Day 2 Part 2: ", day2_part2())
    print("Result Day 3 Part 1: ", day3_part1())
    print("Result Day 3 Part 2: ", day3_part2())
    print("Result Day 4 Part 1: ", day4_part1())
    print("Result Day 4 Part 2: ", day4_part2())
    print("Result Day 5 Part 1: ", day5_part1())
    print("Result Day 5 Part 2: ", day5_part2())
    print("Result Day 6 Part 1: ", day6_part1())
    print("Result Day 6 Part 2: ", day6_part2())
    print("Result Day 7 Part 1: ", day7_part1())
    print("Result Day 7 Part 2: ", day7_part2())
    print("Result Day 8 Part 1: ", day8_part1())
    print("Result Day 8 Part 2: ", day8_part2())
    print("Result Day 9 Part 1: ", day9_part1())
    print("Result Day 9 Part 2: ", day9_part2())
