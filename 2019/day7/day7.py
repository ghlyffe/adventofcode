#!/usr/bin/python3

import FeedbackMachine
import Opcode

def file_to_code(fname):
	mem = []
	for line in open(fname,"r"):
		mem.extend([int(i) for i in line.split(",")])
	return mem

def run(input_seq):
	tape = file_to_code("input.txt")
	ops = Opcode.default_opcodes()
	ops[3] = FeedbackMachine.HaltingInput
	fm = FeedbackMachine.FeedbackMachine(tape,ops)
	return fm.run(input_seq)

if __name__ == '__main__':
	import itertools
	perms = itertools.permutations([5,6,7,8,9],5)
	best = [0,[]]
	for p in perms:
		val = run(p)
		if val > best[0]:
			best = [val,p]
	print(best)
