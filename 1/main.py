import sys

test = True if len(sys.argv) > 1 and sys.argv[1] == "-t"  else False

moves = [s.rstrip() for s in open("test.txt" if test else "real.txt", "r").readlines()]

p = 50
base = 100

ans = 0

for move in moves:
    dir = -1 if move[0] == "L" else 1
    m = int(move[1:])

    for i in range (0, m):
        if p == 99 and dir == 1:
            p = 0
        elif p == 0 and dir == -1:
            p = 99
        else:
            p += dir

        if p == 0:
            ans += 1

    print(p)

print("-" * 10)
print(ans)


