class Node(object):
    def __init__(sel, name):
        self.__name = name

class Edge(object):
    def __init__(self,dist):
        self.__dist = dist

class Graph(object):
    def __init__(self):
        self.__nodes = {}
        self.__edges = {}

    def parse_line(self, line):
        route,dist = line.split(' = ')
        start,end = route.split(' to ')
        if start not in self.__nodes:
            self.__nodes[start] = Node(start)
        if end not in self.__nodes:
            self.__nodes[end] = Node(end)
        self.__edges(start,end) = Edge(dist)
        
    