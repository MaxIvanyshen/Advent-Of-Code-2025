#!/usr/bin/env python3
import sys

def parse_input(filename):
    with open(filename) as f:
        return f.read().strip()

def solve(data, part=1):
    rects = []
    for line in data.splitlines():
        curr_x, curr_y = line.split(",")
        rects.append((int(curr_x), int(curr_y)))

    ans = 0
    for i in range(len(rects)):
        curr = rects[i]
        for j in range(i + 1, len(rects)):
            other = rects[j]
            # print(curr, other)
            s = (abs(other[0] - curr[0])+1) * (abs(other[1] - curr[1])+1)
            if s > ans:
                ans = s
    return ans

if __name__ == "__main__":
    input_type = sys.argv[1] if len(sys.argv) > 1 else "sample"
    part = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    
    filename = f"{input_type}.txt"
    data = parse_input(filename)
    result = solve(data, part)
    
    print(f"Part {part} ({input_type}): {result}")

