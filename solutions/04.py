with open("inputs/04.txt") as f:
    _lines = f.readlines()
    _pairs = []
    content = []
    for line in _lines:
        _pairs.append(line.strip().split(","))
    for pair in _pairs:
        content.append(list(map(lambda y: (int(y[0]), int(y[1]) +1),list(map(lambda x: x.split("-"), pair)))))
        

def part_1(c) -> int:
    counter: int = 0
    for pair in c:
        range_a = list(range(pair[0][0], pair[0][1])) if pair[0][0] != pair[0][1] else [pair[0][0]]
        range_b = list(range(pair[1][0], pair[1][1])) if pair[1][0] != pair[1][1] else [pair[1][0]]
        check_b_in_a = all(n in range_a for n in range_b)
        check_a_in_b = all(n in range_b for n in range_a)
        if check_a_in_b or check_b_in_a:
            counter += 1
    return counter

def part_2(c) -> int:
    counter: int = 0
    for pair in c:
        range_a = list(range(pair[0][0], pair[0][1])) if pair[0][0] != pair[0][1] else [pair[0][0]]
        range_b = list(range(pair[1][0], pair[1][1])) if pair[1][0] != pair[1][1] else [pair[1][0]]
        xs = set(range_a)
        if xs.intersection(range_b):
            counter += 1
    return counter

if __name__ == "__main__":
    print("Part 1:", part_1(content))
    print("Part 2:", part_2(content))