
def new_sep(data):
	'''
	Replaces single new lines with '#', double new lines with '$', and also inserts '$' at the end of the string.
	'''
	text = data.strip().replace('\n\n','$').replace('\n','#')+ '$'
	return text

def identify_elf(data):
	'''
	Uses new_sep() to identify the elf with most calories and returns both values in a list [calories, elf]
	'''
	text = new_sep(data)
	num_str, num = "", 0
	elf_cal, max_cal, topcal = 0, 0, [0,0,0]
	elf_num, max_elf, topelf = 0, 0, [0,0,0] 	# For elves identification, included just because task stated:
												# "Find the Elf carrying the most Calories", but not needed for final answer.
	for c in text:
		if c in "0123456789":  # number in string form
			num_str += c 
		elif c == "#":  # end of number, converts to int and adds to count
			num = int(num_str)
			elf_cal += num
			num_str = ""
		elif c == "$":  # end of elf count, converts to int, adds to count, and updates top list
			num = int(num_str)
			elf_cal += num
			elf_num += 1	# elf id, not needed for final result
			for i in range(len(topcal)):
				if elf_cal > topcal[i]:
					topcal.insert(i,elf_cal)
					topcal.pop(-1)
					topelf.insert(i,elf_num)  	# elf id, not needed for final result
					topelf.pop(-1)				# elf id, not needed for final result
					break
			elf_cal = 0
			num_str = ""
	return [topelf,topcal]

def max_calories(data):
	'''
	Returns the maximum amount of calories that is carried by a single elf.
	'''
	elf_cals = identify_elf(data)
	return elf_cals[1][0]

def sum_cal_top3(data):
	'''
	Returns the sum of the calories carried by the 3 elfs that are carrying 
	more calories.
	'''
	return sum(identify_elf(data)[1])

with open("day01.txt", "rt") as myfile:
	data = myfile.read()
	
	print(max_calories(data))
	print(sum_cal_top3(data))
