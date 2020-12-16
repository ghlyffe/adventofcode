import json

def parse_bounce(el):
    tp = type(el)
    if tp == list:
        return parse_list(el)
    elif tp == dict:
        return parse_valid_dict(el)
    elif tp == int:
        return el
    elif tp == str:
        return 0
    else:
        raise Exception("unexpected type")

def parse_list(el):
    """
    >>> parse_list([])
    0
    >>> parse_list([1,2,3])
    6
    >>> parse_list([-1,{"a":1}])
    0
    >>> parse_list([[[3]]])
    3
    """
    cnt = 0
    for i in el:
        cnt += parse_bounce(i)
    return cnt
    
def parse_dict(el):
    """
    >>> parse_dict({"a":2,"b":4})
    6
    >>> parse_dict({"a":{"b":4},"c":-1})
    3
    >>> parse_dict({"a":[-1,1]})
    0
    >>> parse_dict({})
    0
    """
    cnt = 0
    for i in el:
        cnt += parse_bounce(el[i])
    return cnt

def parse_valid_dict(el):
    """
    >>> parse_valid_dict({"a":2,"b":4})
    6
    >>> parse_valid_dict({"a":{"b":4},"c":-1})
    3
    >>> parse_valid_dict({"a":[-1,1]})
    0
    >>> parse_valid_dict({})
    0
    >>> parse_list([1,{"c":"red","b":2},3])
    4
    >>> parse_valid_dict({"d":"red","e":[1,2,3,4],"f":5})
    0
    >>> parse_list([1,"red",5])
    6
    """
    cnt = 0
    for i in el:
        if el[i] == 'red':
            return 0
        cnt += parse_bounce(el[i])
    return cnt

def parse(fname):
    f = open(fname,"r")
    obj = json.load(f)
    f.close()
    return parse_bounce(obj)

if __name__=='__main__':
    import doctest
    doctest.testmod()

    total = parse('2015/day12/input.txt')
    print(total)