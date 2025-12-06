#!/usr/bin/env python3
import sys

def parse_input(filename):
    with open(filename) as f:
        return f.read().strip()

def solve(data, part=1):
    eq = [[x for x in line.split()] for line in data.splitlines()] # matrix of equations (column is an equation)
    ops = eq[-1]
    ans = [0 if op == "+" else 1 for op in ops]
    for j in range(len(eq[0])):
        for i in range(len(eq)-1):
            if ops[j] == "+":
                ans[j] += int(eq[i][j])
            else:
                ans[j] *= int(eq[i][j])
    return sum(ans)

if __name__ == "__main__":
    input_type = sys.argv[1] if len(sys.argv) > 1 else "sample"
    part = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    
    filename = f"{input_type}.txt"
    data = parse_input(filename)
    result = solve(data, part)
    
    print(f"Part {part} ({input_type}): {result}")

