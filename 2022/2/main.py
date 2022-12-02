"""If l is the move chosen by the elf,
- 'l' is the draw move
- '(l + 1) % 3' is the winning move
- '(l + 2) % 3' is the losing move
"""

ROCK = 0
PAPER = 1
SCISSORS = 2

DECODE_L = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS
}

DECODE_R = {
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS
}

SCORE_LOOSE = 0
SCORE_DRAW = 3
SCORE_WIN = 6


def compute_score(game):
    score = 0
    for l, r in game:
        score += r + 1
        if l == r:
            score += SCORE_DRAW
        elif r == (l + 1) % 3:
            score += SCORE_WIN
        else:
            score += SCORE_LOOSE
    return score


def part_one():
    game = []
    with open("input.txt", "r") as file:
        for line in file.readlines():
            if line.strip() == "":
                continue
            l, r = line.strip().split(" ")
            game.append((DECODE_L[l], DECODE_R[r]))
    return compute_score(game)


def part_two():
    game = []
    with open("input.txt", "r") as file:
        for line in file.readlines():
            if line.strip() == "":
                continue
            l, r = line.strip().split(" ")
            l = DECODE_L[l]
            if r == "X":  # need to loose
                r = (l + 2) % 3
            elif r == "Y":  # need to draw
                r = l
            elif r == "Z":  # need to win
                r = (l + 1) % 3
            game.append((l, r))
    return compute_score(game)


if __name__ == "__main__":
    print("Part 1:", part_one())
    print("Part 2:", part_two())