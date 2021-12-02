import unittest
import day2

class TestTurtleSub(unittest.TestCase):
	def test_parse(self):
		ts = day2.TurtleSub([])
		self.assertEqual(ts.parse('forward 5'),(5,0))
		self.assertEqual(ts.parse('down 3'),(0,3))
		self.assertEqual(ts.parse('up 2'),(0,-2))

	def test_apply(self):
		ts = day2.TurtleSub([])
		self.assertEqual(ts._TurtleSub__pos,(0,0))
		ts.apply((5,0))
		self.assertEqual(ts._TurtleSub__pos,(5,0))
		ts.apply((0,3))
		self.assertEqual(ts._TurtleSub__pos,(5,3))
		ts.apply((0,-2))
		self.assertEqual(ts._TurtleSub__pos,(5,1))

	def test_example(self):
		lines = ['forward 5','down 5','forward 8','up 3','down 8','forward 2']
		ts = day2.TurtleSub(lines)
		self.assertEqual(ts.run(),(15,10))

	def test_aim_apply(self):
		ats = day2.AimedTurtleSub([])
		p = ats.apply((5,0))
		self.assertEqual(p,(5,0))
		p = ats.apply((0,3))
		self.assertEqual(p,(5,0))
		p = ats.apply((5,0))
		self.assertEqual(p,(10,15))
		p = ats.apply((0,-2))
		self.assertEqual(p,(10,15))
		p = ats.apply((5,0))
		self.assertEqual(p,(15,20))


if __name__=='__main__':
	unittest.main()
