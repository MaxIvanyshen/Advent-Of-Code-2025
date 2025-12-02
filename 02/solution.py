#!/usr/bin/env python3
import sys

def parse_input(filename):
    with open(filename) as f:
        return f.read().strip()

def stupidity(n):
    sj = str(n)
    l = len(sj)
    e = 0
    while e != len(sj):
        e += 1 # increase for the next step
        if l % e != 0 or l == e:
            continue
        sub = sj[:e]
        count = 1
        for k in range(e, l, e):
            x = sj[k:k+e]
            if x == sub:
                count += 1
        if count * e == l:
            return count
    return -1


def solve(data, part=1):
    p1, p2 = 0, 0
    ranges = data.split(",")
    c = 0
    for i in range(len(ranges)):
        start, end = [int(s) for s in ranges[i].split("-")]
        for j in range(start, end + 1):
            s = stupidity(j)
            if s != -1:
                p2 += j
                if s % 2 == 0:
                    c += 1
                    p1 += j
    return p1 if part == 1 else p2


if __name__ == "__main__":
    input_type = sys.argv[1] if len(sys.argv) > 1 else "sample"
    part = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    
    filename = f"{input_type}.txt"
    data = parse_input(filename)
    result = solve(data, part)
    
    print(f"Part {part} ({input_type}): {result}")

