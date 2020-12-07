import re
def parse_line(line):
    bag,rest = line.strip().split(' bags contain ')
    if rest == 'no other bags.':
        return bag,{}
    contents = rest[:-1].split(', ')

    cont = {}
    for c in contents:
        m = re.match('(\d+) (.*) bag',c)
        if m:
            cont[m.groups()[1]] = int(m.groups()[0])

    return bag,cont

def parse_lines(lines):
    bags = set()
    contains = {}
    contained_by = {}
    for line in lines:
        bag,cont = parse_line(line)
        bags.add(bag)
        contains[bag] = cont
        if bag not in contained_by:
            contained_by[bag] = set()
        for k in cont:
            if k not in contained_by:
                contained_by[k] = set()
            contained_by[k].add(bag)
            bags.add(k)
    return bags,contains,contained_by


def find_contains(bag,contained_by):
    can_contain = contained_by[bag]
    checked = [bag]
    to_check = list(can_contain)
    for i in to_check:
        if i in checked:
            continue
        checked.append(i)
        nxt = contained_by[i]
        can_contain = can_contain.union(nxt)
        to_check.extend(list(nxt))
    return can_contain

def must_contain(bag,contains,mul=1):
    count = sum(contains[bag].values())
    for k in contains[bag]:
        count += must_contain(k,contains,contains[bag][k])

    return count * mul

if __name__=='__main__':
    bag,contains,contained_by = parse_lines([line for line in open("2020/day7/input.txt","r")])
    res = find_contains('shiny gold',contained_by)
    print(len(res))
    res = must_contain('shiny gold', contains)
    print (res)