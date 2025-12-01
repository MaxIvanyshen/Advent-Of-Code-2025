import sys

test = True if len(sys.argv) > 1 and sys.argv[1] == "-t"  else False

moves = [s.rstrip() for s in open("test.txt" if test else "real.txt", "r").readlines()]

p = 50
base = 100

ans = 0

for move in moves:
    dir = -1 if move[0] == "L" else 1
    m = dir * int(move[1:])
    p = p + m

    if p < 0:
        p = (base - abs(p)) % base
    elif p >= base: 
        p = abs(p) % base

    print(p)
    if p == 0:
        ans += 1

print("-" * 10)
print(ans)


