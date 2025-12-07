#!/usr/bin/env python3
import sys

def parse_input(filename):
    with open(filename) as f:
        return f.read().strip()

def solve(data, part=1):
    grid = [[c for c in line] for line in data.splitlines()]
    s_idx = -1
    for i in range(len(grid[0])):
        if grid[0][i] == "S":
            s_idx = i

    ans = 0
    beams = {s_idx}
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

if __name__ == "__main__":
    input_type = sys.argv[1] if len(sys.argv) > 1 else "sample"
    part = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    
    filename = f"{input_type}.txt"
    data = parse_input(filename)
    result = solve(data, part)
    
    print(f"Part {part} ({input_type}): {result}")

