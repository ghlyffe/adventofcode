class Operation(object):
    def __init__(self,val):
        self.__hits = 0
        self.val = val

    def run(self):
        if self.__hits == 1:
            return False,0,0
        self.__hits += 1
        return True,0,1

    def reset(self):
        self.__hits = 0

class Nop(Operation):
    def __init__(self, val):
        super().__init__(val)

class Jmp(Operation):
    def __init__(self, val):
        super().__init__(val)

    def run(self):
        ret = super().run()
        return ret[0],ret[1],self.val

class Acc(Operation):
    def __init__(self, val):
        super().__init__(val)
    
    def run(self):
        ret = super().run()
        return ret[0],self.val,ret[2]

class Interpreter(object):
    def __init__(self,pgm):
        self.__program = pgm
        self.__accumulator = 0
        self.__pc = 0
        self.__history = []

    def run(self):
        for i in self.__program:
            i.reset()
        self.__pc = 0
        self.__accumulator = 0 
        running,acc,pc = self.__program[self.__pc].run()
        self.__history = [self.__pc]
        while running and self.__pc < len(self.__program):
            self.__accumulator += acc
            self.__pc += pc
            self.__history.append(self.__pc)
            if self.__pc >= len(self.__program):
                break
            running,acc,pc = self.__program[self.__pc].run()

        return self.__accumulator

    def fix_self(self):
        import copy
        backup = copy.copy(self.__program)
        nop_locs = [i for i,v in enumerate(self.__program) if type(v) == Nop]
        for i in nop_locs:
            self.__program[i] = Jmp(self.__program[i].val)
            acc = self.run()
            if self.__pc >= (len(self.__program)):
                return acc # it's fixed, and we just ran it, no need to do it again
            self.__program = copy.copy(backup)

        jmp_locs = [i for i,v in enumerate(self.__program) if type(v) == Jmp]
        for i in jmp_locs:
            self.__program[i] = Nop(self.__program[i].val)
            acc = self.run()
            if self.__pc >= (len(self.__program)):
                return acc # it's fixed, and we just ran it, no need to do it again
            self.__program = copy.copy(backup)
        

ops = {"nop":Nop,"jmp":Jmp,"acc":Acc}

def parse_lines(lines):
    pgm = []
    for line in lines:
        op,val = line.strip().split(' ')
        val = int(val)
        pgm.append(ops[op](val))
    return Interpreter(pgm)

def parse_file(fname):
    return parse_lines([line for line in open(fname,"r")])

if __name__=='__main__':
    interpreter = parse_file("y2020/day8/input.txt")
    print(interpreter.run())
    print(interpreter.fix_self())