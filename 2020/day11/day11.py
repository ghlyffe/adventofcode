import copy

def neumann_neighbourhood(grid,y,x): # In VSCode (the slowest profiling I've seen yet on identical code), takes ~4us per call
    max_y = len(grid)
    max_x = len(grid[y])
    n = 0
    if y > 0:
        if x > 0:
            if grid[y-1][x-1] == '#':
                n += 1
        if grid[y-1][x] == '#':
            n += 1
        if x < max_x-1:
            if grid[y-1][x+1] == '#':
                n += 1
    if x > 0:
        if grid[y][x-1] == '#':
            n += 1
    if x < max_x-1:
        if grid[y][x+1] == '#':
            n += 1

    if y < max_y-1:
        if x > 0:
            if grid[y+1][x-1] == '#':
                n += 1
        if grid[y+1][x] == '#':
            n += 1
        if x < max_x-1:
            if grid[y+1][x+1] == '#':
                n += 1
    return n

def visibility_neighbourhood(grid,y,x): # In VSCode, takes ~11us per call
    n = 0
    max_y = len(grid)
    max_x = len(grid[y])
    for iy in range(y-1,-1,-1): # up
        if grid[iy][x] == '.':
            continue
        else:
            if grid[iy][x] == '#':
                n += 1
            break
    for iy in range(y+1,max_y): # down
        if grid[iy][x] == '.':
            continue
        else:
            if grid[iy][x] == '#':
                n += 1
            break
    for ix in range(x-1,-1,-1): # left
        if grid[y][ix] == '.':
            continue
        else:
            if grid[y][ix] == '#':
                n += 1
            break
    for ix in range(x+1,max_x): # right
        if grid[y][ix] == '.':
            continue
        else:
            if grid[y][ix] == '#':
                n += 1
            break
    # up-left
    iy = y-1
    ix = x-1
    while iy > -1 and ix > -1:
        if grid[iy][ix] == '.':
            iy -= 1
            ix -= 1
            continue
        else:
            if grid[iy][ix] == '#':
                n += 1
            break
    # up-right
    iy = y-1
    ix = x+1
    while iy > -1 and ix < max_x:
        if grid[iy][ix] == '.':
            iy -= 1
            ix += 1
            continue
        else:
            if grid[iy][ix] == '#':
                n += 1
            break
    # down-left
    iy = y+1
    ix = x-1
    while iy < max_y and ix > -1:
        if grid[iy][ix] == '.':
            iy += 1
            ix -= 1
            continue
        else:
            if grid[iy][ix] == '#':
                n += 1
            break
    # down-right
    iy = y+1
    ix = x+1
    while iy < max_y and ix < max_x:
        if grid[iy][ix] == '.':
            iy += 1
            ix += 1
            continue
        else:
            if grid[iy][ix] == '#':
                n += 1
            break
    return n


class Automaton(object):
    def __init__(self,grid,rules,neighborhood=neumann_neighbourhood):
        self.__grid = grid
        self.__rules = rules
        self.__gen = 0
        self.__neighbourhood = neighborhood

    def generation(self):
        changed = False
        max_y = len(self.__grid)
        new = []
        for y in range(max_y):
            new.append([])
            max_x = len(self.__grid[y])
            for x in range(max_x):
                n = self.__neighbourhood(self.__grid,y,x)
                new[y].append(self.__rules[self.__grid[y][x]][n])
                if new[y][x] != self.__grid[y][x]:
                    changed = True
        self.__grid = new
        self.__gen += 1
        return changed

    def run(self,ngen):
        for i in range(ngen):
            self.generation()

    def run_to_stable(self):
        while self.generation():
            pass

    def grid(self):
        return copy.deepcopy(self.__grid)

    def count_occupied(self):
        out = 0
        for y in range(len(self.__grid)):
            for x in range(len(self.__grid[y])):
                if self.__grid[y][x] == '#':
                    out += 1
        return out


def lines_to_grid(lines):
    out = []
    for line in lines:
        out.append([i for i in line.strip()])
    return out

def part_1_rules():
    rules = {'#': {i:'#' for i in range(9)}, 'L': {i:'L' for i in range(9)}, '.': {i:'.' for i in range(9)}}
    rules['L'][0] = '#'
    rules['#'][4] = 'L'
    rules['#'][5] = 'L'
    rules['#'][6] = 'L'
    rules['#'][7] = 'L'
    rules['#'][8] = 'L'
    return rules

def part_2_rules():
    rules = {'#': {i:'#' for i in range(9)}, 'L': {i:'L' for i in range(9)}, '.': {i:'.' for i in range(9)}}
    rules['L'][0] = '#'
    rules['#'][5] = 'L'
    rules['#'][6] = 'L'
    rules['#'][7] = 'L'
    rules['#'][8] = 'L'
    return rules

def gol_rules():
    rules = {'#': {i:'.' for i in range(9)}, '.': {i:'.' for i in range(9)}}
    rules['#'][2] = '#'
    rules['#'][3] = '#'
    rules['.'][3] = '#'
    return rules

if __name__=='__main__':
    start = lines_to_grid([line for line in open("2020/day11/input.txt","r")])
    ca = Automaton(start,part_1_rules())
    ca.run_to_stable()
    print(ca.count_occupied())
    start = lines_to_grid([line for line in open("2020/day11/input.txt","r")])
    ca = Automaton(start,part_2_rules(), visibility_neighbourhood)
    ca.run_to_stable()
    print(ca.count_occupied())