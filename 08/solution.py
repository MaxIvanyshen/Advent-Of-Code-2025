#!/usr/bin/env python3
import sys
import math
import heapq

def parse_input(filename):
    with open(filename) as f:
        return f.read().strip()

def distance(a, b):
    return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2) + math.pow(a[2]- b[2], 2))

class Conn:
    def __init__(self, a, b, dist):
        self.a = a
        self.b = b
        self.dist = dist

    def __str__(self):
        return f'[from={self.a};to={self.b};dist={self.dist}]'

    def __repr__(self):
        return f'[from={self.a};to={self.b};dist={self.dist}]'

    def __lt__(self, other):
        return self.dist < other.dist

    def __gt__(self, other):
        return self.dist > other.dist

    def __eq__(self, other):
        return (self.a, self.b) == (other.a, other.b)

    def __hash__(self):
        return hash(tuple(sorted([self.a, self.b])))

def solve(data, part=1):
    boxes = []
    for line in data.splitlines():
        x, y, z = [int(x) for x in line.split(",")]
        boxes.append((x, y, z))

    conn_set = set()
    conns = []
    for i in range(len(boxes)):
        for j in range(i+1, len(boxes)):
            if i == j or Conn(boxes[j], boxes[i], distance(boxes[i], boxes[j])) in conn_set:
                continue
            conn_set.add(Conn(boxes[i], boxes[j], distance(boxes[i], boxes[j])))

    conns = list(conn_set)
    heapq.heapify(conns)

    circuits = [] # a list of sets of boxes
    last = conns[0]
    n = 1000 if part == 1 else len(conns)
    for i in range(n):
        curr = heapq.heappop(conns)

        a, b = curr.a, curr.b
        found_a = found_b = None

        for i, component in enumerate(circuits):
            if a in component:
                found_a = i
            if b in component:
                found_b = i

        if found_a is not None and found_b is not None:
            if found_a == found_b:
                continue  
            else:
                circuits[found_a].update(circuits[found_b])
                del circuits[found_b]
        elif found_a is not None:
            circuits[found_a].add(b)
        elif found_b is not None:
            circuits[found_b].add(a)
        else:
            circuits.append({a, b})

        last = curr

    if part == 1:
        lens = [len(c) for c in circuits]
        heapq.heapify_max(lens)
        return lens[0] * lens[1] * lens[2]
    else:
        return last.a[0] * last.b[0]

if __name__ == "__main__":
    input_type = sys.argv[1] if len(sys.argv) > 1 else "sample"
    part = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    
    filename = f"{input_type}.txt"
    data = parse_input(filename)
    result = solve(data, part)
    
    print(f"Part {part} ({input_type}): {result}")

