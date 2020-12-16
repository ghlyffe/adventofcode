class Ingredient(object):
    def __init__(self,line):
        self._name,valstr = line.split(': ')
        vals = valstr.split(', ')
        self.__vals = {}
        for v in vals:
            k,v = v.split(' ')
            self.__vals[k] = int(v)