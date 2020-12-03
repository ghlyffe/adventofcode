def file_to_grid(fname):
    out = []
    for line in open(fname,"r"):
        out.append(line.strip())
    return out

def trees_on_slope(grid,slope):
    y_inc, x_inc = slope
    y,x=(0,0)
    trees = 0
    while y < len(grid):
        if grid[y][x] == '#':
            trees += 1
        y += y_inc
        x = (x + x_inc) % len(grid[0])
    return trees

if __name__=='__main__':
    grid = file_to_grid('2020/day3/input.txt')
    trees = [trees_on_slope(grid,(1,1)),trees_on_slope(grid,(1,3)),trees_on_slope(grid,(1,5)),trees_on_slope(grid,(1,7)),trees_on_slope(grid,(2,1))]
    print(trees[1])
    prod = 1
    for i in trees:
        prod *= i

    print(prod)