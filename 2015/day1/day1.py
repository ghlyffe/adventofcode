#!/usr/bin/python3

def parse_parens(paren_str):
	"""
	>>> parse_parens("(())")
	0

	>>> parse_parens("()()")
	0

	>>> parse_parens("")
	0

	>>> parse_parens("(((")
	3

	>>> parse_parens("(()(()(")
	3

	>>> parse_parens("())")
	-1

	>>> parse_parens("))(")
	-1

	>>> parse_parens(")))")
	-3

	>>> parse_parens(")())())")
	-3
	"""
	floor = 0
	for par in paren_str:
		if par == '(':
			floor += 1
		else:
			floor -= 1
	return floor


def enters_basement(paren_str):
	"""
	>>> enters_basement(")")
	1

	>>> enters_basement("()())")
	5

	>>> enters_basement("(((")
	-1
	"""
	floor = 0
	for idx,par in enumerate(paren_str):
		if par == '(':
			floor += 1
		else:
			floor -= 1
		if floor == -1:
			return idx + 1
	return -1

if __name__=='__main__':
	import doctest
	doctest.testmod()
###################
	print(str([i for i in map(parse_parens,[line for line in open("input.txt","r")])]))
	print(str([i for i in map(enters_basement,[line for line in open("input.txt","r")])]))
