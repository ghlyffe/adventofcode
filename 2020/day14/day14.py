import re

def parse_mask(instr):
    mask = 0
    reset = 0
    toset = 0
    max = 0xFFFFFFFFF
    for i in instr:
        mask <<= 1
        toset <<= 1
        reset <<= 1
        #We want to put a 1 in reset every time it isn't a 0
        if i=='X':
            mask |= 1
            reset |= 1
        elif i=='1':
            toset |= 1
            reset |= 1

    return mask&max,toset&max,reset&max

def parse_mem_mask(instr):
    mask = 0
    reset = 0
    flot = []
    toset = 0
    max = 0xFFFFFFFFF
    for idx,i in enumerate(instr):
        mask <<= 1
        toset <<= 1
        reset <<= 1
        if i=='0':
            mask |= 1
            reset |= 1
        elif i=='1':
            toset |= 1
            reset |= 1
        elif i=='X':
            flot.append(35-idx) #We want to count from 0 on the right, not the left

    return mask&max,toset&max,reset&max,flot

class Mask(object):
    def __init__(self,instr):
        self.__mask,self.__set,self.__reset = parse_mask(instr)

    def apply(self,mem,addr,value):
        out = value & self.__mask
        out |= self.__set
        out &= self.__reset
        mem[addr] = out

class MemMask(object):
    def __init__(self,instr):
        self.__mask,self.__set,self.__reset,self.__flot = parse_mem_mask(instr)

    def apply(self,mem,addr,value): 
        out = addr & self.__mask
        out |= self.__set
        out &= self.__reset

        addrs = self.floating(out)

        for i in addrs:
            mem[i] = value

    def floating(self,val,inidx=0):
        res = []
        if inidx >= len(self.__flot):
            return []

        res.append(val)
        res.extend(self.floating(val,inidx+1))
        setter = 1<<self.__flot[inidx]
        val2 = (val|setter)&0xFFFFFFFFF
        res.append(val2)
        res.extend(self.floating(val2,inidx+1))

        return res


class Pgm(object):
    def __init__(self, ops, masktype=Mask):
        self.__mem = {}
        self.__ops = ops
        self.__mask = None # First op will always set the mask
        self.__masktype = masktype

    def run(self):
        for op in self.__ops:
            if op[0] == 'mask':
                self.__mask = self.__masktype(op[1])
            else:
                self.__mask.apply(self.__mem,op[0],op[1])

    def total(self):
        return sum(self.__mem.values())

def parse_op(line):
    pts = line.split(' = ')
    val = pts[1]
    try:
        val = int(val)
    except: #Plenty of people say this is the most efficient way to do this in python, I need to benchmark it
        pass
    op = pts[0]
    if 'mem' in op:
        s = re.search('(\d+)',op)
        if s:
            op = int(s.group(0))
        else:
            raise Exception("No valid memory address for operation")
    return op,val

def parse_lines(lines,masktype=Mask):
    return Pgm([parse_op(op) for op in lines],masktype)

if __name__=='__main__':
    lines = [line.strip() for line in open("2020/day14/input.txt","r")]
    pgm = parse_lines(lines)
    pgm.run()
    print(pgm.total())
    
    pgm = parse_lines(lines,MemMask)
    pgm.run()
    print(pgm.total())
    