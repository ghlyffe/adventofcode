import unittest

import day10

class TestAdapters(unittest.TestCase):
    def test_three_in_list(self):
        adapters = day10.sort_and_reverse([1,2,3,4])
        arrangements = day10.find_arrangements(adapters,[[max(adapters)+3]])
        self.assertIn([7,4,3,2,1],arrangements)
        self.assertIn([7,4,3,2],arrangements)
        self.assertIn([7,4,3],arrangements)
        
    def test_arrangements_large(self):
        adapters = day10.sort_and_reverse([28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3])
        arrangements = day10.find_arrangements(adapters,[[max(adapters)+3]])
        self.assertIn(day10.sort_and_reverse([1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, 52]),arrangements)
        self.assertIn(day10.sort_and_reverse([1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 49, 52]),arrangements)
        self.assertIn(day10.sort_and_reverse([1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 48, 49, 52]),arrangements)
        self.assertIn(day10.sort_and_reverse([1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 49, 52]),arrangements)
        self.assertIn(day10.sort_and_reverse([1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 47, 48, 49, 52]),arrangements)
        self.assertIn(day10.sort_and_reverse([3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45, 46, 48, 49, 52]),arrangements)
        self.assertIn(day10.sort_and_reverse([3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45, 46, 49, 52]),arrangements)
        self.assertIn(day10.sort_and_reverse([3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45, 47, 48, 49, 52]),arrangements)
        self.assertIn(day10.sort_and_reverse([3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45, 47, 49, 52]),arrangements)
        self.assertIn(day10.sort_and_reverse([3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45, 48, 49, 52]),arrangements)
        self.assertEqual(len(arrangements),19208)

if __name__=='__main__':
    unittest.main()