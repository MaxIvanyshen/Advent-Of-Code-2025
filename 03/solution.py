#!/usr/bin/env python3
import sys

def parse_input(filename):
    with open(filename) as f:
        return f.read().strip()

def solve(data, part=1):
    max_n = 2 if part == 1 else 12
    ans = 0
    for line in data.splitlines():
        l = len(line)
        old_l = l
        while l != max_n:
            for i in range(l-1):
                if i + 1 < l and line[i] < line[i+1]:
                    line = line[:i] + line[i+1:]
                    l = len(line)
                    break
            if old_l == l:
                line = line[:l-1]
                l -= 1
            old_l = l
        ans += int(line)
    return ans


if __name__ == "__main__":
    input_type = sys.argv[1] if len(sys.argv) > 1 else "sample"
    part = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    
    filename = f"{input_type}.txt"
    data = parse_input(filename)
    result = solve(data, part)
    
    print(f"Part {part} ({input_type}): {result}")

