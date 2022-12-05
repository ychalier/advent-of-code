import re

FILENAME = "input.txt"


def parse_input():
    with open(FILENAME) as file:
        drawing = []
        is_drawing = True
        plan = []
        for line in file.read().splitlines():
            match = re.match(r"^( +?\d+ +?)+$", line)
            if match is not None:
                is_drawing = False
                continue
            elif is_drawing:
                level = tuple(line[1::4])
                drawing.append(level)
            elif line != "":
                match = re.match(r"move (\d+) from (\d+) to (\d+)", line)
                plan.append((int(match.group(1)), int(match.group(2)) - 1, int(match.group(3)) - 1))
        n = len(drawing[0])
        stacks = [[] for _ in range(n)]
        for row in reversed(drawing):
            for i in range(n):
                if row[i] == " ":
                    continue
                stacks[i].append(row[i])
        return stacks, plan


def part_one():
    stacks, plan = parse_input()
    for qty, i, j in plan:
        for _ in range(qty):
            stacks[j].append(stacks[i].pop())
    return "".join([s[-1] for s in stacks])


def part_two():
    stacks, plan = parse_input()
    for qty, i, j in plan:
        stacks[j] += stacks[i][-qty:]
        del stacks[i][-qty:]
    return "".join([s[-1] for s in stacks])


if __name__ == "__main__":
    print("Part 1:", part_one())
    print("Part 2:", part_two())