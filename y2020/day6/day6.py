def get_questions_as_set():
    return set([chr(i+97) for i in range(26)])

def parse_lines(lines,intersect=False):
    groups = []
    grp = set()
    if intersect:
        grp = get_questions_as_set()
    for line in lines:
        if line.strip() == "":
            groups.append(grp)
            grp = set()
            if intersect:
                grp = get_questions_as_set()
            continue
        if intersect:
            grp = grp.intersection([i for i in line.strip()])
        else:
            grp = grp.union([i for i in line.strip()])
    if len(grp):
        groups.append(grp)
    return groups

def parse_file(fname,intersect=False):
    return parse_lines([line for line in open(fname,"r")], intersect)

def count_resps(resps):
    c = 0
    for r in resps:
        c += len(r)
    return c

if __name__=='__main__':
    resps = parse_file("y2020/day6/input.txt")
    print(count_resps(resps))
    resps = parse_file("y2020/day6/input.txt",True)
    print(count_resps(resps))