#!/usr/bin/python3

import intcode_except as ie

class Opcode(object):
	def __init__(self,interpreter):
		self.interpreter = interpreter
		self.__ptr = self.interpreter._Interpreter__ptr
		self.__memory = self.interpreter._Interpreter__memory
		self.__parameter_modes = None
		self.__parameter_modes = self.get_parameter_modes()

	def get_parameter_modes(self):
		if self.__parameter_modes:
			return self.__parameter_modes
		par_modes = [int(i) for i in reversed([j for j in str(self.__memory[self.__ptr])[:-2]])]
		return {idx:(mode,self.__memory[self.__ptr+idx+1]) for idx,mode in enumerate(par_modes)}

	def __getitem__(self,key):
		mode = 0
		val = self.__memory[self.__ptr+key+1]
		if key in self.__parameter_modes:
			mode,val = self.__parameter_modes[key]
		if mode == 0: #Positional
			while val >= len(self.__memory):
				self.__memory.append(0)
			return self.__memory[val]
		elif mode == 1: #Immediate
			return val
		elif mode == 2: #Relative
			while (val+self.interpreter._Interpreter__rel_base) >= len(self.__memory):
				self.__memory.append(0)
			return self.__memory[self.interpreter._Interpreter__rel_base + val]
		else:
			raise Exception("Invalid Parameter Mode %d"%mode)

	def __setitem__(self,key,value):
		mode = 0
		val = self.__memory[self.__ptr+key+1]
		if key in self.__parameter_modes:
			mode,val = self.__parameter_modes[key]
		if mode == 0: #Positional
			while val >= len(self.__memory):
				self.__memory.append(0)
			self.__memory[val] = value
		elif mode == 1: #Immediate
			raise Exception("Trying to use immediate mode for assignment")
		elif mode == 2: #Relative
			while (val+self.interpreter._Interpreter__rel_base) >= len(self.__memory):
				self.__memory.append(0)
			self.__memory[self.interpreter._Interpreter__rel_base + val] = value
		else:
			raise Exception("Invalid Parameter Mode %d"%mode)


	def validate(self):
		self.__memory[self.__ptr] % 100 == self.opcode()

	def opcode(self):
		raise ie.NotImplementedException("Opcode.opcode")

	def run(self):
		raise ie.NotImplementedException("Opcode.run")

	def ptr_inc(self):
		raise ie.NotImplementedException("Opcode.ptr_inc")

class Addition(Opcode):
	def opcode(self):
		return 1

	def run(self):
		self[2] = self[0] + self[1]
		return True

	def ptr_inc(self):
		return 4

class Multiplication(Opcode):
	def opcode(self):
		return 2

	def run(self):
		self[2] = self[0] * self[1]
		return True

	def ptr_inc(self):
		return 4

class Halt(Opcode):
	def opcode(self):
		return 99

	def run(self):
		self.interpreter.halt()
		return False

	def ptr_inc(self):
		return 1

class Input(Opcode):
	def opcode(self):
		return 3

	def run(self):
		self[0] = self.interpreter.pop_input()
		return True

	def ptr_inc(self):
		return 2

class UserInput(Input):
	def run(self):
		self.interpreter.queue_input(int(input()))
		return super().run()

class Output(Opcode):
	def opcode(self):
		return 4

	def run(self):
		self.interpreter.queue_output(self[0])
		return True

	def ptr_inc(self):
		return 2

class ScreenPrint(Output):
	def run(self):
		super().run()
		return True

class JumpIfTrue(Opcode):
	def opcode(self):
		return 5

	def run(self):
		if(self[0] != 0):
			self.interpreter.reset_ptr(self[1])
			self.__ptr_inc = 0
		else:
			self.__ptr_inc = 3
		return True

	def ptr_inc(self):
		return self.__ptr_inc

class JumpIfFalse(Opcode):
	def opcode(self):
		return 6

	def run(self):
		if(self[0] == 0):
			self.interpreter.reset_ptr(self[1])
			self.__ptr_inc = 0
		else:
			self.__ptr_inc = 3
		return True

	def ptr_inc(self):
		return self.__ptr_inc

class LessThan(Opcode):
	def opcode(self):
		return 7

	def run(self):
		self[2] = self[0] < self[1]
		return True

	def ptr_inc(self):
		return 4

class Equal(Opcode):
	def opcode(self):
		return 8

	def run(self):
		self[2] = self[0]==self[1]
		return True

	def ptr_inc(self):
		return 4

class RelativeBaseOffset(Opcode):
	def opcode(self):
		return 9

	def run(self):
		self.interpreter._Interpreter__rel_base += self[0]
		return True

	def ptr_inc(self):
		return 2

class OutputFeedback(Output):
	def run(self):
		self.interpreter.queue_input(self[0])
		return True

def default_opcodes():
		return {1:Addition,2:Multiplication,3:Input,4:Output,5:JumpIfTrue,6:JumpIfFalse,7:LessThan,8:Equal,9:RelativeBaseOffset,99:Halt}

