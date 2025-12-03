#!/usr/bin/env python3
import sys

def parse_input(filename):
    with open(filename) as f:
        return f.read().strip()

def solve(data, part=1):
    max_n = 2 if part == 1 else 12 # 2 for part 1, 12 for part 2
    ans = 0
    for line in data.splitlines():
        l = len(line)
        while l != max_n:
            for i in range(l + 1):
                if i + 1 < l and line[i] < line[i+1]: # if the current digit is lower than the next one - remove it 
                    line = line[:i] + line[i+1:]
                    break
                elif i == l: # if reached the end - remove the last digit
                    line = line[:l-1]
            l -= 1
        ans += int(line)
    return ans


if __name__ == "__main__":
    input_type = sys.argv[1] if len(sys.argv) > 1 else "sample"
    part = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    
    filename = f"{input_type}.txt"
    data = parse_input(filename)
    result = solve(data, part)
    
    print(f"Part {part} ({input_type}): {result}")

