import copy

def adapter_differences(adapters):
    """
    >>> adapter_differences([16,10,15,5,1,11,7,19,6,12,4])
    (7, 5)
    >>> adapter_differences([28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3])
    (22, 10)
    """
    one = 1 # From the outlet
    three = 1 # To the device
    adapts = sorted(adapters)
    for i in range(len(adapts)-1):
        diff = adapts[i+1] - adapts[i]
        if diff == 1:
            one += 1
        elif diff == 3:
            three += 1
    return one,three

def find_next_options(adapters, value):
    out = []
    for i in adapters:
        diff = value - i
        if diff > 3:
            break
        elif diff < 1:
            continue
        out.append(i)
    return out

def find_arrangements(adapters, arrangements):
    """
    >>> len(find_arrangements([i for i in reversed(sorted([16,10,15,5,1,11,7,19,6,12,4]))],[[22]]))
    8
    >>> len(find_arrangements([i for i in reversed(sorted([28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]))],[[52]]))
    19208
    """
    arrs = []
    for i in arrangements:
        target = i[-1]
        opts = find_next_options(adapters,i[-1])
        if target <= 3: #We might have already finished this arrangement (meaning no opts), but also it's valid as it is (meaning it ends in 3 or less)
            if i not in arrs:
                arrs.append(copy.copy(i))
        for j in opts:
            new = copy.copy(i)
            new.append(j)
            if new not in arrs:
                arrs.append(new)
    if sorted(arrs) == sorted(arrangements):
        return arrangements
    return find_arrangements(adapters,arrs)

def sort_and_reverse(lst):
    return [i for i in reversed(sorted(lst))]


def file_to_ratings(fname):
    return [int(line.strip()) for line in open(fname,"r")]

if __name__=='__main__':
    import doctest
    doctest.testmod()

    adapters = file_to_ratings("2020/day10/input.txt")
    diffs = adapter_differences(adapters)
    print(diffs[0]*diffs[1])
    print(len(find_arrangements(sort_and_reverse(adapters),[max(adapters)+3])))