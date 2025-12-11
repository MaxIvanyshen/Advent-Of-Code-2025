#!/usr/bin/env python3
import sys

def parse_input(filename):
    with open(filename) as f:
        return f.read().strip()

cache = {}

def dfs(edges, curr="svr", dac = False, fft = False, part = 1):
    key = (curr, dac, fft)
    if key in cache:
        return cache[key]
    if curr == "out":
        if part == 1:
            return 1
        cache[key] = 1 if dac and fft else 0
        return cache[key] 
    ans = 0
    for edge in edges[curr]:
        ans += dfs(edges, edge, True if edge == "dac" else dac, True if edge == "fft" else fft, part)
    cache[key] = ans
    return ans 

def solve(data, part=1):
    edges = dict(set())
    for conn in data.splitlines():
        out, to = [x.strip() for x in conn.split(":")]
        edges[out] = set(to.split())
    return dfs(edges, "you") if part == 1 else dfs(edges, "svr", part=2)

if __name__ == "__main__":
    input_type = sys.argv[1] if len(sys.argv) > 1 else "sample"
    part = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    
    filename = f"{input_type}.txt"
    data = parse_input(filename)
    result = solve(data, part)
    
    print(f"Part {part} ({input_type}): {result}")

