def get_content():
    with open("inputs/02.txt") as f:
        return [ tuple(e.split(" ")) for e in f.read().splitlines()]



def get_points(attack, conter) -> int:
    match attack:
        case "A":
            match conter:
                case "X": 
                    return 3
                case "Y": 
                    return 6
                case "Z": 
                    return 0
        case "B":
            match conter:
                case "X": 
                    return 0
                case "Y": 
                    return 3
                case "Z": 
                    return 6
        case "C":
            match conter:
                case "X": 
                    return 6
                case "Y": 
                    return 0
                case "Z": 
                    return 3

def part_1():
    s: int = 0
    content: list = get_content()
    vals: dict = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    for attack, conter in content:
        s += vals[conter] + get_points(attack, conter)
    return s


def part_2():
    content = get_content()
    sc = {
        'A': {
            'X': 3,
            'Y': 4,
            'Z': 8
        },
        'B': {
            'X': 1,
            'Y': 5,
            'Z': 9
        },
        'C': {
            'X': 2,
            'Y': 6,
            'Z': 7
        }
    }
    return sum([sc[a][b] for a,b in content])

if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())