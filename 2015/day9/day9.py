import itertools

class Graph(object):
    def __init__(self):
        self.__nodes = []
        self.__edges = {}

    def parse_line(self, line):
        route,dist = line.split(' = ')
        start,end = route.split(' to ')
        if start not in self.__nodes:
            self.__nodes.append(start)
        if end not in self.__nodes:
            self.__nodes.append(end)
        self.__edges[(start,end)] = int(dist)
        
    def __validate_single(self,perm):
        for i in range(len(perm)-1):
            if not ((perm[i],perm[i+1]) in self.__edges or (perm[i+1],perm[i]) in self.__edges):
                return False
        return True

    def valid_perms(self):
        perms = itertools.permutations(self.__nodes, len(self.__nodes))
        perms = [i for i in perms if self.__validate_single(i)]
        return perms

    def length_for_perm(self,perm):
        d = 0
        for i in range(len(perm)-1):
            fst,snd = perm[i:i+2]
            if (fst,snd) in self.__edges:
                d += self.__edges[(fst,snd)]
            else:
                d += self.__edges[(snd,fst)]
        return d

    def sorted_perms(self):
        return sorted(self.valid_perms(),key=self.length_for_perm)

if __name__=='__main__':
    g = Graph()
    for line in open("2015/day9/input.txt","r"):
        g.parse_line(line)
    ordered = g.sorted_perms()
    shortest = ordered[0]
    longest = ordered[-1]
    print(g.length_for_perm(shortest))
    print(g.length_for_perm(longest))