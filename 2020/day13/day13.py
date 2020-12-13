import math
from collections import Counter

def is_int(i):
    try:
        int(i)
        return True
    except:
        return False

def get_ids(line):
    """
    >>> get_ids("7,13,x,x,59,x,31,19")
    [7, 13, 59, 31, 19]
    """
    pts = line.split(',')
    return [int(i) for i in pts if is_int(i)]

def earliest_bus(tstamp,buses):
    """
    >>> earliest_bus(939, [7, 13, 59, 31, 19])
    [(59, 5), (7, 6), (13, 10), (19, 11), (31, 22)]
    """
    eb = [(i, i-(tstamp%i)) for i in buses]
    return sorted(eb, key=lambda x: x[1])

def find_sequence(line):
    """
    n % ids[0] = 0
    ids[1] - n%ids[1] = 1
    .
    .
    .
    ids[-1] - n%ids[-1] = len(ids)-1

    (assuming ids includes the 'x' markers)


    >>> find_sequence("7,13,x,x,59,x,31,19")
    1068781
    """
    offsets = {}
    seq = []
    cur = 0
    pts = line.split(',')
    for i in pts:
        if is_int(i):
            offsets[int(i)] = cur
            seq.append(int(i))
        cur += 1

    cand = seq[0]
    while True:
        if all([(cand+offsets[i])%i==0 for i in seq]):
            return cand
        cand += seq[0]

if __name__=='__main__':
    import doctest
    doctest.testmod()

    lines = [line.strip() for line in open("2020/day13/input.txt","r")]
    tstamp = int(lines[0])
    buses = get_ids(lines[1])
    ordered = earliest_bus(tstamp,buses)
    print(ordered[0][0] * ordered[0][1])
    print(find_sequence(lines[1]))