def gen_square(size):
    out = []
    for i in range(size):
        app = []
        for i in range(size):
            app.append(0)
        out.append(app)
    return out


def range_to_points(rng):
    """
    >>> range_to_points(((1,2),(3,4)))
    (2, 4, 1, 3)
    >>> range_to_points(((3,2),(1,4)))
    (2, 4, 1, 3)
    """
    c1,c2 = rng

    start_row = min(c1[1],c2[1])
    end_row = max(c1[1],c2[1])
    start_col = min(c1[0],c2[0])
    end_col = max(c1[0],c2[0])
    return start_row,end_row,start_col,end_col

def apply(map,rng,op):
    """
    >>> map = gen_square(5)
    >>> map
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    >>> apply(map,((1,2),(1,4)),on)
    >>> map
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0]]
    >>> apply(map,((1,2),(3,4)),on)
    >>> map
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 2, 1, 1, 0], [0, 2, 1, 1, 0], [0, 2, 1, 1, 0]]
    >>> apply(map,((0,1),(2,3)),off)
    >>> map
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [0, 2, 1, 1, 0]]
    """
    start_row,end_row,start_col,end_col = range_to_points(rng)

    for y in range(start_row,end_row+1):
        for x in range(start_col,end_col+1):
            op(map,(y,x))

def on(map,loc):
    """
    >>> map = [[0,0,0],[0,0,0],[0,0,0]]
    >>> on(map, (2,1))
    >>> map
    [[0, 0, 0], [0, 0, 0], [0, 1, 0]]
    >>> on(map, (2,1))
    >>> map
    [[0, 0, 0], [0, 0, 0], [0, 2, 0]]
    """
    map[loc[0]][loc[1]] += 1
    
def off(map,loc):
    """
    >>> map = [[0,0,0],[0,0,0],[0,1,0]]
    >>> off(map, (2,1))
    >>> map
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    >>> off(map, (2,1))
    >>> map
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    """
    if map[loc[0]][loc[1]] != 0:
        map[loc[0]][loc[1]] -= 1

def toggle(map,loc):
    """
    >>> map = [[0,0,0],[0,0,0],[0,0,0]]
    >>> toggle(map, (2,1))
    >>> map
    [[0, 0, 0], [0, 0, 0], [0, 2, 0]]
    >>> toggle(map, (2,1))
    >>> map
    [[0, 0, 0], [0, 0, 0], [0, 4, 0]]
    """
    map[loc[0]][loc[1]] += 2

def parse_instr(instr):
    """
    >>> parse_instr("turn on 123,456 through 987,654")
    (<function on at 0x...>, ((123, 456), (987, 654)))

    >>> parse_instr("turn off 123,456 through 987,654")
    (<function off at 0x...>, ((123, 456), (987, 654)))

    >>> parse_instr("toggle 123,456 through 987,654")
    (<function toggle at 0x...>, ((123, 456), (987, 654)))
    """
    op = None
    idx = 0
    if instr[:7] == 'turn on':
        op = on
        idx = 7
    elif instr[:8] == 'turn off':
        op = off
        idx = 8
    else:
        op = toggle
        idx = 6

    rng_parts = instr[idx:].split(" through ")
    rng = tuple([tuple([int(i) for i in rng_parts[0].split(',')]),tuple([int(i) for i in rng_parts[1].split(',')])])
    return op,rng

def run_file(fname, map):
    instrs = []
    for line in open(fname,"r"):
        instrs.append(line.strip())
    
    for instr in instrs:
        op,rng = parse_instr(instr)
        apply(map,rng,op)

if __name__=='__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)

    map = gen_square(1000)
    run_file("2015/day6/input.txt", map)
# The following for "bad toggle"
#    c = 0
#    for y in range(1000):
#        for x in range(1000):
#            if map[y][x] != 0:
#                c += 1
#    print(c)
    print(sum([sum(i) for i in map]))