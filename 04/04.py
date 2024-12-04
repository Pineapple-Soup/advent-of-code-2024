def parse_input(filename):
    puzzle = []
    with open(filename, "r") as file:
        for line in file:
            puzzle.append(line.strip())
    return puzzle

word = "XMAS"
puzzle = parse_input("input.txt")

directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

def search_index(row, col, direction):
    for i in range(len(word)):
        new_row = row + i * direction[0]
        new_col = col + i * direction[1]
        if new_row < 0 or new_row >= len(puzzle) or new_col < 0 or new_col >= len(puzzle[0]):
            return False
        if puzzle[new_row][new_col] != word[i]:
            return False
    return True

def part1(puzzle):
    ans = 0
    for r in range(len(puzzle)):
        for c in range(len(puzzle[0])):
            for direction in directions:
                if search_index(r, c, direction):
                    ans += 1
    return ans

print("Part 1:", part1(puzzle))