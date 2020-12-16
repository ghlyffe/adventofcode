#!/usr/bin/python3

from itertools import zip_longest

def split_to_layers(value,width,height):
	"""
	>>> split_to_layers("123456789012",3,2)
	[[['1', '2', '3'], ['4', '5', '6']], [['7', '8', '9'], ['0', '1', '2']]]
	>>> split_to_layers("0222112222120000",2,2)
	[[['0', '2'], ['2', '2']], [['1', '1'], ['2', '2']], [['2', '2'], ['1', '2']], [['0', '0'], ['0', '0']]]
	"""
	return [[list(k) for k in j] for j in [zip_longest(*([iter(i)]*width)) for i in zip_longest(*([iter(value)]*(width*height)))]]

def layer_calc(image, identifier='0', count_a='1', count_b='2'):
	"""
	>>> layer_calc([[['1','2','3'],['4','5','6']],[['7','8','9'],['0','1','2']]])
	1
	>>> layer_calc([[['1','2','3'],['4','5','6']],[['1','1','9'],['0','1','2']]])
	1
	>>> layer_calc([[['1','2','3'],['4','5','6']],[['1','2','9'],['0','1','2']]])
	1
	>>> layer_calc([[['1','2','3'],['4','0','6']],[['1','2','9'],['6','1','2']]])
	4
	>>> layer_calc([[['1','2','3'],['4','5','6']],[['2','2','9'],['0','2','2']]])
	1
	>>> layer_calc([[['1','2','0'],['4','0','6']],[['2','2','9'],['0','2','2']]])
	0
	>>> layer_calc([[['1','0','0'],['1','2','1']],[['2','2','9'],['0','2','2']]])
	0
	"""
	best = None
	out = 0

	for i in image:
		c = sum(map(lambda x: 0 if identifier not in x else x.count(identifier), i))
		if best == None or c < best:
			best = c
			out = sum(map(lambda x: 0 if count_a not in x else x.count(count_a), i)) * sum(map(lambda x: 0 if count_b not in x else x.count(count_b), i))

	return out

def collapse_layers(layers, width, height):
	"""
	>>> collapse_layers(split_to_layers("0222112222120000",2,2),2,2)
	[['0', '1'], ['1', '0']]
	"""
	output = [[None for w in range(width)] for h in range(height)]
	for layer in layers:
		for y in range(height):
			for x in range(width):
				if output[y][x] == None:
					if layer[y][x] != "2":
						output[y][x] = layer[y][x]
	return output

def checksum(value,width,height):
	"""
	>>> checksum("123456789012",3,2)
	1
	>>> checksum("123456119012",3,2)
	1
	>>> checksum("123456129012",3,2)
	1
	>>> checksum("123406129612",3,2)
	4
	>>> checksum("123456229022",3,2)
	1
	>>> checksum("120406229022",3,2)
	0
	>>> checksum("100121229022",3,2)
	0
	"""
	layers = [(i.count('0'),i.count('1')*i.count('2')) for i in zip_longest(*([iter(value)]*(width*height)))]
	return sorted(layers)[0][1]

if __name__=='__main__':
	import doctest
	doctest.testmod()

######################

	for line in open("input.txt","r"):
		print(checksum(line.strip(),25,6))
	images = [split_to_layers(line.strip(),25,6) for line in open("input.txt","r")]

	for i in map(lambda x: collapse_layers(x,25,6),images):
		for col in i:
			for row in col:
				if row != '1':
					print(' ',end='')
				else:
					print(row, end='')
			print('')
