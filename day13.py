
def to_list(data):
    packets = [[] for i in range(len(data))]
    for i in range(len(data)):
        packets[i] = data[i].split("\n")
        for j in range(len(packets[i])):
            packets[i][j] = eval(packets[i][j])
    return packets


def unpack(index, left, right):
    i, l, r = index, left, right
    if isinstance(l,int) and isinstance(r,int):
        return evaluate(i, l, r)
    elif isinstance(l, int) and isinstance(r, list):
        nl, nr = [l], r
    elif isinstance(l, list) and isinstance(r, int):
        nl, nr = l, [r]
    else:
        nl, nr = l, r
    min_len = min(len(nl), len(nr))
    if min_len == 0:
        comp = evaluate(i, len(nl), len(nr))
        comp[1], comp[2] = [len(nl)], [len(nr)]
        return comp
    else:
        for j in range(min_len):
            comp = unpack(i, nl[j], nr[j])
            if comp[3] != 0 or comp[4] != 0:
                return comp
            elif j == min_len - 1 and (comp[3] == 0 or comp[4] == 0):
                comp = evaluate(i, len(nl), len(nr))
                comp[1], comp[2] = [len(nl)], [len(nr)]
                return comp
        
def evaluate(index, li, ri):
    i = index
    if li < ri:
        return [i, li, ri, i + 1, 0]
    elif li > ri:
        return [i, li, ri, 0, i + 1]
    elif li == ri:
        return [i, li, ri, 0, 0]

def compare(left, right):
    all_comp = []
    for i in range(len(right)):
        l, r = left[i], right[i]
        comp = unpack(i, l, r)
        all_comp.append(comp)
    return all_comp

def part1(comp_list):
    index_sum = 0
    for e in comp_list:
        index_sum += e[3]
    return index_sum

def compare_one(left, right):
    all_comp = []
    for i in range(len(right)):
        l, r = left, right[i]
        comp = unpack(i, l, r)
        all_comp.append(comp)
    return all_comp

def get_pos(item, items):
    all_comp = compare_one(item, items)
    pos = 1
    for i in range(len(all_comp)):
        if all_comp[i][4] > 0:
            pos += 1
    return pos

with open('day13.txt') as myfile:
    data = myfile.read().strip().split("\n\n")
    ps = to_list(data)
    pl, pr = [], []
    for p in ps:
        pl.append(p[0])
        pr.append(p[1])
    
    # Answer part1
    print(part1(compare(pl, pr)))


    all_p = [[[2]], [[6]]]
    for j in range(len(ps)):
        for k in [0,1]:
            all_p.append(ps[j][k])

    pos2 = get_pos(all_p[0], all_p)
    pos6 = get_pos(all_p[1], all_p)

    # Answer part2
    print(pos2*pos6)


    # List in order
    inorder = [[] for i in all_p]
    for packet in all_p:
        pos = get_pos(packet, all_p)
        inorder[pos-1] = packet
    #print(inorder[pos2-1])
    #print(inorder[pos6-1])




