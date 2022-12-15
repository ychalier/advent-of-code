import re

FILENAME = "input.txt"


def part_one():
    y = 2000000
    beacons_at_y = set()
    spans = []
    with open(FILENAME) as file:
        for line in file.read().splitlines():
            match = re.match(r"Sensor at x=(\-?\d+), y=(\-?\d+): closest beacon is at x=(\-?\d+), y=(\-?\d+)", line)
            sensor = int(match.group(1)), int(match.group(2))
            beacon = int(match.group(3)), int(match.group(4))
            if beacon[1] == y:
                beacons_at_y.add(beacon)
            radius = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
            if sensor[1] - radius <= y and sensor[1] + radius >= y:
                h = radius - abs(sensor[1] - y)
                spans.append([sensor[0] - h, sensor[0] + h])
    spans.sort()
    i = 1
    while i < len(spans):
        if spans[i][0] >= spans[i - 1][0] and spans[i][0] <= spans[i - 1][1]:
            spans[i - 1][1] = max(spans[i - 1][1], spans[i][1])
            spans.pop(i)
        else:
            i += 1
    return sum([end - start + 1 for start, end in spans]) - len(beacons_at_y)


def part_two():
    sensors = []
    with open(FILENAME) as file:
        for line in file.read().splitlines():
            match = re.match(r"Sensor at x=(\-?\d+), y=(\-?\d+): closest beacon is at x=(\-?\d+), y=(\-?\d+)", line)
            sensor = int(match.group(1)), int(match.group(2))
            beacon = int(match.group(3)), int(match.group(4))
            radius = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
            sensors.append((sensor, radius))
    for y in range(0, 4000000):
        spans = []
        for sensor, radius in sensors:
            if sensor[1] - radius <= y and sensor[1] + radius >= y:
                h = radius - abs(sensor[1] - y)
                spans.append([max(0, sensor[0] - h), min(4000000, sensor[0] + h)])
        spans.sort()
        i = 1
        while i < len(spans):
            if spans[i][0] >= spans[i - 1][0] and spans[i][0] <= spans[i - 1][1]:
                spans[i - 1][1] = max(spans[i - 1][1], spans[i][1])
                spans.pop(i)
            else:
                i += 1
        if len(spans) == 2:
            x = spans[0][1] + 1
            frequency = x * 4000000 + y
            return frequency


if __name__ == "__main__":
    print("Part 1:", part_one())
    print("Part 2:", part_two())