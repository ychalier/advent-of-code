FILENAME = "input.txt"


def read_grid():
    grid = []
    with open(FILENAME) as file:
        for line in file.read().splitlines():
            grid.append(list(map(int, line)))
    return grid


def part_one():
    grid = read_grid()
    n = len(grid)
    visibility = [[{} for _ in range(n)] for _ in range(n)]

    # Visibility from left
    for i in range(n):
        highest_tree = None
        for j in range(n):
            if highest_tree is None or grid[i][j] > highest_tree:
                visibility[i][j]["left"] = True
                highest_tree = grid[i][j]
            else:
                visibility[i][j]["left"] = False
    
    # Visibility from right
    for i in range(n):
        highest_tree = None
        for j in reversed(range(n)):
            if highest_tree is None or grid[i][j] > highest_tree:
                visibility[i][j]["right"] = True
                highest_tree = grid[i][j]
            else:
                visibility[i][j]["right"] = False
    
    # Visibility from top
    for j in range(n):
        highest_tree = None
        for i in range(n):
            if highest_tree is None or grid[i][j] > highest_tree:
                visibility[i][j]["top"] = True
                highest_tree = grid[i][j]
            else:
                visibility[i][j]["top"] = False
    
    # Visibility from bottom
    for j in range(n):
        highest_tree = None
        for i in reversed(range(n)):
            if highest_tree is None or grid[i][j] > highest_tree:
                visibility[i][j]["bottom"] = True
                highest_tree = grid[i][j]
            else:
                visibility[i][j]["bottom"] = False
    
    total = 0
    for i in range(n):
        for j in range(n):
            if True in visibility[i][j].values():
                total += 1
    return total


def part_two():
    grid = read_grid()
    n = len(grid)
    best_scenic_score = 0
    for i in range(n):
        for j in range(n):
            scenic_score = 1
            for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                pos = [i, j]
                viewing_distance = 0
                while True:
                    pos[0] += direction[0]
                    pos[1] += direction[1]
                    if pos[0] < 0 or pos[0] >= n or pos[1] < 0 or pos[1] >= n:
                        break # Reach an edge
                    if grid[i][j] <= grid[pos[0]][pos[1]]:
                        viewing_distance += 1
                        break # View gets blocked
                    viewing_distance += 1
                scenic_score *= viewing_distance
            best_scenic_score = max(best_scenic_score, scenic_score)
    return best_scenic_score


if __name__ == "__main__":
    print("Part 1:", part_one())
    print("Part 2:", part_two())