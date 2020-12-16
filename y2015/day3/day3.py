#!/usr/bin/python3

import itertools

def deliver(insts):
	"""
	>>> deliver(">")
	{(0, 0): 1, (1, 0): 1}

	>>> deliver("^>v<")
	{(0, 0): 2, (0, 1): 1, (1, 1): 1, (1, 0): 1}

	>>> deliver("^V^V^V^V^V")
	{(0, 0): 6, (0, 1): 5}
	"""
	deliveries = {(0,0):1}
	loc = [0,0]
	for inst in insts:
		if inst == "^":
			loc[1] += 1
		elif inst == ">":
			loc[0] += 1
		elif inst == "<":
			loc[0] -= 1
		elif inst in ("v","V"):
			loc[1] -= 1
		tpl = tuple(loc)
		if tpl not in deliveries.keys():
			deliveries[tpl] = 0
		deliveries[tpl] += 1
	return deliveries

class Agent(object):
	"""
	>>> a = Agent()
	>>> a.deliver_one("^")
	>>> a.deliveries()
	{(0, 0): 1, (0, 1): 1}

	>>> a.deliver_all(">^<<V")
	>>> a.deliveries()
	{(0, 0): 1, (0, 1): 1, (1, 1): 1, (1, 2): 1, (0, 2): 1, (-1, 2): 1, (-1, 1): 1}
	"""
	def __init__(self):
		self.__loc = [0,0]
		self.__deliveries = {(0,0): 1}

	def deliver_one(self,inst):
		if inst == "^":
			self.__loc[1] += 1
		elif inst == ">":
			self.__loc[0] += 1
		elif inst == "<":
			self.__loc[0] -= 1
		elif inst in ("v","V"):
			self.__loc[1] -= 1
		tpl = tuple(self.__loc)
		if tpl not in self.__deliveries.keys():
			self.__deliveries[tpl] = 0
		self.__deliveries[tpl] += 1

	def deliver_all(self, insts):
		[self.deliver_one(i) for i in insts]

	def deliveries(self):
		return self.__deliveries

def split_instructions(insts,splits=2):
	"""
	>>> split_instructions("^V^V^V^V^V")
	['^^^^^', 'VVVVV']

	>>> split_instructions("^V^")
	['^^', 'V']

	>>> split_instructions("^")
	['^', '']
	"""
	return [''.join(i) for i in list(zip(*list(itertools.zip_longest(*([iter(insts)]*splits), fillvalue=''))))]

def deliver_multi(insts,agent_count=2):
	"""
	>>> deliver_multi("^V^V")
	[[(0, 0), (0, 1), (0, 2)], [(0, 0), (0, -1), (0, -2)]]
	"""
	agents = list(zip([Agent() for i in range(agent_count)],split_instructions(insts, agent_count)))
	for i in agents:
		i[0].deliver_all(i[1])
	return [list(i[0].deliveries().keys()) for i in agents]

if __name__=='__main__':
	import doctest
	doctest.testmod()

########################
	print([len(i.keys()) for i in [deliver(line) for line in open("input.txt","r")]])
	for line in open("input.txt","r"):
		result = []
		for i in deliver_multi(line):
			result.extend(i)
		print(len(set(result)))
