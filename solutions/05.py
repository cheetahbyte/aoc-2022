import re

with open("inputs/05.txt") as f:
    bay = {}
    _raw = list(f.read().split("\n\n"))


def data() -> tuple:
    cts = _raw[0].split("\n")
    nums = cts[len(cts) - 1]
    l = int(nums[len(nums) - 2])
    for p in range(1, l + 1):
        pi = nums.index(str(p))
        bay[p] = []
        for i in range(len(cts) -1):
            crate = cts[i][pi]
            if crate != " ":
                bay[p].append(crate)
        bay[p].reverse()

    sts = list(map(lambda l: re.findall("\d+", l),_raw[1].split("\n")))
    return bay, sts

def part_1() -> str:
    string: str = ""
    bay, inst = data()
    for i in inst:
        count, o_raw, d_raw = i
        origin, destination = bay.get(int(o_raw)), bay.get(int(d_raw))
        transfer = origin[-int(count):]
        transfer.reverse()
        bay[int(o_raw)] = origin[:-int(count)]
        bay[int(d_raw)] += transfer
    for b in bay.values():
        string += b[-1]
    return string

def part_2() -> str:
    string: str = ""
    bay, inst = data()
    for i in inst:
        count, o_raw, d_raw = i
        origin, destination = bay.get(int(o_raw)), bay.get(int(d_raw))
        transfer = origin[-int(count):]
        bay[int(o_raw)] = origin[:-int(count)]
        bay[int(d_raw)] += transfer
    for b in bay.values():
        string += b[-1]
    return string

if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())
