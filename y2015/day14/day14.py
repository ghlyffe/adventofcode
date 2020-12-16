import re

class Reindeer(object):
    def __init__(self,name,spd,dur,rest):
        self.__name = name
        self.__speed = spd
        self.__duration = dur
        self.__rest = rest

    def distance(self,time):
        cycles = int(time / (self.__duration + self.__rest))
        rem = time % (self.__duration + self.__rest)
        addl = min(rem,self.__duration)
        return ((cycles * self.__duration) + addl) * self.__speed

    def __str__(self):
        return "%s can fly %d km/s for %d seconds, but then must rest for %d seconds."%(self.__name,self.__speed,self.__duration,self.__rest)

def reindeer_from_line(line):
    match = re.match("([A-Z][a-z]+) .* (\d+) km/s.* (\d+) .* (\d+) .*",line)
    return Reindeer(match.groups()[0],int(match.groups()[1]),int(match.groups()[2]),int(match.groups()[3]))

def parse_file(fname):
    out = []
    for line in open(fname,"r"):
        out.append(reindeer_from_line(line))
    return out

def points(reindeer, time):
    """
    >>> r = [reindeer_from_line("Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds."), reindeer_from_line("Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.")]
    >>> scores = points(r,140)
    >>> scores['Comet']
    1
    >>> scores['Dancer']
    139
    >>> scores = points(r,1000)
    >>> scores['Comet']
    312
    >>> scores['Dancer']
    689
    """
    scores = {r._Reindeer__name:0 for r in reindeer}
    for t in range(time):
        res = race(reindeer,t+1)
        scores[res[0]._Reindeer__name] += 1
        dst = res[0].distance(t+1)
        for i in res[1:]:
            if i.distance(t+1) == dst:
                scores[i._Reindeer__name] += 1
            else:
                break
    return scores

def race(reindeer,time):
    """
    >>> r = [reindeer_from_line("Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds."), reindeer_from_line("Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.")]
    >>> res = race(r,1000)
    >>> print(res[0])
    Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
    >>> res[0].distance(1000)
    1120
    >>> print(res[1])
    Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
    >>> res[1].distance(1000)
    1056
    """
    results = sorted(reindeer, key=lambda x: x.distance(time))
    results.reverse()
    return results

if __name__=='__main__':
    import doctest
    doctest.testmod()

    reindeer = parse_file("2015/day14/input.txt")
    results = race(reindeer,2503)
    print(results[0].distance(2503))
    scores = points(reindeer,2503)
    s = sorted(scores.keys(), key=lambda x: scores[x])
    print(scores[s[-1]])
    