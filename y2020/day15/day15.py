def run_n(gen,count=2020):
    out = next(gen)
    while out[0] != count:
        out = next(gen)
    return out
    

def generator(init):
    """
    >>> g = generator([0,3,6])
    >>> next(g)
    (4, 0)
    >>> next(g)
    (5, 3)
    >>> next(g)
    (6, 3)
    >>> next(g)
    (7, 1)
    >>> next(g)
    (8, 0)
    >>> next(g)
    (9, 4)
    >>> next(g)
    (10, 0)
    >>> g = generator([1,3,2])
    >>> run_n(g)
    (2020, 1)
    >>> g = generator([2,1,3])
    >>> run_n(g)
    (2020, 10)
    >>> g = generator([1,2,3])
    >>> run_n(g)
    (2020, 27)
    >>> g = generator([2,3,1])
    >>> run_n(g)
    (2020, 78)
    >>> g = generator([3,2,1])
    >>> run_n(g)
    (2020, 438)
    >>> g = generator([3,1,2])
    >>> run_n(g)
    (2020, 1836)
    """
    latest = {v:i+1 for i,v in enumerate(init)} # Assume no repeats in the setup
    prev = {}
    count = len(init)+1
    lst = init[-1]
    nxt = 0
    if nxt in latest:
        prev[nxt] = latest[nxt]
    latest[nxt] = count
    while True:
        yield count,nxt
        count += 1
        if nxt in prev:
            nxt = latest[nxt] - prev[nxt]
        else:
            nxt = 0
        if nxt in latest:
            prev[nxt] = latest[nxt]
        latest[nxt] = count


if __name__=='__main__':
    import doctest
    doctest.testmod()
    g = generator([1,2,16,19,18,0])
    res = run_n(g)
    print(res[1])
    res = run_n(g,30000000)
    print(res[1])