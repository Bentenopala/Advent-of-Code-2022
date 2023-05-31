
def count_ls(data):
	count = 0
	for h in data:
		if h == "$ ls":
			count += 1
	return count

def full_space(count):
	full = [[[],[],[],0] for e in range(count+1)]		# route, dirs, files, total size
	return full

def go_parent(command):
	gop = False
	if command == "$ cd ..":
		gop = True
	return gop

def history(data):
	full = full_space(count_ls(data))
	route = []
	total_size, i = 0, 0
	for h in data:
		if h.startswith("dir "):
			full[i][1].append(h.replace("dir ", ""))	
		elif h[0] in "0123456789":
			file = h.split(" ")
			full[i][2].append([file[1],file[0]])
			total_size += int(file[0])
			full[i][3] = total_size
		elif h.startswith("$ cd ") and go_parent(h) == False:
			i += 1
			last_dir = h.replace("$ cd ", "")
		elif h.startswith("$ ls"):
			route.append(last_dir)
			full[i][0].extend(route)
			total_size = 0
		elif h.startswith("$ cd .."):
			route.pop()
	return full

def inventory(data):
	full = history(data)[1:]
	all_dirs = []
	for n in range(len(full)):
		dir_info = [0,"","",0]	# depth, parent, name, size
		dir_info[0] = len(full[n][0])	# depth
		if len(full[n][0]) > 1:			# parent
			dir_info[1] = full[n][0][-2]
		dir_info[2] = full[n][0][-1]	# name
		dir_info[3] = full[n][3]		#size
		all_dirs.append(dir_info)
	for i in range(len(all_dirs)-1,-1,-1):
		depth, parent, size = all_dirs[i][0], all_dirs[i][1], all_dirs[i][3]
		for j in range(i,-1,-1):
			if all_dirs[j][0] == depth-1 and all_dirs[j][2] == parent:
				all_dirs[j][3] += size
				break
	return all_dirs

def sum_size(inv, max_size):
	s = 0
	for i in range(len(inv)):
		if inv[i][3] <= max_size:
			s += inv[i][3]
	return s

def smallest_erase(inv, needed_space, capacity):
	used = inv[0][3]
	to_remove = needed_space - (capacity - used)
	min_size = used
	for i in range(len(inv)):
		if inv[i][3] >= to_remove:
			min_size = min(min_size,inv[i][3])
	return min_size


with open("day07.txt", "rt") as myfile:
    data = myfile.read().strip().split("\n")

    print((sum_size(inventory(data),100000)))
    print(smallest_erase(inventory(data),30000000,70000000))