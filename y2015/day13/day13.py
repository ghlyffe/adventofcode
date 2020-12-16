import re
import itertools

def parse_line(line):
    """
    >>> parse_line("Alice would gain 54 happiness units by sitting next to Bob.")
    {'Alice': {'Bob': 54}}
    >>> parse_line("Alice would lose 79 happiness units by sitting next to Carol.")
    {'Alice': {'Carol': -79}}
    >>> parse_line("Alice would lose 2 happiness units by sitting next to David.")
    {'Alice': {'David': -2}}
    >>> parse_line("Bob would gain 83 happiness units by sitting next to Alice.")
    {'Bob': {'Alice': 83}}
    >>> parse_line("Bob would lose 7 happiness units by sitting next to Carol.")
    {'Bob': {'Carol': -7}}
    >>> parse_line("Bob would lose 63 happiness units by sitting next to David.")
    {'Bob': {'David': -63}}
    >>> parse_line("Carol would lose 62 happiness units by sitting next to Alice.")
    {'Carol': {'Alice': -62}}
    >>> parse_line("Carol would gain 60 happiness units by sitting next to Bob.")
    {'Carol': {'Bob': 60}}
    >>> parse_line("Carol would gain 55 happiness units by sitting next to David.")
    {'Carol': {'David': 55}}
    >>> parse_line("David would gain 46 happiness units by sitting next to Alice.")
    {'David': {'Alice': 46}}
    >>> parse_line("David would lose 7 happiness units by sitting next to Bob.")
    {'David': {'Bob': -7}}
    >>> parse_line("David would gain 41 happiness units by sitting next to Carol.")
    {'David': {'Carol': 41}}
    """
    match = re.match("([A-Z][a-z]+).*(gain|lose) (\d+) .* ([A-Z][a-z]+)\.$",line)
    if match:
        src = match.groups()[0]
        dest = match.groups()[-1]
        chg = int(match.groups()[2])
        if match.groups()[1] == "lose":
            chg = 0-chg
        return {src:{dest:chg}}
    return {}

def value_for_perm(perm,chgs):
    """
    >>> chgs = parse_line("Alice would gain 54 happiness units by sitting next to Bob.")
    >>> merge_dicts(chgs, parse_line("Alice would lose 79 happiness units by sitting next to Carol."))
    >>> merge_dicts(chgs, parse_line("Alice would lose 2 happiness units by sitting next to David."))
    >>> merge_dicts(chgs, parse_line("Bob would gain 83 happiness units by sitting next to Alice."))
    >>> merge_dicts(chgs, parse_line("Bob would lose 7 happiness units by sitting next to Carol."))
    >>> merge_dicts(chgs, parse_line("Bob would lose 63 happiness units by sitting next to David."))
    >>> merge_dicts(chgs, parse_line("Carol would lose 62 happiness units by sitting next to Alice."))
    >>> merge_dicts(chgs, parse_line("Carol would gain 60 happiness units by sitting next to Bob."))
    >>> merge_dicts(chgs, parse_line("Carol would gain 55 happiness units by sitting next to David."))
    >>> merge_dicts(chgs, parse_line("David would gain 46 happiness units by sitting next to Alice."))
    >>> merge_dicts(chgs, parse_line("David would lose 7 happiness units by sitting next to Bob."))
    >>> merge_dicts(chgs, parse_line("David would gain 41 happiness units by sitting next to Carol."))
    >>> value_for_perm(('Alice','Bob','Carol','David'),chgs)
    330
    """
    total = 0
    for i in range(len(perm)-1):
        fst = perm[i]
        snd = perm[i+1]
        total += chgs[fst][snd]
        total += chgs[snd][fst]
    fst = perm[0]
    snd = perm[-1]
    total += chgs[fst][snd]
    total += chgs[snd][fst]
    return total

def merge_dicts(fst,snd):
    for key in snd:
        if key not in fst:
            fst[key] = {}
        fst[key].update(snd[key])

def parse_file(fname):
    out = {}
    for line in open(fname,"r"):
        merge_dicts(out, parse_line(line))
    return out

def test_perms(chgs):
    perms = itertools.permutations(chgs.keys(),len(chgs.keys()))
    s = sorted(perms,key=lambda x: value_for_perm(x, chgs))
    return s

def insert_self(chgs):
    others = chgs.keys()
    chgs['Self'] = {}
    for o in others:
        chgs['Self'][o] = 0
        chgs[o]['Self'] = 0

if __name__=='__main__':
    import doctest
    doctest.testmod()
    
    chgs = parse_file("2015/day13/input.txt")
    perms = test_perms(chgs)
    print(value_for_perm(perms[-1],chgs))
    insert_self(chgs)
    perms = test_perms(chgs)
    print(value_for_perm(perms[-1],chgs))