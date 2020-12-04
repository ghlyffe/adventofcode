def iterate(seq):
    """
    >>> iterate("1")
    '11'
    >>> iterate("11")
    '21'
    >>> iterate("21")
    '1211'
    >>> iterate("1211")
    '111221'
    >>> iterate("111221")
    '312211'
    """
    out = ""
    cur = seq[0]
    cnt = 0
    for i in range(len(seq)):
        if seq[i] == cur:
            cnt += 1
        else:
            out += str(cnt)
            out += cur
            cur = seq[i]
            cnt = 1
    out += str(cnt)
    out += cur

    return out

def run_n(seq,n=40):
    for i in range(n):
        seq = iterate(seq)
    return seq

if __name__=='__main__':
    import doctest
    doctest.testmod()

    s = run_n("1113222113")
    print(len(s))
    s = run_n(s,10)
    print(len(s))