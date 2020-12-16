#!python3

def find_pair(exps,total):
    for idx,val1 in enumerate(exps[:-1]):
        for val2 in exps[idx:]:
            if val1 + val2 == total:
                return val1,val2

def find_triple(exps,total):
    for idx,val1 in enumerate(exps[:-2]):
        for idx_in,val2 in enumerate(exps[idx:-1]):
            for val3 in exps[idx+idx_in:]:
                if val1 + val2 + val3 == total:
                    return val1,val2,val3

def expenses(fname):
    exps = []
    for line in open(fname,'r'):
        exps.append(int(line.strip()))
    return exps

if __name__ == '__main__':
    exps = expenses("y2020/day1/input.txt")
    vals = find_pair(exps,2020)
    print(vals[0]*vals[1])
    vals = find_triple(exps,2020)
    print(vals[0]*vals[1]*vals[2])