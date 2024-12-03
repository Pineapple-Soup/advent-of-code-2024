import re

def parse_input(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    return data

str = "".join(parse_input('input.txt'))

pattern = r"mul\(\d{1,3},\d{1,3}\)"
matches = re.findall(pattern, str)

def part1(matches):
    ans = 0
    for match in matches:
        num1, num2 = map(int, re.findall(r"\d{1,3}", match))
        ans += num1*num2
    return ans

adv_pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
matches2 = re.findall(adv_pattern, str)

def part2(matches):
    ans = 0
    active = True
    for match in matches:
        #print(match)
        if match == "do()":
            active = True
        elif match == "don't()":
            active = False
        else:
            if active:
                num1, num2 = map(int, re.findall(r"\d{1,3}", match))
                ans += num1*num2
    return ans

print("Part 1:", part1(matches))
print("Part 2:", part2(matches2))