#!/usr/bin/python

def depths_from_file(fname):
	return [int(line) for line in open(fname,"r")]

def count_increases(depths):
	if len(depths) == 0:
		return 0
	base = depths[0]
	last = depths[0]
	ctr = 0
	for d in depths[1:]:
		if d > last:
			ctr += 1
		last = d
	return ctr

def make_windows(depths):
	if len(depths) < 3:
		return []
	val = depths[0] + depths[1] + depths[2]
	out = [depths[0] + depths[1] + depths[2]]

	for d in range(3,len(depths)):
		val = val - depths[d-3] + depths[d]
		out.append(val)
	return out

if __name__=='__main__':
	depths = depths_from_file("input.txt")
	print("==================")
	print("Single measurement\n")
	incs = count_increases(depths)
	print(incs)
	print("\n==================")
	print("Sliding Windows\n")
	incs = count_increases(make_windows(depths))
	print(incs)
