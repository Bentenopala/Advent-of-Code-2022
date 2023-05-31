
def count_visited(data,knots):
    k = knots
    moves = data
    knots = [[0,0] for i in range(k)]
    ihat = {"R": 1, "L": -1,"U": 0, "D": 0}
    jhat = {"R": 0, "L": 0,"U": 1, "D": -1}
    visited = {(0,0)}
    for m in moves:
        s = int(m[2:])
        signx = ihat.get(m[0])
        signy = jhat.get(m[0])
        dxh = signx*s
        dyh = signy*s
        for steps in range(s):
            knots[0][0] += dxh//abs(dxh) if dxh else 0
            knots[0][1] += dyh//abs(dyh) if dyh else 0
            for i in range(1, len(knots)):
                hx, hy = knots[i-1]
                tx, ty = knots[i]
                dx = hx - tx
                dy = hy - ty
                if abs(dx) > 1 or abs(dy) > 1:
                    tx += dx//abs(dx) if dx else 0
                    ty += dy//abs(dy) if dy else 0
                knots[i][0], knots[i][1] = tx, ty
            visited.add(tuple(knots[-1]))
    return len(visited)


with open("day09.txt", "rt") as myfile:
    data = myfile.read().strip().split("\n")
    print(count_visited(data,2))
    print(count_visited(data,10))