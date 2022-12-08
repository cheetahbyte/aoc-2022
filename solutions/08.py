with open("inputs/08.txt") as f:
    content = f.readlines()

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def data(ct):
    c = []
    for line in ct:
        c.append(list(map(int, line.strip())))
    return c



def part_1(c):
    vis = 0
    ox = len(c)
    oy = len(c[0])

    def isVisible(i, j):
        for di, dj in dirs:
            ni, nj = i+di, j+dj

            while 0 <= ni < ox and 0 <= nj < oy and c[ni][nj] < c[i][j]:
                ni += di
                nj += dj

            if not (0 <= ni < ox and 0 <= nj < oy):
                return True

        return False

    for i in range(ox):
        for j in range(oy):
            if isVisible(i, j):
                vis += 1

    return vis

def part_2(c):
    r = 0
    ox = len(c)
    oy = len(c[0])

    def sc_score(i, j) -> int:
        s = 1
        for di, dj in dirs:
            curr = 0
            ni, nj = i+di, j+dj

            while 0 <= ni < ox and 0 <= nj < oy:
                curr += 1
                if c[ni][nj] >= c[i][j]:
                    break

                ni += di
                nj += dj

            s *= curr

        return s

    for i in range(ox):
        for j in range(oy):
            r = max(r, sc_score(i, j))

    return r



if __name__ == "__main__":
    d = data(content)
    print("Part 1:", part_1(d))
    print("Part 2:", part_2(d))
