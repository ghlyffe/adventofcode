import unittest

try:
    import day10
except:
    import y2020.day10.day10 as day10

class TestAdapters(unittest.TestCase):
    def test_build_map(self):
        adapters = [16,10,15,5,1,11,7,19,6,12,4]
        mapping = {}
        day10.build_map(adapters,mapping)
        expect = {0: [1],  1: [4],  4: [5, 6, 7],  5: [6, 7],  6: [7],  7: [10],  10: [11, 12],  11: [12],  12: [15],  15: [16],  16: [19],  19: [22]}
        self.assertEqual(mapping,expect)

    def test_build_map_large(self):
        adapters = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]
        mapping = {}
        day10.build_map(adapters,mapping)
        expect = {0: [1, 2, 3],  1: [2, 3, 4],  2: [3, 4],  3: [4],  4: [7],  7: [8, 9, 10],  8: [9, 10, 11],  9: [10, 11],  10: [11],  11: [14],  14: [17],  17: [18, 19, 20],  18: [19, 20],  19: [20],  20: [23],  23: [24, 25],  24: [25],  25: [28],  28: [31],  31: [32, 33, 34],  32: [33, 34, 35],  33: [34, 35],  34: [35],  35: [38],  38: [39],  39: [42],  42: [45],  45: [46, 47, 48],  46: [47, 48, 49],  47: [48, 49],  48: [49],  49: [52]}
        self.assertEqual(mapping,expect)

    def test_count(self):
        adapters = [16,10,15,5,1,11,7,19,6,12,4]
        mapping = {}
        day10.build_map(adapters,mapping)
        cache = {}
        day10.adapter_to_count(mapping,0,cache)
        self.assertEqual(cache[0],8)
        expect = {0: 8, 1: 8, 4: 8, 5: 4, 6: 2, 7: 2, 10: 2, 11: 1, 12: 1, 15: 1, 16: 1, 19: 1}
        self.assertEqual(cache,expect)

    def test_count_large(self):
        adapters = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]
        mapping = {}
        day10.build_map(adapters,mapping)
        cache = {}
        day10.adapter_to_count(mapping,0,cache)
        self.assertEqual(cache[0],19208)
        


if __name__=='__main__':
    unittest.main()