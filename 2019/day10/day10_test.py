#!/usr/bin/python3

import unittest

from day10 import *

class TestMapMods(unittest.TestCase):
	def test_transpose(self):
		lst = [[1,2,3],[4,5,6],[7,8,9]]
		self.assertEqual(transpose(lst),[[1,4,7],[2,5,8],[3,6,9]])

	def test_map_to_points(self):
		in_map = [".#..#",".....","#####","....#","...##"]
		self.assertEqual(map_to_points(in_map),sorted([(0,1),(0,4),(2,0),(2,1),(2,2),(2,3),(2,4),(3,4),(4,3),(4,4)]))

	def test_map_to_points_empty(self):
		in_map = [".....",".....",".....",".....","....."]
		self.assertEqual(map_to_points(in_map),[])

	def test_map_to_points_one(self):
		in_map = [".....","...#.",".....",".....","....."]
		self.assertEqual(map_to_points(in_map),[(1,3)])

	def test_map_to_points_two(self):
		in_map = [".#...",".....",".....",".....","..#.."]
		self.assertEqual(map_to_points(in_map),[(0,1),(4,2)])

	def test_mask_from_pair(self):
		import copy
		in_map = transpose(transpose([".#..#",".....","#####","....#","...##"]))
		out_map = copy.copy(in_map)
		out_map = mask_from_pair((2,2),(2,3),out_map)
		self.assertEqual(out_map,transpose(transpose([".#..#",".....","####X","....#","...##"])))

		out_map = mask_from_pair((2,2),(2,1),out_map)
		self.assertEqual(out_map,transpose(transpose([".#..#",".....","X###X","....#","...##"])))

		out_map = mask_from_pair((0,1),(2,3),out_map)
		self.assertEqual(out_map,transpose(transpose([".#..#",".....","X###X","....X","...##"])))

	def test_counting(self):
		in_map = transpose(transpose([".#..#",".....","#####","....#","...##"]))
		self.assertEqual(count_asteroids(in_map),10)
		in_map = transpose(transpose([".#..#",".....","X###X","....X","...##"]))
		self.assertEqual(count_asteroids(in_map),7)

	def test_all_counts_individual(self):
		in_map = transpose(transpose([".#..#",".....","#####","....#","...##"]))
		asts = map_to_points(in_map)
	
		self.assertEqual(seen_by_asteroid(asts,asts.index((0,1)),in_map),7)
		self.assertEqual(seen_by_asteroid(asts,asts.index((0,4)),in_map),7)
		self.assertEqual(seen_by_asteroid(asts,asts.index((2,0)),in_map),6)
		self.assertEqual(seen_by_asteroid(asts,asts.index((2,1)),in_map),7)
		self.assertEqual(seen_by_asteroid(asts,asts.index((2,2)),in_map),7)
		self.assertEqual(seen_by_asteroid(asts,asts.index((2,3)),in_map),7)
		self.assertEqual(seen_by_asteroid(asts,asts.index((2,4)),in_map),5)
		self.assertEqual(seen_by_asteroid(asts,asts.index((3,4)),in_map),7)
		self.assertEqual(seen_by_asteroid(asts,asts.index((4,3)),in_map),8)
		self.assertEqual(seen_by_asteroid(asts,asts.index((4,4)),in_map),7)

	def test_all_counts(self):
		in_map = transpose(transpose([".#..#",".....","#####","....#","...##"]))
		counts = {(0,1):7,(0,4):7,(2,0):6,(2,1):7,(2,2):7,(2,3):7,(2,4):5,(3,4):7,(4,3):8,(4,4):7}
		self.assertEqual(map_to_counts(in_map),counts)

if __name__=='__main__':
	unittest.main()
