
def lava_air(cubes_list, cubes_dict):
    clist, cubes = cubes_list, cubes_dict
    n = len(clist)
    s = 0
    for c in clist:
        for dr in [-1,1]:
            s += 1 if (c[0]+dr,c[1],c[2]) in cubes else 0
            s += 1 if (c[0],c[1]+dr,c[2]) in cubes else 0
            s += 1 if (c[0],c[1],c[2]+dr) in cubes else 0
    return 6*n-s


def exterior(cubes_dict, min_vertex, max_vertex):
    cubes, minv, maxv = cubes_dict, min_vertex, max_vertex
    explored, frontier, ext = set(), [], 0
    frontier.append(maxv)
    while frontier:
        node = frontier[-1]
        frontier.pop()
        if node in cubes:
            ext += 1
        elif node not in explored:
            explored.add(node)
            frontier.extend(shell_neighbours(node, minv, maxv))
    return ext

def shell_neighbours(node, min_vertex, max_vertex):
    x, y, z = node
    minv, maxv = min_vertex, max_vertex
    ne = []
    ne.extend((x+dr, y, z) for dr in [-1,1] if minv[0] <= x+dr <= maxv[0])
    ne.extend((x, y+dr, z) for dr in [-1,1] if minv[1] <= y+dr <= maxv[1])
    ne.extend((x, y, z+dr) for dr in [-1,1] if minv[2] <= z+dr <= maxv[2])
    return ne

with open('day18.txt') as myfile:
    cubes = dict(sorted({eval('('+l+')'): True for l in myfile.read().strip().split("\n")}.items()))

clist = sorted(list(cubes.keys()))

# PART 1
print(lava_air(clist, cubes))

# Min and max vertices of a shell covering the lava polygon
minv = (min(c[0]-1 for c in clist), min(c[1]-1 for c in clist), min(c[2]-1 for c in clist))
maxv = (max(c[0]+1 for c in clist), max(c[1]+1 for c in clist), max(c[2]+1 for c in clist))

# PART 2
print(exterior(cubes, minv, maxv))


'''
p1: 3526
p2: 2090
'''