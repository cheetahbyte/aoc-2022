import string
with open("inputs/03.txt") as f:
    c = f.read().splitlines()

def part_1(c):
    score:int = 0
    for bag in c:
        first, second = bag[:int(len(bag) / 2)], bag[int(len(bag) / 2):]
        common = list(set(first)&set(second))[0]
        score += list(string.ascii_letters).index(common) +1
    return score


def part_2(c):
    score: int = 0
    grouped = list(zip(*[iter(c)] *3))
    for group in grouped:
        common = list(set(group[0])&set(group[1])&set(group[2]))[0]
        score += list(string.ascii_letters).index(common) +1
    return score

if __name__ == "__main__":
    print("Part 1:", part_1(c))
    print("Part 2:", part_2(c))
