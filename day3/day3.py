#!/usr/bin/python3

def moves_to_edges(moves):
    """
    >>> moves_to_edges([])
    []

    >>> moves_to_edges(["U5"])
    [((0, 0), (0, 5))]

    >>> moves_to_edges(["R8","U5","L5","D3"])
    [((0, 0), (8, 0)), ((8, 0), (8, 5)), ((8, 5), (3, 5)), ((3, 5), (3, 2))]
    """
    cur_x = 0
    cur_y = 0
    last_point = (0,0)
    edges = []
    for move in moves:
        direction = move[0]
        dist = int(move[1:])
        if direction == "U":
            cur_y += dist
        elif direction == "D":
            cur_y -= dist
        elif direction == "R":
            cur_x += dist
        elif direction == "L":
            cur_x -= dist
        edges.append((last_point,(cur_x,cur_y)))
        last_point = (cur_x,cur_y)
    return edges

class Intersection(object):
    """
    >>> i = Intersection((1,2),43)
    >>> i.dist()
    3

    >>> i2 = Intersection((1,1),20)
    >>> i < i2
    False

    >>> i == i2
    False

    >>> i > i2
    True
    """
    def __init__(self, coord, steps):
        self.__loc = coord
        self.__steps = steps

    def dist(self):
        return abs(self.__loc[0]) + abs(self.__loc[1])

    def __str__(self):
        return str(self.__loc) + " => " + str(self.dist()) + ":" + str(self.__steps)

    def __eq__(self,other):
#        return self.__loc == other.__loc
        return self.__steps == other.__steps

    def __gt__(self,other):
#        return self.dist() > other.dist()
        return self.__steps > other.__steps

    def __lt__(self,other):
#        return self.dist() < other.dist()
        return self.__steps < other.__steps

class Wire(object):
    """
    >>> w = Wire(["R8","U5","L5","D3"])
    >>> w2 = Wire(["U7","R6","D4","L4"])
    >>> list(map(str,w.intersects(w2)))
    ['(6, 5) => 11:30', '(3, 3) => 6:40']

    >>> w = Wire(["U5"])
    >>> w.intersects(w2)
    []
    """
    def __init__(self, moves):
        self.__moves = moves
        self.__edges = moves_to_edges(moves)

    def intersects(self, other):
        intersections = []
        for i in self.__edges:
            for j in other.__edges:
                if j[0][0] == j[1][0] and i[0][1] == i[1][1] and ((j[0][1] < i[0][1] and j[1][1] > i[1][1]) or (j[0][1] > i[0][1] and j[1][1] < i[1][1])) and ((j[0][0] < i[0][0] and j[1][0] > i[1][0]) or (j[0][0] > i[0][0] and j[1][0] < i[1][0])):
                    steps = 0
                    steps += sum([int(m[1:]) for m in self.__moves[:self.__edges.index(i)]]) + abs(i[0][0]-j[0][0])
                    steps += sum([int(m[1:]) for m in other.__moves[:other.__edges.index(j)]]) + abs(i[0][1]-j[0][1])
                    intersections.append(Intersection((j[0][0],i[0][1]),steps))
                if j[0][1] == j[1][1] and i[0][0] == i[1][0] and ((j[0][0] < i[0][0] and j[1][0] > i[1][0]) or (j[0][0] > i[0][0] and j[1][0] < i[1][0])) and ((j[0][1] < i[0][1] and j[1][1] > i[1][1]) or (j[0][1] > i[0][1] and j[1][1] < i[1][1])):
                    steps = 0
                    steps += sum([int(m[1:]) for m in self.__moves[:self.__edges.index(i)]]) + abs(i[0][0]-j[0][0])
                    steps += sum([int(m[1:]) for m in other.__moves[:other.__edges.index(j)]]) + abs(i[0][1]-j[0][1])
                    intersections.append(Intersection((i[0][0],j[0][1]),steps))
        return intersections

    def __str__(self):
        return "\n".join([str(self.__moves),str(self.__edges)])

if __name__=='__main__':
    import doctest
    doctest.testmod()

##############################################

    wires = []
    for line in open("day3_input.txt","r"):
#    for line in open("day3_scratch","r"):
        wires.append(Wire(line.strip().split(",")))
    intersections = []
    for i in range(len(wires)):
        for j in range(i+1,len(wires)):
            intersections.extend(wires[i].intersects(wires[j]))
    si = sorted(intersections)
    for i in si:
        print(i)
