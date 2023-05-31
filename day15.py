
def parse(data):
    ssbb = []
    for i in range(len(data)):
        line = data[i].replace("Sensor at ", "").replace("x=","").replace("y=","").replace(" closest beacon is at ", "")
        line = line.split(":")
        s_b = []
        for j in line:
            r = eval(f"({j})")
            s_b.extend(r)
        s_b.extend([abs(s_b[0]-s_b[2])+abs(s_b[1]-s_b[3])])
        ssbb.append(tuple(s_b))
    ssbb_sorted = sorted(ssbb, key=lambda x: (x[1], x[0]))
    return ssbb_sorted


def ssbb_dict(sensors_beacons_list):
    ssbb, notin = sensors_beacons_list, dict()
    for var in ssbb:
        if var[1] not in notin:
            notin[var[1]] = dict()
        if var[3] not in notin:
            notin[var[3]] = dict()
        notin[var[1]][(var[0],var[0])] = "S"
        notin[var[3]][(var[2],var[2])] = "B"
    return notin


def not_in_query(sensors_beacons_list, not_in_dict, y_coord):
    ssbb, notin, query = sensors_beacons_list, not_in_dict, y_coord
    if query not in notin:
        notin[query] = dict()
    for var in ssbb:
        i = abs(query - var[1])
        if i <= var[4]:
            notin = update_notin(notin, query, (var[0] - var[4] + i, var[0] + var[4] - i))
    return notin


def update_notin(not_in_dict, y_coord, candidate_range):
    notin, y, r = not_in_dict, y_coord, candidate_range
    nin_rngs = list(k for k,v in notin[y].items() if v == False)
    nrngs = get_ranges(notin, y, r)
    if len(nin_rngs) == 0 and len(nrngs) > 0:
        notin[y].update({k: False for k in nrngs})
    else: 
        mrngs = merge(nin_rngs + [r])
        for ninr in nin_rngs:
            for m in mrngs:
                if m[1] < ninr[0] or ninr[1] < m[0]:
                    nrngs = get_ranges(notin, y, (m[0], m[1]))
                    notin[y].update({k: False for k in nrngs})
                elif ninr[0] <= m[0] <= m[1] <= ninr[1]:
                    continue
                else:
                    del notin[y][ninr]
                    nmin, nmax = min(m[0], ninr[0]), max(m[1], ninr[1])
                    nrngs = get_ranges(notin, y, (nmin, nmax))
                    notin[y].update({k: False for k in nrngs})
    notin = dict(sorted(notin.items()))
    return notin


def get_ranges(notin_dict, y_coord, range_tuple):
    notin, y, rng = notin_dict, y_coord, range_tuple
    rngs, candidates, sandb = [], [rng], get_sb(notin, y)
    if len(sandb) == 0:
        return [rng]
    for sb in sandb:
        while candidates:
            rng = candidates[-1]
            if (sb,sb) == rng:
                candidates.pop()
            elif sb not in range(rng[0], rng[1]+1):
                rngs.append((rng[0], rng[1]))
                candidates.pop()
            elif sb == rng[0]:
                candidates = [(rng[0]+ 1, rng[1])] + candidates
                candidates.pop()
            elif sb == rng[1]:
                candidates = [(rng[0], rng[1]-1)] + candidates
                candidates.pop()
            elif sb in range(rng[0]+1, rng[1]):
                candidates = [(rng[0], sb-1), (sb+1, rng[1])] + candidates
                candidates.pop()
    return rngs


def get_sb(notin_dict, y_coord):
    notin, y = notin_dict, y_coord
    return sorted([j[0] for j in [k for k,v in notin[y].items() if isinstance(v,str)] if j != []])


def merge(range_list):
    rngs = sorted([list(r) for r in range_list])
    newr = [rngs[0]]
    for r in rngs:
        if r[0] <= newr[-1][1]:
            newr[-1][1] = max(newr[-1][1], r[1])
        else:
            newr.append(r)
    return [tuple(nr) for nr in newr]


def count_not_in(notin_dict, y_coord):
    notin, y = notin_dict, y_coord
    nin_rngs = list(k for k,v in notin[y].items() if v == False)
    count = 0
    for nr in nin_rngs:
        count += nr[1] - nr[0] +1
    return count

def locate_distress(sensors_beacons_list, min_query, max_query):
    ssbb, minq, maxq = sensors_beacons_list, min_query, max_query
    for query in range(maxq+1,minq-1,-1):
        rngs = []
        for var in ssbb:
            i = abs(query - var[1])
            if i <= var[4]:
                rngs.append((var[0] - var[4] + i, var[0] + var [4] - i))
        mrngs = merge(rngs)
        if len(mrngs) == 2:
            if mrngs[1][0] - mrngs[0][1] == 2:
                x = mrngs[0][1] + 1
                frecuency = 4000000*x + query
                return frecuency
    return None

with open('day15.txt') as myfile:
    data = myfile.read().strip().split("\n")
    #print(data)

ssbb = parse(data)

# PART 1
notin = ssbb_dict(ssbb)
query = 2000000
notin = not_in_query(ssbb, notin, query)
print(count_not_in(notin, query))


# PART 2
maxq = 4000000
minq = 0
print(locate_distress(ssbb, minq, maxq))


'''
p1: 4861076
p2: 10649103160102
'''