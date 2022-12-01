def read_input(filename="input.txt"):
    elves = [0]
    with open(filename, "r") as file:
        for line in file.readlines():
            if line.strip() == "":
                elves.append(0)
                continue
            elves[-1] += int(line.strip())
    return elves


def part_one():
    return max(read_input())


def part_two():
    elves = read_input()
    elves.sort()
    return sum(elves[-3:])


if __name__ == "__main__":
    print("Part 1:", part_one())
    print("Part 2:", part_two())