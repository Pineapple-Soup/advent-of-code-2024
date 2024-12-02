def parse_input(filename: str) -> list[list]:
    levels = []
    with open(filename, 'r') as f:
        data = f.readlines()
        for line in data:
            levels.append(list(map(int, line.split())))
    return levels

levels = parse_input('input.txt')

def part1(levels: list) -> int:
    ans = 0
    for level in levels:
        asc = True if level[-1] > level[0] else False
        for i in range(len(level)-1):
            diff = level[i+1] - level[i]
            if asc:
                if diff != 1 and diff != 2 and diff != 3:
                    break
            else:
                if diff != -1 and diff != -2 and diff != -3:
                    break
            if i == len(level)-2:
                ans += 1
    return ans

def is_safe(l: list) -> bool:
    if (l != sorted(l) and l != sorted(l, reverse=True)):
        return False
    for i in range(len(l)-1):
        diff = abs(l[i+1] - l[i])
        if diff != 1 and diff != 2 and diff != 3:
            return False
    return True

def part2(levels: list) -> int:
    ans = 0
    for level in levels:
        safe = False
        for j in range(len(level)):
            alt_level = level[:j] + level[j+1:]
            if is_safe(alt_level):
                safe = True
                break
        if safe:
            ans += 1
    return ans

print("Part 1:", part1(levels))
print("Part 2:", part2(levels))