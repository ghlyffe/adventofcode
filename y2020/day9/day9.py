def find_pair(exps,total):
    for idx,val1 in enumerate(exps[:-1]):
        for val2 in exps[idx:]:
            if val1 + val2 == total:
                return val1,val2

def find_first_failure(vals, preamble_size):
    """
    >>> find_first_failure([35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576],5)
    127
    """
    for i in range(len(vals)-preamble_size):
        if find_pair(vals[i:preamble_size+i], vals[preamble_size+i]) == None:
            return vals[preamble_size+i]

def find_contiguous_seq(seq,total):
    """
    >>> find_contiguous_seq([35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576],127)
    [15, 25, 47, 40]
    """
    start_idx = 0
    end_idx = 0
    for i in range(len(seq)):
        s = seq[i]
        for j in range(len(seq)-i):
            s += seq[i+j+1]
            if s == total:
                return seq[i:i+j+2]
            elif s > total:
                break

if __name__=='__main__':
    import doctest
    doctest.testmod()
    seq = [int(line.strip()) for line in open("y2020/day9/input.txt","r")]
    failure = find_first_failure(seq,25)
    print(failure)
    contig_seq = find_contiguous_seq(seq,failure)
    print(min(contig_seq) + max(contig_seq))