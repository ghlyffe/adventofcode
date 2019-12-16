#!/usr/bin/python3
import Opcode

class Interpreter(object):
	def __init__(self,tape,ops={},inputs=[]):
		self.__ptr = 0
		self.__memory = tape
		self.__inputs = inputs
		self.__outputs = []
		self.__ops = ops
		self.__halted = False
		self.__rel_base = 0

	def queue_input(self,val):
		replacables = self.__inputs.count(None)
		if replacables:
			first_empty = self.__inputs.index(None)
			self.__inputs[first_empty] = val
		else:
			self.__inputs.append(val)

	def queue_output(self,val):
		self.__outputs.append(val)

	def pop_input(self):
		if len(self.__inputs) == 0:
			return None
		val = self.__inputs[0]
		self.__inputs = self.__inputs[1:]
		return val

	def peek_input(self):
		if len(self.__inputs) > 0:
			return self.__inputs[0]
		return None

	def pop_output(self):
		if len(self.__outputs) == 0:
			return None
		val = self.__outputs[0]
		self.__outputs = self.__outputs[1:]
		return val

	def reset_ptr(self, loc=0, relative=False):
		if not relative:
			self.__ptr = loc
		else:
			self.__ptr += loc

	def halt(self):
		self.__halted = True

	def op_at(self,loc):
		return self.__ops[self.__memory[loc]%100](self)

	def stepi(self):
		if not self.__halted:
			op = self.op_at(self.__ptr)
			cont = op.run()
			self.__ptr += op.ptr_inc()
			return cont
		return False

	def run(self):
		self.__running = True
		while self.stepi():
			pass

	def halted(self):
		return self.__halted

	def __getitem__(self,key):
		while key >= len(self.__memory):
			self.__memory.append(0)
		return self.__memory[key]

	def __setitem__(self,key,val):
		while key >= len(self.__memory):
			self.__memory.append(0)
		self.__memory[key] = val

	def __str__(self):
		out = [str(i) for i in self.__memory]
		out[self.__ptr] = ">>>" + out[self.__ptr]
		return str(out)

	def memory(self):
		import copy
		return copy.copy(self.__memory)

if __name__=='__main__':
	import copy
	tape = [int(i) for i in ','.join([line.strip() for line in open("boost_tape.txt","r")]).split(',')]
	i = Interpreter(copy.copy(tape), Opcode.default_opcodes(), [1])
	i.run()
	print(i.pop_output())
	i = Interpreter(copy.copy(tape), Opcode.default_opcodes(), [2])
	i.run()
	print(i.pop_output())
