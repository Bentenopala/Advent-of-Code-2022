
def list_rocks(data):
    rs = []
    for i in range(len(data)):
    	line = data[i].split(" -> ")
    	rock = []
    	for j in line:
    		r = eval(f"({j})")
    		rock.append(r)
    	rs.append(rock)
    return rs

def to_still(still_list, list_items):
	s, itms = still_list, list_items
	for i in itms:
		for j in range(1,len(i)):
			minx, maxx = min(i[j-1][0], i[j][0]), max(i[j-1][0], i[j][0])
			miny, maxy = min(i[j-1][1], i[j][1]), max(i[j-1][1], i[j][1])
			s.append([minx, maxx, miny, maxy])
	return s


def fill_cave(still_list):
	s, cave = still_list, dict()
	for r in s:
		for i in range(r[0],r[1]+1):
			for j in range(r[2],r[3]+1):
				cave[(i,j)] = False
	return cave

def falling(still_list, x_source, y_source, part):
	s, xs, ys, p = still_list, x_source, y_source, part
	x, y = x_source, y_source
	md, c = max_depth(s), fill_cave(s)
	grains, f = 0, True
	while f:
		f, c, x, y, grains = fall(c, x, y, md, grains, p)
		x, y = xs, ys
	return grains

def fall(cave_dict, x_coord, y_coord, max_depth, grains, part):
	c, x, y, md, g, p = cave_dict, x_coord, y_coord, max_depth, grains, part
	if is_air(c, 500, 0) == False:
		return (False, c, x, y, g)
	down = is_air(c, x, y+1)
	left = is_air(c, x-1, y+1)
	right = is_air(c, x+1, y+1)
	if down:
		for d in range(y, md+p):
			down = is_air(c, x, d)
			if down == False:
				return fall(c, x, d-1, md, g, p)
			y = d
		if p == 2:
			c[(x,y)] = False
			return (True, c, x, y, g+1)
		return (False, c, x, y, g)
	if left:
		return fall(c, x-1, y+1, md, g, p)
	elif right:
		return fall(c, x+1, y+1, md, g, p)
	else: 
		c[(x, y)] = False
		return (True, c, x, y, g+1)

def is_air(cave_dict, x_coord, y_coord):
	c, x, y = cave_dict, x_coord, y_coord
	return False if (x,y) in c else True


def max_depth(still_list):
	return max(i[3] for i in still_list)


with open('day14.txt') as myfile:
    data = myfile.read().strip().split("\n")
    rocks = list_rocks(data)
    still = to_still([], rocks)
    print(falling(still, 500, 0, 1))
    print(falling(still, 500, 0, 2))
    #p1: 665
    #p2: 25434
    