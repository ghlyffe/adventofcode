class Ferry(object):
    def __init__(self,instrs,mode=0):
        self.__loc = [0,0,90]
        self.__waypoint = [1,10]
        self.__instrs = instrs
        self.__idx = 0
        self.__mode = mode

    def step(self):
        if self.__idx >= len(self.__instrs):
            return False

        if self.__mode == 1:
            self.__step_waypoint()
        else:
            self.__step_ferry()

        self.__idx += 1
        return True

    def __step_waypoint(self):
        s = self.__instrs[self.__idx]
        val= int(s[1:])
        i = s[0]

        if i == 'N':
            self.__waypoint[0] += val
        elif i == 'S':
            self.__waypoint[0] -= val
        elif i == 'E':
            self.__waypoint[1] += val
        elif i == 'W':
            self.__waypoint[1] -= val
        elif i == 'L':
            if val == 90:
                self.__waypoint = [self.__waypoint[1], 0-self.__waypoint[0]]
            elif val == 180:
                self.__waypoint = [0 - self.__waypoint[0], 0-self.__waypoint[1]]
            elif val == 270:
                self.__waypoint = [0 - self.__waypoint[1], self.__waypoint[0]]
        elif i == 'R':
            if val == 90:
                self.__waypoint = [0 - self.__waypoint[1], self.__waypoint[0]]
            elif val == 180:
                self.__waypoint = [0 - self.__waypoint[0], 0-self.__waypoint[1]]
            if val == 270:
                self.__waypoint = [self.__waypoint[1], 0-self.__waypoint[0]]
            
        elif i == 'F':
            self.__loc[0] += val*self.__waypoint[0]
            self.__loc[1] += val*self.__waypoint[1]

    def __step_ferry(self):
        s = self.__instrs[self.__idx]
        val= int(s[1:])
        i = s[0]

        if i == 'N' or (self.__loc[2]==0 and i=='F'):
            self.__loc[0] += val
        elif i == 'S' or (self.__loc[2]==180 and i=='F'):
            self.__loc[0] -= val
        elif i == 'E' or (self.__loc[2]==90 and i=='F'):
            self.__loc[1] += val
        elif i == 'W' or (self.__loc[2]==270 and i=='F'):
            self.__loc[1] -= val
        elif i == 'L':
            self.__loc[2] = (self.__loc[2]-val)%360
        elif i == 'R':
            self.__loc[2] = (self.__loc[2]+val)%360
        elif i == 'F':
            raise Exception("We're heading an unexpected direction: %d"%(self.__loc[2]))


    def run(self):
        while self.step():
            pass

    def manhattan(self):
        return abs(self.__loc[0]) + abs(self.__loc[1])

    def __str__(self):
        if self.__mode == 0:
            return "Ferry at (%d,%d), heading: %d degrees"%(self.__loc[0],self.__loc[1],self.__loc[2])
        else:
            return "Ferry at (%d,%d), heading towards: (%d,%d)"%(self.__loc[0],self.__loc[1],self.__waypoint[0],self.__waypoint[1])

if __name__=='__main__':
    insts = [line.strip() for line in open("2020/day12/input.txt","r")]
    f = Ferry(insts)
    f.run()
    print(f)
    print(f.manhattan())
    f = Ferry(insts,1)
    f.run()
    print(f)
    print(f.manhattan())