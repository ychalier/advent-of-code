def value(char):
    o = ord(char)
    if o >= 97:
        return o - 96
    return o - 38


def part_one():
    total = 0
    with open("input.txt") as file:
        for line in file.readlines():
            line = line.strip()
            n = len(line)
            c = list(set(line[:n // 2]).intersection(line[n // 2:]))[0]
            total += value(c)
    return total


def part_two():
    total = 0
    with open("input.txt") as file:
        lines = file.readlines()
        for i in range(0, len(lines), 3):
            c = list(set(lines[i].strip()).intersection(lines[i+1]).intersection(lines[i+2]))[0]
            total += value(c)
    return total


if __name__ == "__main__":
    print("Part 1:", part_one())
    print("Part 2:", part_two())