FILENAME = "input.txt"


def find_marker(n):
    with open(FILENAME) as file:
        stream = file.read().strip()
        for i in range(n, len(stream) + 1):
            if len(set(stream[i-n:i])) == n:
                return i


def part_one():
    return find_marker(4)


def part_two():
    return find_marker(14)


if __name__ == "__main__":
    print("Part 1:", part_one())
    print("Part 2:", part_two())