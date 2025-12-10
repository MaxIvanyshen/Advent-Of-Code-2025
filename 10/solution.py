#!/usr/bin/env python3
import sys
from collections import deque

def parse_input(filename):
    with open(filename) as f:
        return f.read().strip()


class Machine:
    def __init__(self, lights, buttons):
        self.buttons = buttons
        self.wanted = lights
        self.curr = ["."] * len(lights)

    def __str__(self):
        return f"[curr={self.curr};wanted={self.wanted};buttons={self.buttons}]"

    def __repr__(self):
        return f"[curr={self.curr};wanted={self.wanted};buttons={self.buttons}]"

    def __hash__(self):
        return hash(f"{tuple(self.curr)}-{tuple(map(tuple, self.buttons))}")


def toggle(state, button):
    new_state = list(state)
    for l in button:
        new_state[l] = "." if new_state[l] == "#" else "#"
    return tuple(new_state)


def min_presses(initial, wanted, buttons):
    q = deque([(initial, 0)])
    seen = set()
    while q:
        curr, presses = q.popleft()
        if curr == wanted:
            return presses
        for b in buttons:
            new = toggle(curr, b)
            if new not in seen:
                seen.add(new)
                q.append((new, presses+1))

    return float("inf")

def solve(data, part=1):
    machines = []
    for machine in data.splitlines():
        split = machine.split()
        state = list(split[0][1 : len(split[0]) - 1])
        buttons = []
        for b in split[1 : len(split) - 1]:
            buttons.append([int(x) for x in b[1 : len(b) - 1].split(",")])
        machines.append(Machine(state, buttons))

    ans = 0
    for m in machines:
        initial = tuple("." * len(m.wanted))
        presses = min_presses(initial, tuple(m.wanted), m.buttons)
        ans += presses
    return ans


if __name__ == "__main__":
    input_type = sys.argv[1] if len(sys.argv) > 1 else "sample"
    part = int(sys.argv[2]) if len(sys.argv) > 2 else 1

    filename = f"{input_type}.txt"
    data = parse_input(filename)
    result = solve(data, part)

    print(f"Part {part} ({input_type}): {result}")
