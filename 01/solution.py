#!/usr/bin/env python3
import sys

def parse_input(filename):
    with open(filename) as f:
        return f.read().strip()

def solve(data, part=1):
    p = 50

    ans1 = 0
    ans2 = 0

    moves = data.splitlines()

    for move in moves:
        dir = -1 if move[0] == "L" else 1
        m = int(move[1:])

        for i in range (0, m):
            if p == 99 and dir == 1:
                p = 0
            elif p == 0 and dir == -1:
                p = 99
            else:
                p += dir

            if p == 0:
                ans2 += 1

        print(p)
        if part == 1 and p == 0:
            ans1 += 1
            ans2 += 1

    return ans1 if part == 1 else ans2

if __name__ == "__main__":
    input_type = sys.argv[1] if len(sys.argv) > 1 else "sample"
    part = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    
    filename = f"{input_type}.txt"
    data = parse_input(filename)
    result = solve(data, part)
    
    print(f"Part {part} ({input_type}): {result}")

