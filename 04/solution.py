#!/usr/bin/env python3
import sys

def parse_input(filename):
    with open(filename) as f:
        return f.read().strip()

def findLessThanFour(s, dirs):
    ans = 0
    for point in s:
        count = 0
        for d in dirs:
            if (point[0] + d[0], point[1] + d[1]) in s:
                count += 1
        if count < 4:
            ans += 1

    return ans

def findWithRemoval(s, dirs):
    ans = 0
    deleted = set()

    for point in s:
        count = 0
        for d in dirs:
            if (point[0] + d[0], point[1] + d[1]) in s:
                count += 1
        if count < 4:
            ans += 1
            deleted.add(point)

    for p in deleted:
        s.remove(p)

    return ans + findWithRemoval(s, dirs) if ans else 0

def solve(data, part=1):
    grid = []
    for line in data.splitlines():
        grid.append([c for c in line])

    s = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@":
                s.add((i, j))

    dirs = [
            [1, 0],
            [1, 1],
            [1, -1],

            [-1, -1],
            [-1, 1],
            [-1, 0],

            [0, 1],
            [0, -1]
    ]

    if part == 1:
        return findLessThanFour(s, dirs)
    return findWithRemoval(s, dirs)

if __name__ == "__main__":
    input_type = sys.argv[1] if len(sys.argv) > 1 else "sample"
    part = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    
    filename = f"{input_type}.txt"
    data = parse_input(filename)
    result = solve(data, part)
    
    print(f"Part {part} ({input_type}): {result}")

