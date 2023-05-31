
def mixing(position, max_position, value):
    pos, mx, val = position, max_position, value
    if val >= 0 and pos + val <= mx:
        npos = pos + val
    elif val >= 0 and pos + val > mx:
        npos = (pos + 1 + val) % (mx + 1)
    elif val < 0:
        npos = (pos + val) % mx
        if npos == 0:
            return maxpos
    return npos


with open('day20.txt') as myfile:
    data = [(n, int(v)) for n,v in enumerate(myfile.read().strip().split("\n"))]


moved = data[:]
maxpos = len(moved) - 1

for c in data:
    #print(c)
    v = c[1]
    pos = moved.index(c)
    moved.remove(c)
    npos = mixing(pos, maxpos, v)
    moved.insert(npos,c)
    #print(moved)

grove = []
poszero = moved.index(([t[0] for t in moved if t[1] == 0][0],0)) #- 1
for th in [1000,2000,3000]:
    grove.append(moved[mixing(poszero, maxpos,th)][1])


print(grove)
print(sum(grove))


