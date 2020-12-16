#!/usr/bin/python

from itertools import combinations

def get_face_dimensions(package_def):
	"""
	>>> get_face_dimensions("1x2x3")
	[(1, 2), (1, 3), (2, 3)]

	>>> get_face_dimensions("1x1x10")
	[(1, 1), (1, 10), (1, 10)]

	>>> get_face_dimensions("1x2")
	[(1, 2)]
	"""
	return list(combinations([int(i) for i in package_def.split("x")],2))

def surface_area(dim_list):
	"""
	>>> surface_area([(1,2),(1,3),(2,3)])
	24

	>>> surface_area([(2,3),(2,4),(3,4)])
	58

	>>> surface_area([(1,1),(1,10),(1,10)])
	43
	"""
	side_surfaces = map(lambda (x,y): x*y, dim_list)
	return 2*sum(side_surfaces) + min(side_surfaces)

def perimeters(dim_list):
	"""
	>>> perimeters([(1,2),(1,3),(2,3)])
	[6, 8, 10]

	>>> perimeters([(2,3),(2,4),(3,4)])
	[10, 12, 14]

	>>> perimeters([(1,1),(1,10),(1,10)])
	[4, 22, 22]
	"""
	return [2*sum(i) for i in dim_list]

def volume(dims):
	"""
	>>> volume("1x2x3")
	6

	>>> volume("2x3x4")
	24

	>>> volume("1x1x10")
	10
	"""
	vals = [int(i) for i in dims.split("x")]
	prod = 1
	for i in vals:
		prod *= i
	return prod

def ribbon(dims):
	"""
	>>> ribbon("1x2x3")
	12

	>>> ribbon("2x3x4")
	34

	>>> ribbon("1x1x10")
	14
	"""
	return volume(dims) + min(perimeters(get_face_dimensions(dims)))

if __name__=='__main__':
	import doctest
	doctest.testmod()

##############################

	print(sum([surface_area(j) for j in [get_face_dimensions(i) for i in [line for line in open("input.txt","r")]]]))
	print(sum([ribbon(line) for line in open("input.txt","r")]))
