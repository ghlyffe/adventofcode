import ast
import doctest
import re

def count_diff(instr):
    """
    >>> count_diff('""')
    2
    >>> count_diff('"abc"')
    2
    >>> count_diff('"aaa\\\\"aaa"')
    3
    >>> count_diff('"\\\\x27"')
    5
    """
    return len(instr) - len(ast.literal_eval(instr))

def count_diff_escape(instr):
    i2 = re.escape(instr)
    i2 = i2.replace('"',r'\"')
    return len(i2) - len(instr) + 2 # Remember to add the surrounding quotes that we'll miss

if __name__ == '__main__':
    doctest.testmod()
    c = 0
    c2 = 0
    for line in open("2015/day8/input.txt","r"):
        c += count_diff(line.strip())
        c2 += count_diff_escape(line.strip())
    print(c)
    print(c2)