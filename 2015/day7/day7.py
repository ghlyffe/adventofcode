import re
import operator

class Lazy(object):
    def __init__(self,id,circuit):
        self.__id = id
        self.__circuit = circuit

    def get_output(self):
        return self.__circuit.get_output_for(self.__id)

    def reset(self):
        pass


class Wire(object):
    def __init__(self,id, inpt):
        self.__id = id
        self.__signal = None
        self.__input = inpt

    def get_output(self):
        if self.__signal is None:
            if self.__input is not None:
                self.__signal = self.__input.get_output()
        return self.__signal

    def reset(self):
        self.__signal = None

class Signal(object):
    def __init__(self, val):
        self.__val = val

    def get_output(self):
        return self.__val

    def reset(self):
        pass

class Gate(object):
    def __init__(self, id, inputs, op):
        self.__inputs = inputs
        self.__id = id
        self.__op = op

    def get_output(self):
        return self.__op([i.get_output() for i in self.__inputs])

    def reset(self):
        pass

class Circuit(object):
    def __init__(self):
        self.__objs = {} # map id to object for reference

    def __parse_input(self,inp):
        if re.search("\d",inp) is not None:
            return Signal(int(inp))
        else:
            return Lazy(inp,self)

    def __and(self,inps):
        return inps[0] & inps[1]

    def __or(self,inps):
        return inps[0] | inps[1]

    def __lshift(self,inps):
        return (inps[0] << inps[1])&0xFFFF

    def __rshift(self,inps):
        return inps[0] >> inps[1]

    def __not(self, inps):
        return (~inps[0])&0xFFFF

    def add_wire(self,id,inpt):
        if id in self.__objs:
            return

        if type(inpt) == int:
            self.__objs[id] = Wire(id, Signal(inpt))
        else:
            self.__objs[id] = Wire(id, inpt)

    def add_gate(self, id):
        if id in self.__objs:
            return

        if "AND" in id:
            lcon,rcon = id.split(' AND ')
            lcon = self.__parse_input(lcon)
            rcon = self.__parse_input(rcon)
            self.__objs[id] = Gate(id,[lcon,rcon],self.__and)
        elif "OR" in id:
            lcon,rcon = id.split(' OR ')
            lcon = self.__parse_input(lcon)
            rcon = self.__parse_input(rcon)
            self.__objs[id] = Gate(id,[lcon,rcon],self.__or)
        elif "LSHIFT" in id:
            lcon,rcon = id.split(' LSHIFT ')
            lcon = self.__parse_input(lcon)
            rcon = self.__parse_input(rcon)
            self.__objs[id] = Gate(id,[lcon,rcon],self.__lshift)
        elif "RSHIFT" in id:
            lcon,rcon = id.split(' RSHIFT ')
            lcon = self.__parse_input(lcon)
            rcon = self.__parse_input(rcon)
            self.__objs[id] = Gate(id,[lcon,rcon],self.__rshift)
        elif "NOT" in id:
            inp = id[4:]
            inp = self.__parse_input(inp)
            self.__objs[id] = Gate(id,[inp],self.__not)
        else:
            raise Exception("Not a valid Gate")

    def parse_line(self, line):
        src,dst = line.split(' -> ')
        ops = ['AND','OR','NOT','LSHIFT','RSHIFT']
        if any(map(lambda x: x in src,ops)):
            self.add_gate(src)
            self.add_wire(dst,Lazy(src,self))
        elif re.search("\d",src):
            self.add_wire(dst,int(src))
        else:
            self.add_wire(dst,Lazy(src,self))

    def parse_file(self,fname):
        for line in open(fname,"r"):
            self.parse_line(line.strip())

    def get_output_for(self, id):
        return self.__objs[id].get_output()

    def override_wire(self,id,inp):
        del self.__objs[id]
        for i in self.__objs:
            self.__objs[i].reset()
        self.add_wire(id,inp)

if __name__ == '__main__':
    c = Circuit()
    c.parse_file("2015/day7/input.txt")
    sig_a = c.get_output_for("a")
    print(sig_a)
    c.override_wire("b",sig_a)
    sig_a = c.get_output_for("a")
    print(sig_a)