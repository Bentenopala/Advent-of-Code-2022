from collections import deque

def sg(relief):
    for i in range(len(relief)):
        for j in range(len(relief[i])):
            if relief[i][j] == 'S':
                start = (i,j)
            elif relief[i][j] == "E":
                goal = (i,j)
    return start, goal

def explored_map(relief):
    emap = dict() 
    for i in range(len(relief)):
        for j in range(len(relief[i])):
            emap[(i,j)] = dict()
            emap[(i,j)]['ex'] = 0
            emap[(i,j)]['ch'] = relief[i][j]
            if relief[i][j] == 'S':
                emap[(i,j)]['va'] = 1
            elif relief[i][j] == 'E':
                emap[(i,j)]['va'] = 26
            else:
                emap[(i,j)]['va'] = ord(relief[i][j]) - 96
    return emap

def bfs(relief, start, goal):
    m, n = len(relief), len(relief[0])
    emap = explored_map(relief)     # dict with expanded and characters
    frontier = deque()
    frontier.append([start])
    while frontier:
        path = frontier.popleft()
        #visualize(data, path, 0, n)
        current = path[-1]
        y, x = current
        if emap[current]['ex'] == 0:
            if current == goal:
                return len(path) - 1, path
            emap[current]['ex'] = 1
            ch, va = emap[current]['ch'], emap[current]['va']
            for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                yi, xi = y + dy, x + dx
                if (0 <= yi < m) and (0 <= xi < n):
                    chi, vai = emap[(yi, xi)]['ch'], emap[(yi, xi)]['va']
                    if vai <= va + 1:
                    #if abs(vai - va) <= 1:
                        cp_path = path[:]
                        cp_path.append((yi, xi))
                        frontier.append(cp_path)
    return "No path found.", path

def visualize(relief, path, xi, xf):
    m, n = len(data), len(data[0])
    vmap = [[0 for j in range(n)] for i in range(m)]
    for i in range(len(vmap)):
        for j in range(len(vmap[0])):
            point = (i, j)
            if point in path:
                vmap[i][j] = data[i][j]
            else:
                vmap[i][j] = " "
    for y in range(len(vmap)):
        print(*vmap[y][xi:xf]," | ",*data[y][xi:xf])
    print(" ")


def best_from(relief, character):
    start, goal = sg(relief)
    emap = explored_map(relief)
    positions = set([k for k,v in emap.items() if v['ch'] == 'a'])
    best = float('inf')
    for p in positions:
        steps, path = bfs(relief, p, goal)
        if steps != "No path found.":
            best = min(steps, best)
    return best


with open('day12.txt') as myfile:
    data = myfile.read().strip().split("\n")
    start, goal = sg(data)
    steps, path = bfs(data, start, goal)
    print(steps)
    print(best_from(data, 'a'))
    #visualize(data, path, 0, len(data[0]))
    #visualize(data, path, 145, len(data[0])-5)



