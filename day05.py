
def columns_pos(data):
    """
    Obtains the position inside the text where the letters of the crates are.
    data: list of lines, except blank lines.
    return: touple with the positions of the stack in the text as an integer.
    """
    col_pos = ()
    for line in data:
        if line.startswith(" 1"):           # select the line that indicates the stacks number
            for i in range(len(line)):
                if line[i] in "0123456789":
                    col_pos = (*col_pos, len(line[0:i])) # select pos where there are numbers
    return col_pos

def initial_stacks(data):
    """
    Creates a list of the initial arrangement of the crates in each stack.
    data: list of lines, except blank lines.
    return: list of stacks [leftmost, rightmost]. Each stack is a list of crates [bottom,top]
    """
    cp, data_stacks = columns_pos(data), []
    for l in data:  
        if not(l.startswith(" 1") or l.startswith("m")):
            data_stacks.append([l[i] for i in cp])      # maps stacks to matrix (has blank spaces)
    m, n = len(data_stacks), len(cp)
    istacks = [[] for s in range(n)]
    for i in range(n):
        for j in range(m-1,-1,-1):
            if data_stacks[j][i] != " ":                # No blank spaces
                istacks[i].append(data_stacks[j][i])    # Each row is a stack of crates [bottom,top]
    return istacks

def instructions(data):
    """
    Obtains the number n of crates to move, from stack f to stack t.
    data: list of lines, except blank lines.
    return: list of instructions, each instruction is a list in the form [n, f, t].
    """
    guide_nft = []
    for line in data:
        if line.startswith("m"):
            nft = [int(e) for e in line.split() if e not in ["move","from","to"]]
            guide_nft.append(nft)
    return guide_nft

def move_crates(data, CrateMover_model = 9001):
    """
    Move the crates accordingly to the instructions guide.
    data: list of lines, except blank lines.
    CrateMover_model:   9000: moves the crate at the top of a stack per move; 
                        9001: moves n consecutive crates (including the one at the top) per move.
    return: list of stacks [leftmost, rightmost] after moving the crates. Each stack is a list of crates [bottom, top].
    """
    guide_nft = instructions(data)
    stacks = initial_stacks(data)
    for i in guide_nft:
        n, f, t = i[0], i[1]-1, i[2]-1  # n: number of crates, f: from stack, t: to stack
        if CrateMover_model == 9000:
            for j in range(n):
                stacks[t].append(stacks[f][-1])
                stacks[f].pop()
        elif CrateMover_model == 9001:
            stacks[t].extend(stacks[f][-n:])
            del stacks[f][-n:]
        else: 
            raise ValueError("Second argument must be 9000 or 9001.")
    return stacks

def top_crates(stacks):
    """
    Gets the letter of the top crates of each stack, left to right.
    stacks: list of stacks [leftmost, rightmost]. Each stack is a list of crates [bottom, top].
    return: string with the letters of the crates one after the other.
    """
    top = "" 
    for i in stacks:
        top += i[-1]
    return top

def visualize(stacks):
    """
    Prints the stacks in horizontal form.
    stacks: list of stacks [leftmost, rightmost]. Each stack is a list of crates [bottom, top].
    """
    count, s_str = 0, ""
    for i in stacks:
        count += 1
        s_str += str(count)+" "
        for c in i:
            s_str += c
        s_str += "\n"
    print(s_str)


with open("day05.txt", "rt") as myfile:
    data = myfile.read().rstrip().replace('\n\n','\n').split('\n')
    
    print(top_crates(move_crates(data,9000)))
    print(top_crates(move_crates(data,9001)))
