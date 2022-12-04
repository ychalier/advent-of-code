FILENAME = "input.txt"


parse_pair = lambda pair: tuple(map(int, pair.split("-")))
parse = lambda line: tuple(map(parse_pair, line.split(",")))


def part_one():
    contains = 0
    with open(FILENAME) as file:
        for line in file.read().splitlines():
            l, r = parse(line)
            if (l[0] >= r[0] and l[1] <= r[1]) or (r[0] >= l[0] and r[1] <= l[1]):
                contains += 1
    return contains


def part_two():
    overlap = 0
    with open(FILENAME) as file:
        for line in file.read().splitlines():
            l, r = parse(line)
            inter = max(l[0], r[0]), min(l[1], r[1])
            if inter[0] <= inter[1]:
                overlap += 1
    return overlap


if __name__ == "__main__":
    print("Part 1:", part_one())
    print("Part 2:", part_two())