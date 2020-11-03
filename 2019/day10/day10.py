#!/usr/bin/python3

import itertools
import copy

def transpose(lst,pad=False):
	if pad:
		return [list(i) for i in itertools.zip_longest(*lst)]
	else:
		return [list(i) for i in zip(*lst)]

def file_to_map(fname):
	return [[i for i in line.strip()] for line in open(fname,"r")]

def map_to_points(smap):
	width = len(smap)
	height = len(smap[0])

	out = []

	for x in range(width):
		for y in range(height):
			if smap[x][y] != '#':
				continue
			out.append((x,y))
	return sorted(out)

def make_unit_vector(deltas):
	import math
	gcd = math.gcd(*deltas)
	return [int(i/gcd) for i in deltas]

def mask_from_pair(ast_from, ast_to, smap):
	grad_x,grad_y = (ast_to[0]-ast_from[0],ast_to[1]-ast_from[1])
	bounds = (len(smap),len(smap[0]))
	grad_x,grad_y = make_unit_vector((grad_x,grad_y))
	cur_x = ast_to[0]+grad_x
	cur_y = ast_to[1]+grad_y
	while ( (cur_x >= 0) and (cur_x < bounds[0]) ) and ( (cur_y >= 0) and (cur_y < bounds[1]) ):
		smap[cur_x][cur_y] = "X"
		cur_x += grad_x
		cur_y += grad_y
	return smap

def count_asteroids(smap):
	return [i for i in itertools.chain.from_iterable(smap)].count('#')

def seen_by_asteroid(asts,idx,smap):
	mask_map = copy.deepcopy(smap)
	ast = asts[idx]
	mask_map[ast[0]][ast[1]] = 'O'
	for idx_inner in range(len(asts)):
		if idx == idx_inner:
			continue
		mask_map = mask_from_pair(ast,asts[idx_inner],mask_map)
	mask_map[ast[0]][ast[1]] = 'O'
	return count_asteroids(mask_map)

def map_to_counts(smap):
	asts = map_to_points(smap)
	counts = {}
	for idx in range(len(asts)):
		counts[asts[idx]] = seen_by_asteroid(asts,idx,smap)
	return counts

def best_location(smap):
	counts = map_to_counts(smap)
	best = 0
	best_key = None
	for k in counts:
		if counts[k] > best:
			best = counts[k]
			best_key = k
	return best_key,best

# If we arrange our points such that we have a list of lists, such that:
## Each list contains asteroids at a given angle from the station
## Each list is sorted nearest-furthest from the station
## Lists are sorted from 0-359 degrees
# Then:
# transpose(listolists) would transform to [[first asteroid at each angle],[second asteroid at each angle]...]
# Need this transpose to add Nones as appropriate
#
# Steps:
## map_to_points
## Remove monitoring station
## Partition by angle
## Sort lists by angle
## For each list, sort by distance
## transpose(,True)
## while count < 200 count += len([i for i in lst if i])
## Count back to find 200th asteroid vaporised

def find_nth_asteroid(vapo_list,n=200):
	"""
	Find the nth element of a list-of-lists, not counting None
	But apparently a really weird way?
	This is tested and seems to work, but maybe flatten handles None already
	"""
	return [i for l in vapo_list for i in l if i is not None][n-1]

def calc_angle(first, second):
	import math
	dx = float(first[1] - second[1]) # Also bear in mind that this is addressed as [row,column] which is equivalent to [y,x], NOT [x,y]
	dy = float(first[0] - second[0])
	adx = abs(dx)
	ady = abs(dy)
	hyp = math.sqrt(math.pow(dx,2)+math.pow(dy,2))
	angle = 0
	if(dx==0): # Handle the "special" cases where our equation would divide by zero, but we know the answer (e.g., "directly north" is angle 0)
		if(dy < 0):
			angle = 0
		else:
			angle = math.pi
	elif(dy==0):
		if(dx < 0):
			angle = (math.pi/2)*3
		else:
			angle = math.pi/2
	# For everything else, we use triangles
	# Note that we alternate opposite and adjacent based on which axis we're computing from
	elif (dx > 0) and (dy < 0):	# Top right quadrant: nearest "easy" answer is 0, add on angle from the zero line (i.e., just the angle)
		angle = math.asin(adx/hyp)
	elif (dx > 0) and (dy > 0): # Bottom right quadrant: nearest "easy" answer is pi/2, so we calculate the angle-from-0 as pi/2 + angle further around from the pi/2 line (positive x-axis)
		angle = (math.pi/2) + math.acos(adx/hyp)
	elif (dx < 0) and (dy > 0): # Bottom left quadrant: As above, but now from pi
		angle = math.pi + math.asin(adx/hyp)
	elif (dx < 0) and (dy < 0): # And finally, the top left quadrant
		angle = (3*(math.pi/2)) + math.acos(adx / hyp)
	else:
		assert(False) #How did we get here?
	return round(angle,5)

def partition_by_angle(asts, base): # We're going to do a lot of work with triangles here.
	import math
	outs = {}
	for ast in asts: # Find the angle from base to every asteroid in the grid; we assume base has been removed already, otherwise it should be the first hit
		angle = calc_angle(ast, base)

		if angle not in outs:
			outs[angle] = []
		outs[angle].append(ast)

	for angle in outs:
		outs[angle].sort(key=lambda x: math.sqrt(math.pow((x[0]-base[0]),2)+math.pow((x[1]-base[1]),2)))

	outl = []
	for angle in sorted(outs.keys()):
		outl.append(outs[angle])
	return outl

def nth_asteroid_vaporised(smap, base_loc, n=200):
	asts = map_to_points(smap)
	asts.remove(base_loc)

	parts = partition_by_angle(asts,base_loc)
	parts = transpose(parts,True)
	return find_nth_asteroid(parts,n)

if __name__=='__main__':
	smap = file_to_map("input.txt")
	loc,seen=best_location(copy.deepcopy(smap))
	print("(%d,%d):%d"%(loc[1],loc[0],seen)) #Part 1

	nth  = nth_asteroid_vaporised(smap,loc)
	#1912 is too high - add tests
	#1007 is too low
	print(nth[1]*100 + nth[0])