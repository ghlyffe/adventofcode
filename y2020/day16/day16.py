class Rule(object):
    def __init__(self,line):
        pts = line.split(': ')
        self.__field = pts[0]
        ranges = pts[1].split(' or ')
        self.__ranges = []
        for r in ranges:
            pts = r.split('-')
            self.__ranges.append((int(pts[0]),int(pts[1])))

    def apply(self,value):
        return any([value >= p[0] and value <= p[1] for p in self.__ranges])

    def name(self):
        return self.__field

class Checker(object):
    def __init__(self, rules):
        self.__rules = rules

    def invalid_tickets(self, tickets):
        out = {}
        for t in tickets:
            for v in t:
                if all([not r.apply(v) for r in self.__rules]):
                    if t not in out:
                        out[t] = []
                    out[t].append(v)
        return out

    def error_rate(self, tickets):
        invalid = self.invalid_tickets(tickets)
        return sum([sum(i) for i in invalid.values()])

    def find_fields(self, tickets):
        valid = [t for t in tickets if t not in self.invalid_tickets(tickets).keys()]
        possible = {}
        for i in range(len(valid[0])):
            for r in self.__rules:
                if all([r.apply(v[i]) for v in valid]):
                    if i not in possible:
                        possible[i] = []
                    possible[i].append(r.name())

        fixed = [k for k,v in possible.items() if len(v)==1] #Find everything that has only one possibility
        while not all([len(i)==1 for i in possible.values()]):
            for k in possible.keys():
                if k not in fixed:
                    for f in fixed:
                        for p in possible[f]:
                            if p in possible[k]:
                                possible[k].remove(p)
                    if len(possible[k]) == 1:
                        fixed.append(k)
        return {k:v[0] for k,v in possible.items()}

def parse_lines(lines):
    rules = []
    own = None
    tickets = []

    parsing = 0
    for line in lines:
        if line == '':
            parsing += 1
            continue
        if parsing == 0:
            rules.append(Rule(line))
        elif parsing in (1,3):
            parsing += 1
        elif parsing == 2:
            own = [int(i) for i in line.split(',')]
        elif parsing == 4:
            tickets.append(tuple(int(i) for i in line.split(',')))
    return Checker(rules),own,tickets

def field_product(ticket,fields,pref="departure"):
    prod = 1
    ids = [idx for idx in fields if fields[idx][:len(pref)] == pref]
    for i in ids:
        prod *= ticket[i]
    return prod

if __name__=='__main__':
    checker,own,others = parse_lines([line.strip() for line in open("y2020/day16/input.txt")])
    print(checker.error_rate(others))

    fields = checker.find_fields(others)
    print(field_product(own,fields))