def find_row(row_markers,rows=127):
    """
    >>> find_row('F')
    63
    >>> find_row('FB')
    63
    >>> find_row('FBF')
    47
    >>> find_row('FBFB')
    47
    >>> find_row('FBFBB')
    47
    >>> find_row('FBFBBF')
    45
    >>> find_row('FBFBBFF')
    44
    >>> find_row('BFFFBBF')
    70
    >>> find_row('FFFBBBF')
    14
    >>> find_row('BBFFBBF')
    102
    >>> find_row('RLR',7)
    5
    >>> find_row('RRR',7)
    7
    >>> find_row('RLL',7)
    4
    """
    hi = rows
    lo = 0
    for marker in row_markers:
        mod = int(round((hi-lo)/2.0))
        if mod == 0:
            mod = 1
        if marker in ['F','L']:
            hi -= mod
        elif marker in ['B','R']:
            lo += mod

    return hi

def process_pass(bpass):
    """
    >>> process_pass("FBFBBFFRLR")
    [44, 5]
    >>> process_pass("BFFFBBFRRR")
    [70, 7]
    >>> process_pass("FFFBBBFRRR")
    [14, 7]
    >>> process_pass("BBFFBBFRLL")
    [102, 4]
    """
    return [find_row(bpass[:7]),find_row(bpass[7:],7)]

def find_missing(passes):
    ids = sorted([i[0]*8+i[1] for i in [process_pass(p) for p in passes]])
    for i,v in enumerate(ids):
        if v+1 != ids[i+1]:
            return v+1

if __name__=='__main__':
    import doctest
    doctest.testmod()

    passes = [line.strip() for line in open("2020/day5/input.txt","r")]
    ids = {p:process_pass(p) for p in passes}
    print(max([i[0]*8+i[1] for i in ids.values()]))
    print(find_missing(passes))