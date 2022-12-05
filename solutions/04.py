with open("inputs/04-maik.txt") as f:
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
        a,b = pair
        if a[0] <= b[0] and a[1] >= b[1]:
            counter += 1
        elif b[0] <= a[0] and b[1] >= a[1]:
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