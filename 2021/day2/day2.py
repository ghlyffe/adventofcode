#!/usr/bin/python

class TurtleSub(object):
	def __init__(self,instrs):
		self.__pos = (0,0) # Horizontal, depth
		self.__instrs = instrs

	def run(self):
		for i in self.__instrs:
			m = self.parse(i)
			self.apply(m)
		return self.__pos

	def parse(self,line):
		pts = line.split(' ')
		mov = [0,0]
		if pts[0] == 'forward':
			mov[0] += int(pts[1])
		elif pts[0] == 'up':
			mov[1] -= int(pts[1])
		elif pts[0] == 'down':
			mov[1] += int(pts[1])
		else:
			pass
		return tuple(mov)

	def apply(self,mov):
		h = self.__pos[0] + mov[0]
		d = self.__pos[1] + mov[1]
		self.__pos = (h,d)
		return self.__pos

class AimedTurtleSub(TurtleSub):
	def __init__(self,lines):
		self.__aim = 0
		super().__init__(lines)

	def apply(self, mov):
		h = mov[0]
		d = self.__aim*mov[0]
		self.__aim += mov[1]
		return super().apply((h,d))

if __name__=='__main__':
	lines = [line for line in open('input.txt','r')]
	ts = TurtleSub(lines)
	p = ts.run()
	print(p[0]*p[1])

	ats = AimedTurtleSub(lines)
	p = ats.run()
	print(p[0]*p[1])
