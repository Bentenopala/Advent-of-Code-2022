
def types_in_both(data):
    '''Identifies letters that are in both the first and the second half of the string.
    Returns a list with the letter, but not the number of repetitions.'''
    in_both = []
    for rucksack in data:
        m, n = len(rucksack)//2, len(rucksack)
        s = rucksack[0:m]
        t = rucksack[m:n]
        match = next(i for i in s if i in t)
        in_both.append(match)
        # NICE ALT! Solution with sets:
        #s = set([es for es in rucksack[0:m]])
        #t = set([et for et in rucksack[m:n]])
        #match = next(iter(s & t))
        #in_both.append(match)
    return in_both

def obtain_badges(data):
    '''In groups of three lines, depending on the order of the input, identifies the letter that only line that they share.
    Returns a list of those letters.'''
    badges = []
    i = 0
    while i < len(data)-1:
        r = data[i]
        s = data[i+1]
        t = data[i+2]
        badge = next(b for b in r if b in s and b in t)
        badges.append(badge)
        i+=3
    return badges


def calculate_priority(types):
    '''Calculates priority converting each character to ASCII code and 
    taking a = 1 ... z = 26, A = 27...Z = 52.
    Returns the sum of the priorities.'''
    priority = 0
    for t in types:
        if t.islower() == True:
            priority += ord(t) - 96
        else:
            priority += ord(t) - 38
    return priority


with open("day03.txt", "rt") as myfile:
    data = myfile.read().strip().split()
    
    print(calculate_priority(types_in_both(data)))
    print(calculate_priority(obtain_badges(data)))