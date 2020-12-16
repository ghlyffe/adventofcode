#!/usr/bin/python3

def common_point(l1,l2):
    """
    >>> common_point(["A"],["B"])
    >>> common_point(["A","B","C","D"],["E","F","G","H","B","C","D"])
    'B'
    """
    for val in l1:
        if val in l2:
            return val
    return None

def common_dist(l1,l2):
    """
    >>> common_dist(["A"],["B"])
    -1
    >>> common_dist(["A","B","C","D"],["E","F","G","H","B","C","D"])
    5
    """
    v = common_point(l1,l2)
    if v:
        return l1.index(v) + l2.index(v)
    return -1

class Graph(object):
    """
    >>> g = Graph()
    >>> g.add_edge(("COM","B"))
    >>> g.add_edge(("B","C"))
    >>> g.add_edge(("B","G"))
    >>> g.add_edge(("G","H"))
    >>> g.add_edge(("C","D"))
    >>> g.add_edge(("D","E"))
    >>> g.add_edge(("D","I"))
    >>> g.add_edge(("E","F"))
    >>> g.add_edge(("E","J"))
    >>> g.add_edge(("J","K"))
    >>> g.add_edge(("K","L"))
    >>> g.total_orbits_one("D")
    3
    >>> g.total_orbits_one("L")
    7
    >>> g.total_orbits_one("COM")
    0
    >>> g.total_orbits()
    42
    >>> g.route_to_root("COM")
    ['COM']
    >>> g.route_to_root("G")
    ['G', 'B', 'COM']
    >>> g.dist_between("F","J")
    0
    >>> g.dist_between("H","K")
    5
    """
    def __init__(self):
       self.__nodes = []
       self.__edges = []
       self.__cache = {}

    def total_orbits_one(self,key):
        if key in self.__cache:
            return self.__cache[key]
        directly_orbits = [edge[0] for edge in self.__edges if edge[1] == key]
        total = len(directly_orbits)
        total += sum([self.total_orbits_one(i) for i in directly_orbits])
        self.__cache[key] = total
        return total

    def total_orbits(self):
        return sum([self.total_orbits_one(i) for i in self.__nodes])

    def add_edge(self,edge):
        if edge[0] not in self.__nodes:
            self.__nodes.append(edge[0])
        if edge[1] not in self.__nodes:
            self.__nodes.append(edge[1])
        if edge not in self.__edges:
            self.__edges.append(edge)

    def route_to_root(self,key):
        hops = [key]
        next = [i[0] for i in self.__edges if i[1] == hops[-1]]
        while len(next) > 0:
            hops.extend(next)
            next = [i[0] for i in self.__edges if i[1] == hops[-1]]
        return hops

    def dist_between(self,key1,key2):
        r1 = self.route_to_root(key1)
        r2 = self.route_to_root(key2)
        return common_dist(r1,r2) - 2

def file_to_edges(fname):
    return [line.strip().split(")") for line in open(fname,"r")]

if __name__=='__main__':
    import doctest
    doctest.testmod()

    g = Graph()
    for e in file_to_edges("input.txt"):
        g.add_edge(e)
    print(g.total_orbits())
    print(g.dist_between("YOU","SAN"))
