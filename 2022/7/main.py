import re


FILENAME = "input.txt"


def get_size(fs, path):
    obj = fs.get(path)
    if obj is None:
        return 0
    if isinstance(obj, int):
        return obj
    return sum([get_size(fs, child) for child in obj])


def parse_fs():
    fs = {}
    cwd = "/"
    with open(FILENAME) as file:
        for line in file.read().splitlines():
            match = re.match(r"^\$ cd (.+)$", line)
            if match is not None:
                path = match.group(1)
                if path == "/":
                    cwd = "/"
                elif path == "..":
                    cwd = "/".join(cwd.split("/")[:-2]) + "/"
                else:
                    cwd += path + "/"
                fs.setdefault(cwd, set())
                continue
            match = re.match(r"^\$ ls$", line)
            if match is not None:
                continue
            match = re.match(r"^dir (.+)$", line)
            if match is not None:
                path = cwd + match.group(1) + "/"
                fs[cwd].add(path)
                continue
            match = re.match(r"^(\d+) (.+)$", line)
            if match is not None:
                path = cwd + match.group(2)
                fs[cwd].add(path)
                fs[path] = int(match.group(1))
                continue
            print("Could not match '%s'" % line)
    return fs



def part_one():
    fs = parse_fs()
    total = 0
    for path, obj in fs.items():
        if isinstance(obj, int):
            continue
        size = get_size(fs, path)
        if size <= 100000:
            total += size
    return total


def part_two():
    fs = parse_fs()
    du = get_size(fs, "/")
    to_free = 30000000 - 70000000 + du
    candidates = []
    for path, obj in fs.items():
        if isinstance(obj, int):
            continue
        size = get_size(fs, path)
        if size >= to_free:
            candidates.append(size)
    return min(candidates)


if __name__ == "__main__":
    print("Part 1:", part_one())
    print("Part 2:", part_two())