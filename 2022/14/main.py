FILENAME = "input.txt"


def parse_rocks():
    rocks = set()
    with open(FILENAME) as file:
        for line in file.read().splitlines():
            points = list(map(lambda s: tuple(map(int, s.split(","))), line.split(" -> ")))
            for start, end in zip(points[:-1], points[1:]):
                for i in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
                    for j in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                        rocks.add((i, j))
    return rocks


def part_one():
    rocks = parse_rocks()
    bottom = max([r[1] for r in rocks])
    sand_at_rest = set()
    total = 0
    while True:
        sand = (500, 0)
        while True:
            falls = False
            for di in [0, -1, 1]:
                target = sand[0] + di, sand[1] + 1
                if target in rocks or target in sand_at_rest:
                    continue
                falls = True
                sand = target
                break
            if not falls:
                sand_at_rest.add(sand)
                break
            if sand[1] > bottom:
                break
        if sand[1] > bottom:
            return total
        total += 1


def part_two():
    rocks = parse_rocks()
    bottom = max([r[1] for r in rocks]) + 2
    sand_at_rest = set()
    total = 0
    while True:
        sand = (500, 0)
        while True:
            falls = False
            for di in [0, -1, 1]:
                target = sand[0] + di, sand[1] + 1
                if target in rocks or target in sand_at_rest or target[1] == bottom:
                    continue
                falls = True
                sand = target
                break
            if not falls:
                if sand == (500, 0):
                    return total + 1
                sand_at_rest.add(sand)
                break
            if sand[1] > bottom:
                break
        if sand[1] > bottom:
            return total
        total += 1


if __name__ == "__main__":
    print("Part 1:", part_one())
    print("Part 2:", part_two())