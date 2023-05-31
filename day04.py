def ranges_str_to_lst(ranges_str):
	'''Converts a string containing two ranges in the form 'a-b,c-d' to a integer list [a, b, c, d]
	ranges_str: two ranges represented in a string in the form 'a-b,c-d'. '''
	num_str, ranges_lst = "", []
	for c in ranges_str:
		if c in "0123456789":	# Number in string form
			num_str += c
		elif c == "-":	# Append range's starting values
			ranges_lst.append(int(num_str))
			num_str = ""
		elif c == ",":	# Append first range's final value
			ranges_lst.append(int(num_str))
			num_str = ""
	ranges_lst.append(int(num_str)) # Append second range's final value
	num_str = ""
	return ranges_lst

def count_overlaps(data):
	'''Counts how many ranges overlap completely, partially or doesn't overlap.
	data: string with two ranges per line represented as 'a-b,c-d'. 
	Returns a list containing the total number of each case: [full_overlap, partial_overlap, no_overlap]'''
	full_overlap, partial_overlap, no_overlap = 0, 0, 0
	for line in data:
		pair = ranges_str_to_lst(line)
		if (pair[0] <= pair[2]) and (pair[1] >= pair[3]): # second range contained in first range
			full_overlap += 1
		elif (pair[2] <= pair[0]) and (pair[3] >= pair[1]): # first range contained in second range
			full_overlap += 1
		elif (pair[1] < pair[2]) or (pair[3] < pair[0]): # initial value of one range larger than final value the other range
			no_overlap += 1
		else:
			partial_overlap += 1
	return [full_overlap, partial_overlap, no_overlap]

def overlaps(data, overlap_type = "full"):
	'''Returns the count of ranges with full, partial or no overlap.
	data: string with two ranges per line represented as 'a-b,c-d'. 
	overlap_type: 'full', 'partial' or 'no'.'''
	fpn = count_overlaps(data)
	try: 
		if overlap_type == "full":
			overlaps = fpn[0]
		elif overlap_type == "partial":
			overlaps = fpn[1]
		elif overlap_type == "no":
			overlaps = fpn[2]
		else: 
			raise ValueError("Second argument must be 'full', 'partial' or 'no'.")
		return overlaps
	except: 
		print("Error: second argument must be type of overlap: 'full', 'partial' or 'no'.")

with open("day04.txt", "rt") as myfile:
    data = myfile.read().split()
    
    print(overlaps(data, "full"))
    print(overlaps(data, "full") + overlaps(data, "partial"))

