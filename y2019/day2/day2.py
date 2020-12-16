#!/usr/bin/python3

def file_to_code(fname):
	mem = []
	for line in open(fname,"r"):
		mem.extend([int(i) for i in line.split(",")])
	return mem

class Opcode(object):
	def __init__(self, mem, ptr, code, inc):
		"""
		>>> o = Opcode([1001, 2, 4, 1], 0, 1, 4)
		>>> o._Opcode__par_modes
		[0, 1]
		"""
		if mem[ptr]%100 != code:
			raise Exception("Creating Opcode%d for opcode %d"%(code, mem[ptr]))
		self.memory = mem
		self.ptr = ptr
		self.__par_modes = list(reversed([int(i) for i in str(int(mem[ptr]/100))]))
		self.__ptr_inc = inc

	def ptr_inc(self):
		return self.__ptr_inc

	def get_val(self, arg_idx):
		"""
		>>> o = Opcode([1001, 2, 4, 1], 0, 1, 4)
		>>> o.get_val(1)
		4
		>>> o.get_val(2)
		4
		>>> o.get_val(3)
		2
		"""
		idx = arg_idx-1
		if idx >= len(self.__par_modes) or self.__par_modes[idx] == 0:
			return self.memory[self.memory[self.ptr+arg_idx]]
		elif self.__par_modes[idx] == 1:
			return self.memory[self.ptr + arg_idx]

	def set_ptr(self):
		return False,0

	def reads(self):
		raise Exception("Call to base class reads()")

	def writes(self):
		raise Exception("Call to base class writes()")

	def op(self):
		raise Exception("Call to base class op()")

	def params(self):
		raise Exception("Call to base class params()")

	def run(self):
		raise Exception("Call to base class run()")


class Opcode1(Opcode):
	"""
	>>> o = Opcode1([101, 2, 1, 3], 0)
	>>> o.run()
	True
	>>> o.memory
	[101, 2, 1, 4]
	"""
	def __init__(self, mem, ptr):
		super().__init__(mem, ptr, 1, 4)
		self.__first = self.get_val(1)
		self.__second = self.get_val(2)
		self.__res = mem[ptr+3]

	def run(self):
		self.memory[self.__res] = self.__first + self.__second
		return True

	def params(self):
		return {'noun':self.__first, 'verb':self.__second, 'result':self.__res}

	def reads(self):
		return [self.__first, self.__second]

	def writes(self):
		return self.__res

	def op(self):
		return "+"

	def __str__(self):
		return "loc[%d] = %d + %d"%(self.__res,self.__first,self.__second)

class Opcode2(Opcode):
	"""
	>>> o = Opcode2([2, 2, 3, 4, 99], 0)
	>>> o.run()
	True
	>>> o.memory
	[2, 2, 3, 4, 12]
	"""
	def __init__(self, mem, ptr):
		super().__init__(mem, ptr, 2, 4)
		self.__first = self.get_val(1)
		self.__second = self.get_val(2)
		self.__res = mem[ptr+3]

	def run(self):
		self.memory[self.__res] = self.__first * self.__second
		return True

	def params(self):
		return {'noun':self.__first, 'verb':self.__second, 'result':self.__res}

	def reads(self):
		return [self.__first, self.__second]

	def writes(self):
		return self.__res

	def op(self):
		return "*"

	def __str__(self):
		return "loc[%d] = %d * %d"%(self.__res,self.__first,self.__second)

class Opcode99(Opcode):
	"""
	>>> o = Opcode99([99,12,3,4,5], 0)
	>>> o.run()
	False
	"""
	def __init__(self, mem, ptr):
		super().__init__(mem, ptr, 99, 1)

	def run(self):
		return False

	def params(self):
		return {}

	def reads(self):
		return []

	def writes(self):
		return None

	def op(self):
		return "HALT"

	def __str__(self):
		return "HALT"

def default_ops():
	return {1:Opcode1,2:Opcode2,99:Opcode99}

class Interpreter(object):
	def __init__(self, input_code, ops=default_ops()):
		self.__memory = input_code

		self.__ops = ops
		self.__ptr = 0
		self.__running = True
		self.length = len(self.__memory)

	def stepi(self):
		o = None
		if self.__running:
			o = self.next_op()
			self.__running = o.run()
			chk,val = o.set_ptr()
			if chk:
				self.__ptr = val
			else:
				self.__ptr += o.ptr_inc()
		return o

	def run(self):
		while self.__running:
			self.stepi()

	def inspect(self,loc):
		return self.__memory[loc]

	def next_op(self):
		return self.op_at(self.__ptr)

	def op_at(self, ptr):
		return self.__ops[self.__memory[ptr] % 100](self.__memory, ptr)

	def __str__(self):
		strs = []
		for i,v in enumerate(self.__memory):
			if i == self.__ptr:
				strs.append("{:*>4}".format(v))
			else:
				strs.append("{:>4}".format(v))
		return ",".join(strs) + "\n" + "Next:\n\t" + str(self.next_op())

	def poke(self,loc,val):
		self.__memory[loc] = val

	def rebind(self,code,call):
		self.__ops[code] = call

	def as_opcodes(self):
		ops = [self.op_at(0)]
		ptr = ops[-1].ptr_inc()
		while ops[-1].op() != "HALT":
			ops.append(self.op_at(ptr))
			ptr += ops[-1].ptr_inc()
		return ops

class ValueNode(object):
	def __init__(self,val,tag=''):
		self.__val = val
		self.__tag = tag

	def __str__(self):
		return self.__tag + str(self.__val)

class OpNode(object):
	def __init__(self,op,depends):
		self.__op = op
		self.__depends = depends

	def __str__(self):
		return "(" + self.__op.op().join([str(i) for i in self.__depends]) + ")"

class OpcodeTreeBuilder(object):
	def __init__(self, interp):
		self.__interpreter = interp
		self.__codes = interp.as_opcodes()

	def construct_mappings(self):
		for i in self.__codes:
			params = i.params()
			if 'result' in params.keys():
				if params['result'] not in self.__writes_to.keys():
					self.__writes_to[params['result']] = []
				self.__writes_to[params['result']].append(i)
			if 'noun' in params.keys():
				if params['noun'] not in self.__reads_from.keys():
					self.__reads_from[params['noun']] = []
				self.__reads_from[params['noun']].append(i)
			if 'verb' in params.keys():
				if params['verb'] not in self.__reads_from.keys():
					self.__reads_from[params['verb']] = []
				self.__reads_from[params['verb']].append(i)

	def construct_graph(self):
		op = self.__interpreter.op_at(0)
		reads = [ValueNode(self.__interpreter.inspect(i),tag="raw%d_"%(i)) for i in op.reads()]
		writes = op.writes()
		base = OpNode(op,reads)
		ptr = op.ptr_inc()
		last_write = {}
		if writes:
			last_write[writes] = base
		while op.op() != "HALT":
			op = self.__interpreter.op_at(ptr)
			if op.op() == "HALT":
				break
			depends = []
			for i in op.reads():
				if i in last_write.keys():
					depends.append(last_write[i])
				else:
					depends.append(ValueNode(self.__interpreter.inspect(i)))
			base = OpNode(op,depends)
			if op.writes():
				last_write[op.writes()] = base
			ptr += op.ptr_inc()
		return base

if __name__=='__main__':
	import doctest
	doctest.testmod()

#################################################

#	i = Interpreter(file_to_code("day2_input.txt"))
#	i.run()
#	i.inspect(0)
