def parse_input(filename: str) -> list[list, list]:
    list1 = []
    list2 = []
    with open(filename, 'r') as f:
        data = f.readlines()
        for line in data:
            x, y = line.split()
            list1.append(int(x))
            list2.append(int(y))
    return list1, list2

l1, l2 = parse_input('input.txt')

def part1(l1: list, l2: list) -> int:
    sorted_l1 = sorted(l1)
    sorted_l2 = sorted(l2)
    sum = 0;
    for i in range(len(sorted_l1)):
        sum += abs(sorted_l1[i] - sorted_l2[i])
    return sum

print(part1(l1, l2))