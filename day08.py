
def create_score_dict(m,n):
    sco = dict()
    for i in range(0,m):
        sco[i] = dict()
        for j in range(0,n):
            sco[i].update({j: {"n": 0, "s": 0, "w": 0, "e": 0,}})
    return sco


def create_vis_dict(m,n):
    vis = create_score_dict(m,n)
    for i in range(0,m):
        for j in range(0,n):
            if i == 0:
                vis[i].update({j: {"n": 1}})
            elif i == m-1:
                vis[i].update({j: {"s": 1}})
            elif j == 0:
                vis[i].update({j: {"w": 1}})
            elif j == m-1:
                vis[i].update({j: {"e": 1}})
    return vis


def vis_latitude(data,vis_dict,d):
    m, n = len(data), len(data[0])
    vis = vis_dict
    mi, mf, ms = 1, len(data)-1, 1
    ni, nf, ns = 1, len(data[0])-1, 1
    if d == "n":   # north
        edge, d = tuple([int(i) for i in data[0]]), "n"
    elif d == "s":    # south
        edge, d = tuple([int(i) for i in data[-1]]), "s"
        mi, mf, ms = len(data)-2, 0, -1
    mini, maxi = [e+1 for e in edge], 9
    for i in range(mi,mf,ms):
        for j in range(ni,nf,ns):
            if int(data[i][j]) in range(mini[j],maxi):
                vis.get(i).get(j)[d] += 1
                mini[j] = int(data[i][j]) + 1
            elif int(data[i][j]) == 9 and mini[j] < 10:
                vis.get(i).get(j)[d] += 1
                mini[j], maxi = 10, 11
    return vis


def vis_longitude(data,vis_dict,d):
    m, n = len(data), len(data[0])
    vis = vis_dict
    mi, mf, ms = 1, len(data)-1, 1
    ni, nf, ns = 1, len(data[0])-1, 1
    if d == "w":     # west
        edge, d = tuple([int(i[0]) for i in data]), "w"
    elif d == "e":    # east
        edge, d = tuple([int(i[-1]) for i in data]), "e"
        ni, nf, ns = len(data[0])-2, 0, -1
    mini, maxi = [e+1 for e in edge], 9
    for i in range(mi,mf,ms):
        for j in range(ni,nf,ns):
            if int(data[i][j]) in range(mini[i],maxi):
                vis.get(i).get(j)[d] += 1
                mini[i] = int(data[i][j]) + 1
            elif int(data[i][j]) == 9 and mini[i] < 10:
                vis.get(i).get(j)[d] += 1
                mini[i], maxi = 10, 11
    return vis


def count_visibility(data):
    m, n, nvis = len(data), len(data[0]), 0
    vis = create_vis_dict(m, n)
    visn = vis_latitude(data,vis,"n")
    viss = vis_latitude(data,visn,"s")
    visw = vis_longitude(data,viss,"w")
    vis = vis_longitude(data,visw,"e")
    counter = 0
    for i in range(m):
        for j in range(n):
            if sum(vis.get(i).get(j).values()) > 0:
                nvis += 1
    return nvis


def create_score_list(m,n):
    scolst = [[[0,0,0,0] for j in range(n)] for i in range(m)]
    return scolst


def score_latitude(data,score_list,d):
    m, n = len(data), len(data[0])
    sco, score = score_list, 0
    if d == "n":
        d, mi, mf, step = 0, 1, m, -1
    elif d == "s":
        d, mi, mf, step = 1, 0, m-1, 1
    for i in range(mi,mf):
        for j in range(n):
            score = 0
            for k in range(m)[i+step::step]:
                score += 1
                sco[i][j][d] = score
                if int(data[k][j]) >= int(data[i][j]):
                    break
    return sco


def score_longitude(data,score_list,d):
    m, n = len(data), len(data[0])
    sco, score = score_list, 0
    if d == "w":
        d, ni, nf, step = 2, 1, n, -1
    elif d == "e":
        d, ni, nf, step = 3, 0, n-1, 1
    for i in range(m):
        for j in range(ni,nf):
            score = 0
            for k in range(n)[j+step::step]:
                score += 1
                sco[i][j][d] = score
                if int(data[i][k]) >= int(data[i][j]):
                    break
    return sco


def max_score(data):
    m, n, max_sco = len(data), len(data[0]), 0
    sco = create_score_list(m,n)
    scon = score_latitude(data,sco,"n")
    scos = score_latitude(data,scon,"s")
    scow = score_longitude(data,scos,"w")
    scoe = score_longitude(data,scow,"e")
    for i in range(m):
        for j in range(n):
            s = 1
            for k in range(4):
                s = s*scoe[i][j][k]
            if s > max_sco:
                max_sco = s
    return max_sco


with open("day08.txt", "rt") as myfile:
    data = myfile.read().strip().split("\n")
    print(count_visibility(data))
    print(max_score(data))
