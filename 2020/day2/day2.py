def check_pwd_count(pwd):
    pts = pwd.split(': ')

    count_pts = pts[0].split(' ')
    min,max = [int(i) for i in count_pts[0].split('-')]
    letter = count_pts[1]
    val = pts[1].count(letter)
    if val < min or val > max:
        return False
    return True

def check_all(file,checker):
    c = 0
    for line in open(file,"r"):
        if checker(line):
            c += 1
    return c

def check_pwd_loc(pwd):
    pts = pwd.split(': ')

    count_pts = pts[0].split(' ')
    p1,p2 = [int(i)-1 for i in count_pts[0].split('-')]
    letter = count_pts[1]
    if (pts[1][p1] == letter) == (pts[1][p2] == letter):
        return False
    return True

if __name__=='__main__':
    print(check_all('2020/day2/input.txt',check_pwd_count))
    print(check_all('2020/day2/input.txt',check_pwd_loc))