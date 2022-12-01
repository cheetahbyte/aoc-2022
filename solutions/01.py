
def content(file: str) -> str:
    with open(file) as f:
        return f.read()

c = content("inputs/01.txt").splitlines()
count: int = 0
content = []
l = []
while count < len(c):
    if c[count] == "":
        content.append(l)
        l = []
    else:
        l.append(int(c[count]))
    count += 1

def part_1() -> None:
    return max([sum(elem) for elem in content])

def part_2() -> None:
    return sum(sorted([sum(elem) for elem in content], reverse=True)[:3])

if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())