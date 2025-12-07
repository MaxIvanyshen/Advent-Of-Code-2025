#!/usr/bin/env python3
import sys

def parse_input(filename):
    with open(filename) as f:
        return f.read().strip()

def backtrack(grid, r, c, cache):
    for i in range(r, len(grid)):
        if grid[i][c] == "^":
            l, r = 0, 0

            if (i+1, c-1) in cache:
                l = cache[i+1, c-1]
            else:
                l = backtrack(grid, i + 1, c - 1, cache)
                cache[i+1, c-1] = l

            if (i+1, c+1) in cache:
                r = cache[i+1, c+1]
            else:
                r = backtrack(grid, i + 1, c + 1, cache)
                cache[i+1, c+1] = r

            return l + r

    return 1

def watch_in_parallel(grid, start_idx):
    ans = 0
    beams = {start_idx}
    for i in range(1, len(grid)):
        new_beams = set()
        delete = set()
        for b in beams:
            if grid[i][b] == "^":
                ans += 1
                delete.add(b)
                new_beams.add(b - 1)
                new_beams.add(b + 1)
        beams = (beams - delete) | new_beams
    return ans

def solve(data, part=1):
    grid = [[c for c in line] for line in data.splitlines()]
    s_idx = -1
    for i in range(len(grid[0])):
        if grid[0][i] == "S":
            s_idx = i

    if part == 1:
        return watch_in_parallel(grid, s_idx)
    else:
        cache = dict()
        return backtrack(grid, 1, s_idx, cache)


if __name__ == "__main__":
    input_type = sys.argv[1] if len(sys.argv) > 1 else "sample"
    part = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    
    filename = f"{input_type}.txt"
    data = parse_input(filename)
    result = solve(data, part)
    
    print(f"Part {part} ({input_type}): {result}")

