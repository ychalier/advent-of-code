FILENAME = "input.txt"


DIRECTIONS = {
    "U": [-1, 0],
    "D": [1, 0],
    "L": [0, -1],
    "R": [0, 1],
}


def moveto(source, destination):
    # Check if source and destination are touching
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if source[0] + i == destination[0] and source[1] + j == destination[1]:
                return source
    
    # Check if we just can go straigth to it
    for direction in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
        if source[0] + direction[0] == destination[0] and source[1] + direction[1] == destination[1]:
            return [source[0] + direction[0] // 2, source[1] + direction[1] // 2]
    
    # Otherwise get closer by moving diagonnally
    min_direction = None
    min_distance = None
    for direction in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        distance = abs(destination[0] - (source[0] + direction[0])) + abs(destination[1] - (source[1] + direction[1]))
        if min_distance is None or distance < min_distance:
            min_direction = direction
            min_distance = distance
    return [source[0] + min_direction[0], source[1] + min_direction[1]]


def simulate(rope_length):
    rope = [[0, 0] for _ in range(rope_length)]
    seen = set()
    with open(FILENAME) as file:
        for line in file.read().splitlines():
            direction_letter, length = line.split()
            direction = DIRECTIONS[direction_letter]
            for _ in range(int(length)):
                rope[0][0] += direction[0]
                rope[0][1] += direction[1]
                for t in range(1, rope_length):
                    rope[t] = moveto(rope[t], rope[t - 1])
                seen.add(tuple(rope[-1]))
    return len(seen)


def part_one():
    return simulate(2)


def part_two():
    return simulate(10)


if __name__ == "__main__":
    print("Part 1:", part_one())
    print("Part 2:", part_two())