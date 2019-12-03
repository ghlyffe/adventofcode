#!/usr/bin/python3
class Interpreter(object):
	def __init__(self, fname):
		self.__memory = []
		for line in open(fname,"r"):
			self.__memory.extend([int(i) for i in line.split(",")])

		self.__ops = {1:Opcode1,2:Opcode2,99:Opcode99}
		self.__ptr = 0
		self.__running = True
		self.length = len(self.__memory)

	def stepi(self):
		o = None
		if self.__running:
			o = self.next_op()
			self.__running = o.run()
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
		return self.__ops[self.__memory[ptr]](self.__memory, ptr)

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

class Opcode1(object):
	def __init__(self, mem, ptr):
		if mem[ptr] != 1:
			raise Exception("Creating Opcode1 for opcode %d"%(mem[ptr]))
		self.__memory = mem
		self.__ptr = ptr
		self.__first = mem[ptr+1]
		self.__second = mem[ptr+2]
		self.__res = mem[ptr+3]

	def run(self):
		self.__memory[self.__res] = self.__memory[self.__first] + self.__memory[self.__second]
		return True

	def ptr_inc(self):
		return 4

	def params(self):
		return {'noun':self.__first, 'verb':self.__second, 'result':self.__res}

	def reads(self):
		return [self.__first, self.__second]

	def writes(self):
		return self.__res

	def op(self):
		return "+"

	def __str__(self):
		return "loc[%d] = loc[%d](%d) + loc[%d](%d)"%(self.__res,self.__first,self.__memory[self.__first],self.__second,self.__memory[self.__second])

class Opcode2(object):
	def __init__(self, mem, ptr):
		if mem[ptr] != 2:
			raise Exception("Creating Opcode1 for opcode %d"%(mem[ptr]))
		self.__memory = mem
		self.__ptr = ptr
		self.__first = mem[ptr+1]
		self.__second = mem[ptr+2]
		self.__res = mem[ptr+3]

	def run(self):
		self.__memory[self.__res] = self.__memory[self.__first] * self.__memory[self.__second]
		return True

	def ptr_inc(self):
		return 4

	def params(self):
		return {'noun':self.__first, 'verb':self.__second, 'result':self.__res}

	def reads(self):
		return [self.__first, self.__second]

	def writes(self):
		return self.__res

	def op(self):
		return "*"

	def __str__(self):
		return "loc[%d] = loc[%d](%d) * loc[%d](%d)"%(self.__res,self.__first,self.__memory[self.__first],self.__second,self.__memory[self.__second])

class Opcode99(object):
	def __init__(self, mem, ptr):
		self.__memory = mem

	def run(self):
		return False

	def ptr_inc(self):
		return 1

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
		reads = [ValueNode(self.__interpreter.inspect(i),tag="raw") for i in op.reads()]
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
	i = Interpreter("day2_input.txt")
	o = OpcodeTreeBuilder(i)
	n = o.construct_graph()
	print(n)
