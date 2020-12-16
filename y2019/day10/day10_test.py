#!/usr/bin/python3

import unittest

try:
    from day10 import *
except:
    from y2019.day10.day10 import *

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

	def test_transpose_with_null(self):
		ll = [[0,1,2],[3],[4,5]]
		out = [[0,3,4],[1,None,5],[2,None,None]]
		self.assertEqual(transpose(ll,True),out)

	def test_find_nth(self):
		ll = [[0,1,2],[3,None,4],[5,None,None]]
		self.assertEqual([i for l in ll for i in l if i is not None],[0,1,2,3,4,5])
		for i in range(6):
			self.assertEqual(find_nth_asteroid(ll,i+1),i)

	def test_angles_small(self):
		base_loc = (3,8)
		self.assertEqual(True,True)

	def test_vaporisations_small(self):
		in_map = transpose(transpose([".#....#####...#..","##...##.#####..##","##...#...#.#####.","..#.........###..","..#.#.....#....##"]))
		pts = map_to_points(in_map)
		base_loc = (3,8)
		order = [i for l in transpose(partition_by_angle(pts,base_loc), True) for i in l if i]
		expect = [(1,8),(0,9),(1,9),(0,10),(2,9),(1,11),(1,12),(2,11),(1,15),(2,12),(2,13),(2,14),(2,15),(3,12),(4,16),(4,15),(4,10),(4,4),(4,2),(3,2),(2,0),(2,1),(1,0),(1,1),(2,5),(0,1),(1,5),(1,6),(0,6),(0,7),(0,8),(1,10),(0,14),(1,16),(3,13),(3,14)]
		self.assertEqual(order,expect)

	def test_vaporisations_large(self):
		in_map = transpose(transpose([".#..##.###...#######","##.############..##.",".#.######.########.#",".###.#######.####.#.","#####.##.#.##.###.##","..#####..#.#########","####################","#.####....###.#.#.##","##.#################","#####.##.###..####..","..######..##.#######","####.##.####...##..#",".#####..#.######.###","##...#.##########...","#.##########.#######",".####.#.###.###.#.##","....##.##.###..#####",".#.#.###########.###","#.#.#.#####.####.###","###.##.####.##.#..##"]))
		base_loc = (13,11)

		self.assertEqual(calc_angle((0,16),(13,11)),0.36717)

		self.assertEqual(nth_asteroid_vaporised(in_map,base_loc,1),(12,11))
		self.assertEqual(nth_asteroid_vaporised(in_map,base_loc,2),(1,12))
		self.assertEqual(nth_asteroid_vaporised(in_map,base_loc,3),(2,12))
		self.assertEqual(nth_asteroid_vaporised(in_map,base_loc,10),(8,12))
		self.assertEqual(nth_asteroid_vaporised(in_map,base_loc,20),(0,16))
		self.assertEqual(nth_asteroid_vaporised(in_map,base_loc,50),(9,16))
		self.assertEqual(nth_asteroid_vaporised(in_map,base_loc,100),(16,10))
		self.assertEqual(nth_asteroid_vaporised(in_map,base_loc,199),(6,9))
		self.assertEqual(nth_asteroid_vaporised(in_map,base_loc,200),(2,8))
		self.assertEqual(nth_asteroid_vaporised(in_map,base_loc,201),(9,10))
		self.assertEqual(nth_asteroid_vaporised(in_map,base_loc,299),(1,11))
		

if __name__=='__main__':
	unittest.main()
