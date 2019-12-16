#!/usr/bin/python3

from Interpreter import Interpreter
from Opcode import *

class FeedbackOpcode(Output):
	def __init__(self, interpreter, out_list):
		super().__init__(interpreter)
		self.__feedback = out_list

	def run(self):
		self.__feedback.append(self[0])
		return True

class FeedbackAndFork(FeedbackOpcode):
	def run(self):
		self.interpreter.queue_output(self[0])
		return super().run()

class HaltingInput(Input):
	def __init__(self, interpreter):
		super().__init__(interpreter)
		self.__ptr_inc = 0

	def run(self):
		if self.interpreter.peek_input() != None:
			self.__ptr_inc = 2
			return super().run()
		self.__ptr_inc = 0
		return False

	def ptr_inc(self):
		return self.__ptr_inc

class FeedbackOutputFactory(object):
	def __init__(self, f_type=FeedbackOpcode):
		self.__outerpreter = None
		self.__type = f_type

	def set_outerpreter(self, outerpreter):
		self.__outerpreter = outerpreter

	def construct(self, interpreter):
		return self.__type(interpreter, self.__outerpreter._Interpreter__inputs)

class FeedbackMachine(object):
	def __init__(self,tape,ops,nodes=5):
		from copy import copy
		self.__tape = tape
		self.__ops = ops
		self.__factories = []
		self.__nodes = []
		for i in range(nodes-1):
			ops = copy(self.__ops)
			self.__factories.append(FeedbackOutputFactory())
			ops[4] = self.__factories[-1].construct
			self.__nodes.append(Interpreter(copy(self.__tape), copy(ops), []))
		ops = copy(self.__ops)
		self.__factories.append(FeedbackOutputFactory(FeedbackAndFork))
		ops[4] = self.__factories[-1].construct
		self.__nodes.append(Interpreter(copy(self.__tape), copy(ops), []))
		for i,f in enumerate(self.__factories):
			f.set_outerpreter(self.__nodes[(i+1)%len(self.__nodes)])

	def set_inputs(self, input_seq):
		for i in range(len(self.__nodes)):
			self.__nodes[i].queue_input(input_seq[i])

	def run(self, input_seq, initial=0):
		self.set_inputs(input_seq)
		self.__nodes[0].queue_input(initial)
		val = 0
		while any([not i.halted() for i in self.__nodes]):
			self.run_one()
			val = self.__nodes[-1].pop_output()
		return val

	def run_one(self):
		for j in range(len(self.__nodes)):
			self.__nodes[j].run()
