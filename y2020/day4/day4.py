import re

def lines_to_pass(lines):
    ports = []
    batch = {}
    for line in lines:
        if line.strip() == "":
            if len(batch.keys()):
                ports.append(batch)
            batch = {}
            continue
        pts = line.strip().split(' ')
        for p in pts:
            k,v = p.split(':')
            batch[k] = v
    if len(batch.keys()) > 0:
        ports.append(batch)
    return ports

def validate_num(yr,lo,hi,pattern="\d{4}$"):
    if not re.match(pattern, yr):
        return False
    y = int(yr)
    if y < lo or y > hi:
        return False
    return True

def validate_pass_data(port):
    for k in port.keys():
        if k == 'byr':
            if not validate_num(port[k],1920,2002):
                return False
        elif k == 'iyr':
            if not validate_num(port[k],2010,2020):
                return False
        elif k == 'eyr':
            if not validate_num(port[k],2020,2030):
                return False
        elif k == 'hgt':
            m = re.match("(\d{2,3})(cm|in)",port[k])
            if m is None:
                return False
            v = int(m.groups()[0])
            if m.groups()[1] == 'in':
                if v < 59 or v > 76:
                    return False
            else:
                if v < 150 or v > 193:
                    return False
        elif k == 'hcl':
            if not re.match('#[0-9a-f]{6}$',port[k]):
                return False
        elif k == 'ecl':
            if port[k] not in ['amb','blu','brn','gry','grn','hzl','oth']:
                return False
        elif k == 'pid':
            if not re.match('\d{9}$',port[k]):
                return False
    return True
            

def validate_passports(ports, validate_data=False, req_keys = ['byr','iyr','eyr','hgt','hcl','ecl','pid']):
    c = 0
    for p in ports:
        if all([i in p.keys() for i in req_keys]):
            if validate_data and not validate_pass_data(p):
                continue
            c += 1
    return c

if __name__=='__main__':
    lines = []
    for line in open("y2020/day4/input.txt","r"):
        lines.append(line)
    ports = lines_to_pass(lines)
    print(validate_passports(ports))
    print(validate_passports(ports, True))