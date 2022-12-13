import json
import functools


FILENAME = "input.txt"


def compare(left, right):
    for i in range(min(len(left), len(right))):
        x = left[i]
        y = right[i]
        if isinstance(x, int) and isinstance(y, int):
            if x < y:
                return True
            if x > y:
                return False
            continue
        if isinstance(x, int) and isinstance(y, list):
            sub_comparison = compare([x], y)
        elif isinstance(x, list) and isinstance(y, int):
            sub_comparison = compare(x, [y])
        else:
            sub_comparison = compare(x, y)
        if sub_comparison is None:
            continue
        return sub_comparison
    if len(left) < len(right):
        return True
    if len(left) > len(right):
        return False
    return None


def part_one():
    pairs = []
    with open(FILENAME) as file:
        current_pair = []
        for line in file.read().splitlines():
            if line == "":
                continue
            current_pair.append(json.loads(line))
            if len(current_pair) == 2:
                pairs.append(current_pair[:])
                current_pair = []
    total = 0
    for i, pair in enumerate(pairs):
        if compare(*pair):
            total += i + 1
    return total


def part_two():
    packets = []
    with open(FILENAME) as file:
        for line in file.read().splitlines():
            if line == "":
                continue
            packets.append(json.loads(line))
    packets += [[[2]], [[6]]]
    packets.sort(key=functools.cmp_to_key(lambda x, y: -1 if compare(x, y) else 1))
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


if __name__ == "__main__":
    print("Part 1:", part_one())
    print("Part 2:", part_two())
