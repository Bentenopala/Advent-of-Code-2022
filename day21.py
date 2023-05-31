
def monkey_inventory(monkey_list):
    ml, mdict = monkey_list, dict()
    for m in monkey_list:
        if len(m) < 17:
            mdict[m[:4]] = int(m[6:])
        else:
            mdict[m[:4]] = {'mm': [m[6:10], m[13:]], 'op': m[11:12]}
    return mdict


def monkey_order(monkey_list):
    ml = monkey_list
    return tuple([m[:4] for m in ml])


def test_update(monkey):
    m = monkey
    return all([k in yelled for k in inv[m]['mm']])


def do_job(monkey):
    m = monkey
    if test_update(m):
        m1, m2, op = inv[m]['mm'][0], inv[m]['mm'][1], inv[m]['op']
        inv[m] = operate(inv[m1], inv[m2], op)
        yelled.append(m)
        up = m
        if m in waiting:
            waiting.remove(m)
    else:
        waiting.append(m)
        up = False
    return up


def operate(n1, n2, operation):
    op = operation
    match op:
        case '+':
            return n1 + n2
        case '-':
            return n1 - n2
        case '*':
            return n1 * n2
        case '/':
            return int(n1 / n2)

with open('day21.txt') as myfile:
    data = myfile.read().strip().split("\n")

inv = monkey_inventory(data)
order = monkey_order(data)


yelled = []
waiting = []
for m in order:
    if isinstance(inv[m],int):
        yelled.append(m)
    else:
        waiting.append(m)
    update = True
    while update:
        jobs = [k for k in waiting if test_update(k)]
        update = True if len(jobs)>0 else False
        for job in jobs:
            update = do_job(job)


print(inv['root'])


'''
p1: 87457751482938
'''