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

def check_cross(rs, cs, re, ce, puzzle):
    # Case 1:
    # M M
    #  A
    # S S   
    if puzzle[rs][cs] == "M" and puzzle[rs][ce] == "M" and puzzle[rs+1][cs+1] == "A" and puzzle[re][cs] == "S" and puzzle[re][ce] == "S":
        return True
    # Case 2:
    # M S
    #  A
    # M S
    if puzzle[rs][cs] == "M" and puzzle[rs][ce] == "S" and puzzle[rs+1][cs+1] == "A" and puzzle[re][cs] == "M" and puzzle[re][ce] == "S":
        return True
    # Case 3:
    # S M
    #  A
    # S M
    if puzzle[rs][cs] == "S" and puzzle[rs][ce] == "M" and puzzle[rs+1][cs+1] == "A" and puzzle[re][cs] == "S" and puzzle[re][ce] == "M":
        return True
    # Case 4:
    # S S
    #  A
    # M M
    if puzzle[rs][cs] == "S" and puzzle[rs][ce] == "S" and puzzle[rs+1][cs+1] == "A" and puzzle[re][cs] == "M" and puzzle[re][ce] == "M":
        return True
    return False

def search_cross(row, col, puzzle):
    row_end = row + 2
    col_end = col + 2
    if row_end >= len(puzzle) or col_end >= len(puzzle[0]):
        return False
    return check_cross(row, col, row_end, col_end, puzzle)
    
def part2(puzzle):
    ans = 0
    for r in range(len(puzzle)):
        for c in range(len(puzzle[0])):
            if search_cross(r, c, puzzle):
                ans += 1
    return ans

print("Part 1:", part1(puzzle))
print("Part 2:", part2(puzzle))