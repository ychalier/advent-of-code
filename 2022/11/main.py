FILENAME = "input.txt"   


def part_one():
    monkeys = []
    with open(FILENAME) as file:
        monkey = {}
        monkeys.append(monkey)
        for line in file.readlines():
            if line.strip().startswith("Starting items"):
                monkey["items"] = list(map(int, line.strip()[16:].split(", ")))
            elif line.strip().startswith("Operation"):
                monkey["op"] = line.strip()[17:]
            elif line.strip().startswith("Test"):
                monkey["test"] = int(line.strip()[19:])
            elif line.strip().startswith("If true"):
                monkey["true"] = int(line.strip()[25:])
            elif line.strip().startswith("If false"):
                monkey["false"] = int(line.strip()[26:])
            elif line.strip() == "":
                monkey = {}
                monkeys.append(monkey)
    for _ in range(20):
        for i, monkey in enumerate(monkeys):
            monkey.setdefault("inspected", 0)
            while len(monkey["items"]) > 0:
                item = monkey["items"].pop(0)
                monkey["inspected"] += 1
                worry_level = int(eval(monkey["op"], {"old": item}) / 3)
                if worry_level % monkey["test"] == 0:
                    monkeys[monkey["true"]]["items"].append(worry_level)
                else:
                    monkeys[monkey["false"]]["items"].append(worry_level)
    total = 1
    for monkey in sorted(monkeys, key=lambda monkey: monkey["inspected"])[-2:]:
        total *= monkey["inspected"]
    return total


def part_two():
    monkeys = []
    dividers = []
    with open(FILENAME) as file:
        monkey = {}
        monkeys.append(monkey)
        for line in file.readlines():
            lstrip = line.strip()
            if lstrip.startswith("Starting items"):
                monkey["starting_items"] = list(map(int, lstrip[16:].split(", ")))
            elif lstrip.startswith("Operation"):
                monkey["op"] = lstrip[17:]
            elif lstrip.startswith("Test"):
                dividers.append(int(lstrip[19:]))
                monkey["test"] = int(lstrip[19:])
            elif lstrip.startswith("If true"):
                monkey["true"] = int(lstrip[25:])
            elif lstrip.startswith("If false"):
                monkey["false"] = int(lstrip[26:])
            elif lstrip == "":
                monkey = {}
                monkeys.append(monkey)
    for monkey in monkeys:
        monkey["items"] = [
            [item % divider for divider in dividers]
            for item in monkey["starting_items"]
        ]
    for _ in range(10000):
        for i, monkey in enumerate(monkeys):
            monkey.setdefault("inspected", 0)
            while len(monkey["items"]) > 0:
                item = monkey["items"].pop(0)[:]
                monkey["inspected"] += 1
                for j, divider in enumerate(dividers):
                    item[j] = eval(monkey["op"], {"old": item[j]}) % divider
                if item[i] == 0:
                    monkeys[monkey["true"]]["items"].append(item)
                else:
                    monkeys[monkey["false"]]["items"].append(item)
    total = 1
    for monkey in sorted(monkeys, key=lambda monkey: monkey["inspected"])[-2:]:
        total *= monkey["inspected"]
    return total


if __name__ == "__main__":
    print("Part 1:", part_one())
    print("Part 2:", part_two())