with open("inputs/06.txt") as f:
    content = f.read().strip()

def part_1(c: str) -> int:
    parts = list(c)
    start, end = 0,4
    current = None
    while True and end < len(parts):
        current = parts[start:end]
        if len(current) != len(set(current)):
            start += 1;end += 1
        else:
            break
    return end
    
def part_2(c: str) -> int:
    parts = list(c)
    start, end = 0,14
    current = None
    while True and end < len(parts):
        current = parts[start:end]
        if len(current) != len(set(current)):
            start += 1;end += 1
        else:
            break
    return end
    
            
    

if __name__ == "__main__":
    print("Part 1:", part_1(content))
    print("Part 2:", part_2(content))