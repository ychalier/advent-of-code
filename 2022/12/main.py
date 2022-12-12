FILENAME = "input.txt"


def parse_grid():
    grid = []
    start = None
    end = None
    with open(FILENAME) as file:
        for i, line in enumerate(file.read().splitlines()):
            grid.append([])
            for j, char in enumerate(line):
                if char == "S":
                    start = i, j
                    grid[i].append(0)
                elif char == "E":
                    end = i, j
                    grid[i].append(25)
                else:
                    grid[i].append(ord(char) - 97)
    return grid, start, end


def dijkstra(grid, start, reversed=False):
    width = len(grid[0])
    height = len(grid)
    distance = { (i, j): width * height * 2 for i in range(height) for j in range(width) }
    distance[start] = 0
    seen = set()
    while len(seen) < width * height:
        node = min(set(distance.keys()).difference(seen), key=lambda x: distance[x])
        seen.add(node)
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if node[0] + d[0] < 0 or node[0] + d[0] >= height or node[1] + d[1] < 0 or node[1] + d[1] >= width:
                continue
            neighbor = node[0] + d[0], node[1] + d[1]
            if reversed and grid[node[0]][node[1]] > grid[neighbor[0]][neighbor[1]] + 1:
                continue
            if not reversed and grid[node[0]][node[1]] + 1 < grid[neighbor[0]][neighbor[1]]:
                continue
            distance[neighbor] = min(distance[neighbor], distance[node] + 1)
    return distance


def part_one():
    grid, start, end = parse_grid()
    return dijkstra(grid, start)[end]


def part_two():
    grid, _, end = parse_grid()
    width = len(grid[0])
    height = len(grid)
    distance = dijkstra(grid, end, True)
    start = min(
        [(i, j) for i in range(height) for j in range(width) if grid[i][j] == 0],
        key=lambda node: distance[node])
    return distance[start]


if __name__ == "__main__":
    print("Part 1:", part_one())
    print("Part 2:", part_two())