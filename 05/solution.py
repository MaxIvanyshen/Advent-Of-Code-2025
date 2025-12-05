#!/usr/bin/env python3
import sys

def parse_input(filename):
    with open(filename) as f:
        return f.read().strip()

def merge_ranges(int_ranges):
    int_ranges.sort()

    i = 0
    while i < len(int_ranges) - 1:
        curr, other = int_ranges[i], int_ranges[i+1]
        if curr[1] >= other[0]:
            curr = (min(curr[0], other[0]), max(other[1], curr[1]))
            int_ranges[i] = curr
            int_ranges.pop(i+1)
        else:
            i += 1

    return int_ranges

def solve(data, part=1):
    ranges, fruits = [x.splitlines() for x in data.split("\n\n")]
    rs = []
    for r in ranges:
        s, e = r.split("-")
        rs.append((int(s), int(e)))

    ans = 0
    if part == 1:
        for c in fruits:
            f = int(c)
            for r in rs:
                if f >= r[0] and f <= r[1]:
                    ans += 1
                    break
    else:
        for r in merge_ranges(rs):
            ans += (r[1] - r[0] + 1)

    return ans

if __name__ == "__main__":
    input_type = sys.argv[1] if len(sys.argv) > 1 else "sample"
    part = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    
    filename = f"{input_type}.txt"
    data = parse_input(filename)
    result = solve(data, part)
    
    print(f"Part {part} ({input_type}): {result}")

