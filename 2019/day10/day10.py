#!/usr/bin/python3

import itertools
import copy

def transpose(lst):
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

if __name__=='__main__':
	loc,seen=best_location(file_to_map("input.txt"))
	print("(%d,%d):%d"%(loc[1],loc[0],seen))
