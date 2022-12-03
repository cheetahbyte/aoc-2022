
def content():
    with open("inputs/01.txt") as f:
        return sorted([*map(sum, (map(int, x.splitlines()) for x in f.read().split('\n\n')))], reverse=True)


def part_1() -> None:
    return max(content())

def part_2() -> None:
    return sum(content()[:3])

if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())