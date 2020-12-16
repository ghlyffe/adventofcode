#!/usr/bin/python3

import day2

def test_input():
	return 42

class Opcode3(day2.Opcode):
	"""
	>>> o = Opcode3([3, 2, 0], 0, test_input)
	>>> o.run()
	True
	>>> o.memory
	[3, 2, 42]
	"""
	def __init__(self, mem, ptr, read=input):
		super().__init__(mem, ptr, 3, 2)
		self.__output = mem[ptr+1]
		self.__read = read

	def run(self):
		self.memory[self.__output] = int(self.__read())
		return True

	def op(self):
		"INPUT"

	def __str__(self):
		return "loc[%d] = INPUT"%(self.__output)

class Opcode4(day2.Opcode):
	"""
	>>> ops = day2.default_ops()
	>>> ops[4] = Opcode4
	>>> i = day2.Interpreter([4, 1, 99],ops)
	>>> i.run()
	1
	>>> i = day2.Interpreter([104, 0, 99], ops)
	>>> i.run()
	0
	"""
	def __init__(self, mem, ptr):
		super().__init__(mem, ptr, 4, 2)
		self.__output = self.get_val(1)

	def run(self):
		print(self.__output)
		return True

	def op(self):
		"PRINT"

	def __str__(self):
		return "PRINT loc[%d]"%(self.__output)

class Opcode5(day2.Opcode):
	"""
	>>> o = Opcode5([5, 0, 3, 4, 99], 0)
	>>> o.run()
	True
	>>> o.set_ptr()
	(True, 4)
	>>> o = Opcode5([105, 0, 3, 4, 99], 0)
	>>> o.run()
	True
	>>> o.set_ptr()
	(False, 0)
	>>> o = Opcode5([1005, 0, 3, 99], 0)
	>>> o.run()
	True
	>>> o.set_ptr()
	(True, 3)
	"""
	def __init__(self, mem, ptr):
		super().__init__(mem, ptr, 5, 3)
		self.__test = self.get_val(1)
		self.__loc = self.get_val(2)
		self.__set = False

	def run(self):
		if self.__test != 0:
			self.ptr = self.__loc
			self.__set = True
		return True

	def set_ptr(self):
		return self.__set,self.ptr

	def op(self):
		"IF_TRUE"

	def __str__(self):
		return "IF_TRUE %d => %d"%(self.__test,self.__loc)

class Opcode6(day2.Opcode):
	"""
	>>> o = Opcode6([6, 0, 3, 4, 99], 0)
	>>> o.run()
	True
	>>> o.set_ptr()
	(False, 0)
	>>> o = Opcode6([106, 0, 3, 4, 99], 0)
	>>> o.run()
	True
	>>> o.set_ptr()
	(True, 4)
	>>> o = Opcode6([1006, 0, 3, 99], 0)
	>>> o.run()
	True
	>>> o.set_ptr()
	(False, 0)
	"""
	def __init__(self, mem, ptr):
		super().__init__(mem, ptr, 6, 3)
		self.__test = self.get_val(1)
		self.__loc = self.get_val(2)
		self.__set = False

	def run(self):
		if self.__test == 0:
			self.ptr = self.__loc
			self.__set = True
		return True

	def set_ptr(self):
		return self.__set,self.ptr

	def op(self):
		"IF_FALSE"

	def __str__(self):
		return "IF_FALSE %d => %d"%(self.__test,self.__loc)

class Opcode7(day2.Opcode):
	"""
	>>> o = Opcode7([7,2,1,3], 0)
	>>> o.run()
	True
	>>> o.memory
	[7, 2, 1, 1]
	>>> o = Opcode7([1107,2,1,3], 0)
	>>> o.run()
	True
	>>> o.memory
	[1107, 2, 1, 0]
	"""
	def __init__(self, mem, ptr):
		super().__init__(mem, ptr, 7, 4)
		self.__first = self.get_val(1)
		self.__second = self.get_val(2)
		self.__res = mem[ptr+3]

	def run(self):
		if self.__first < self.__second:
			self.memory[self.__res] = 1
		else:
			self.memory[self.__res] = 0
		return True

	def op(self):
		"<"

	def __str__(self):
		return ""

class Opcode8(day2.Opcode):
	"""
	>>> o = Opcode8([108,2,2,3], 0)
	>>> o.run()
	True
	>>> o.memory
	[108, 2, 2, 1]
	"""
	def __init__(self, mem, ptr):
		super().__init__(mem, ptr, 8, 4)
		self.__first = self.get_val(1)
		self.__second = self.get_val(2)
		self.__res = mem[ptr+3]

	def run(self):
		if self.__first == self.__second:
			self.memory[self.__res] = 1
		else:
			self.memory[self.__res] = 0
		return True

	def op(self):
		"=="

	def __str__(self):
		return ""

def day5_ops():
	return {3: Opcode3, 4: Opcode4, 5: Opcode5, 6: Opcode6, 7: Opcode7, 8: Opcode8}

if __name__=='__main__':
	import doctest
	doctest.testmod()

##########################################
	print( "END TEST")
	print("BEGIN OPERATION")
	ops = day2.default_ops()
	ops.update(day5_ops())

	i = day2.Interpreter(day2.file_to_code("input.txt"), ops)
	i.run()
