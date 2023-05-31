def get_register(data,query):
    d = data
    trans = {"noop": 1, "addx": 2}
    cycle, register, q = 0, 1, query
    for d in data:
        for c in range(trans.get(d[:4])):
            cycle += 1
            if cycle == query:
                break
        if cycle == query:
            break
        register += int(d[5:])
    return register

def get_strenght(cycle, register):
    return cycle*register

def get_cycles(data):
    trans = {"noop": 1, "addx": 2}
    total_cycles = 0
    for d in data:
        total_cycles += trans.get(d[:4])
    return total_cycles

def strength_queries(data, first, every_n_cycles):
    d, s, n = data, first, every_n_cycles
    strengths, e, total = [], get_cycles(d), 0
    for q in range(s,e+1,n):
        total += get_strenght(q, get_register(d,q)) 
    return total

def get_img(data):
    d = data
    e, n = get_cycles(d), 40 
    rows = [i for i in range(0,e,n)]
    trans = {"noop": 1, "addx": 2}
    cycle, img = 0, ""
    for row in rows:
        for p in range(row,row+n):
            register = get_register(data,p+1)
            if (p-row) in range(register-1,register+2):
                img += "#"
            else:
                img += "."
        img += "\n"

    return img[:-1]


with open("day10.txt", "rt") as myfile:
    data = myfile.read().strip().replace("noop", "noop 0").split("\n")
    print(strength_queries(data, 20, 40))
    print(get_img(data))
