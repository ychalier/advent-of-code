import re


FILENAME = "input.txt"
DARK = "."
LIT = "#"


class CRT:

    def __init__(self):
        self.X = 1
        self.t = 0
        self.strength = 0
        self.width = 40
        self.height = 6
        self.screen = [[DARK for _ in range(self.width)] for _ in range(self.height)]
        self.cursor = 0
    
    def __str__(self):
        return "\n".join("".join(row) for row in self.screen)

    def cycle(self):
        self.t += 1
        if (self.t + 20) % 40 == 0:
            self.strength += self.t * self.X
        i = self.cursor // self.width
        j = self.cursor % self.width
        if j == self.X or j == self.X - 1 or j == self.X + 1:
            self.screen[i][j] = LIT
        else:
            self.screen[i][j] = DARK
        self.cursor = (self.cursor + 1) % (self.width * self.height)
    
    def noop(self):
        self.cycle()
    
    def addx(self, v):
        self.cycle()
        self.cycle()
        self.X += v


def aux():
    crt = CRT()
    with open(FILENAME) as file:
        for line in file.read().splitlines():
            match = re.match(r"(addx|noop) ?(\-?\d+)?", line)
            if match.group(1) == "noop":
                crt.noop()
            elif match.group(1) == "addx":
                crt.addx(int(match.group(2)))
    return crt


def part_one():
    return aux().strength


def part_two():
    return str(aux())


if __name__ == "__main__":
    print("Part 1:", part_one())
    print("Part 2:\n" + part_two())