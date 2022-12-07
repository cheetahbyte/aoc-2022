from collections import Counter
with open("inputs/07.txt") as f:
    content = f.read()

def data(c):
    dirs = Counter()
    cwd = []
    command = ''
    for line in c.splitlines():
        if line.startswith('dir'):
            continue
        if line.startswith('$'):
            _, command, *args = line.split()
            if command == 'cd':
                arg = args.pop()
                if arg == '..':
                    cwd.pop()
                else:
                    cwd.append(arg)
        elif command == 'ls':
            size = int(line.split()[0])
            for i in range(len(cwd)):
                dirs[tuple(cwd[:i + 1])] += size
    return dirs


def part_1(c):
    sizes = data(c).values()
    return sum(filter(lambda x: x <= 100_000, sizes))

def part_2(c):
    dirs = data(c)
    MAX = 70_000_000
    REQUIRED = 30_000_000
    used = dirs[("/",)]
    free = MAX - used
    left = REQUIRED - free
    for size in sorted(dirs.values()):
        if size >= left:
            return size

if __name__ == "__main__":
    print("Part 1:", part_1(content))
    print("Part 2:", part_2(content))
