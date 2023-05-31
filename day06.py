
def nchr_to_marker(data,marker_length):
    """
    Searches in a string (with no blanks spaces) a substring (a marker) with n different characters.
    data: string with no spaces or punctutation before, between or after them them.
    marker_length: amount of different characters looked for (input must be a positive integer).
    return: number of letters processed until the marker with n different characters is found.

    """
    try:
        m = int(marker_length)    # marker length (m)
        if m <= 0:
            ncp = "Error: marker_length must be a positive integer."
        else:
            ncp = 0     # number of characters processed until finding the marker
            for i in range(len(data)-m-1):
                range_set = set([c for c in data[i:i+m]])
                if len(range_set) == m:
                    ncp = i + m
                    break
            if ncp == 0:
                ncp = f"There is no marker with {m} different letters."
        return ncp
    except: 
        return "Please input a positive integer as marker_length."


with open("day06.txt", "rt") as myfile:
    data = myfile.read().strip()
    
    print(nchr_to_marker(data,4))
    print(nchr_to_marker(data,14))