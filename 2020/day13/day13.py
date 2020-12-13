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
    Turns out that this is a CRT-solving sieve, so these tests should be expanded.
    https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Search_by_sieving

    Be prepared for:
    * Set pairwise coprimality
    * Linear Diophantine Systems
    * Univariate polynomial rings and Euclidean domains

    There's a lot of heavy mathematics, the sieve method comes down (approximately) to the approach here:
    * Treat everything as starting from the same number with a modulo (how many steps forward we want it)
    * Find the lowest number where the first two moduli are 0
    * Then scan forwards in steps of the product of all "fixed" moduli to lock in the next
    * Repeat until the entire list is fixed.

    n % ids[0] = 0
    ids[1] - n%ids[1] = 1
    .
    .
    .
    ids[-1] - n%ids[-1] = len(ids)-1

    (assuming ids includes the 'x' markers)


    >>> find_sequence("7,13,x,x,59,x,31,19")
    1068781
    >>> find_sequence("67,7,59,61")
    754018
    >>> find_sequence("67,x,7,59,61")
    779210
    >>> find_sequence("67,7,x,59,61")
    1261476
    >>> find_sequence("1789,37,47,1889")
    1202161486
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

    cand = 0
    fixed = 1
    inc = seq[0]
    while fixed < len(seq):
        cand += inc
        if (cand+offsets[seq[fixed]]) % seq[fixed] == 0:
            fixed += 1
            inc = lcm(seq[:fixed])
    return cand

def lcm(lst):
    """
    >>> lcm([7,13])
    91
    >>> lcm([7,13,59])
    5369
    >>> lcm([7,13,59,31])
    166439
    """
    cur = int(lst[0]*lst[1] / math.gcd(lst[0],lst[1]))
    for i in range(2,len(lst)):
        cur = int((cur*lst[i])/math.gcd(cur,lst[i]))
    return cur


if __name__=='__main__':
    import doctest
    doctest.testmod()

    lines = [line.strip() for line in open("2020/day13/input.txt","r")]
    tstamp = int(lines[0])
    buses = get_ids(lines[1])
    ordered = earliest_bus(tstamp,buses)
    print(ordered[0][0] * ordered[0][1])
    print(find_sequence(lines[1]))