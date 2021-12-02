import unittest

import day1

class TestDepths(unittest.TestCase):
	def test_increases(self):
		depths = [199,200,208,210,200,207,240,269,260,263]
		self.assertEqual(day1.count_increases(depths),7)

	def test_increases_empty(self):
		depths = []
		self.assertEqual(day1.count_increases(depths),0)

	def test_increases_all_equal(self):
		depths = [1,1,1,1,1,1,1,1,1,1,1]
		self.assertEqual(day1.count_increases(depths),0)

	def test_increases_decreasinf(self):
		depths = [10,9,8,7,6,5,4,3,2,1,0]
		self.assertEqual(day1.count_increases(depths),0)

	def test_windows(self):
		depths = [199,200,208,210,200,207,240,269,260,263]
		expect = [607, 618, 618, 617, 647, 716, 769, 792]
		self.assertEqual(day1.make_windows(depths),expect)

	def test_windows_too_short(self):
		expect = []
		depths = []
		self.assertEqual(day1.make_windows(depths), expect)
		depths = [0]
		self.assertEqual(day1.make_windows(depths), expect)
		depths = [0, 1]
		self.assertEqual(day1.make_windows(depths), expect)
		depths = [0,1,2]
		expect = [3]
		self.assertEqual(day1.make_windows(depths), expect)

if __name__=='__main__':
    unittest.main()
