import unittest

try:
    import day12
except:
    import y2020.day12.day12 as day12

class TestFerry(unittest.TestCase):
    def test_example(self):
        instrs = ["F10","N3","F7","R90","F11"]
        f = day12.Ferry(instrs)
        self.assertTrue(f.step())
        self.assertEqual(f._Ferry__loc,[0,10,90])
        self.assertTrue(f.step())
        self.assertEqual(f._Ferry__loc,[3,10,90])
        self.assertTrue(f.step())
        self.assertEqual(f._Ferry__loc,[3,17,90])
        self.assertTrue(f.step())
        self.assertEqual(f._Ferry__loc,[3,17,180])
        self.assertTrue(f.step())
        self.assertEqual(f._Ferry__loc,[-8,17,180])
        self.assertFalse(f.step())
        self.assertEqual(f.manhattan(),25)

    def test_waypoint(self):
        instrs = ["F10","N3","F7","R90","F11"]
        f = day12.Ferry(instrs,1)
        self.assertTrue(f.step())
        self.assertEqual(f._Ferry__loc,[10,100,90])
        self.assertEqual(f._Ferry__waypoint,[1,10])
        self.assertTrue(f.step())
        self.assertEqual(f._Ferry__loc,[10,100,90])
        self.assertEqual(f._Ferry__waypoint,[4,10])
        self.assertTrue(f.step())
        self.assertEqual(f._Ferry__loc,[38,170,90])
        self.assertEqual(f._Ferry__waypoint,[4,10])
        self.assertTrue(f.step())
        self.assertEqual(f._Ferry__loc,[38,170,90])
        self.assertEqual(f._Ferry__waypoint,[-10,4])
        self.assertTrue(f.step())
        self.assertEqual(f._Ferry__loc,[-72,214,90])
        self.assertEqual(f._Ferry__waypoint,[-10,4])
        self.assertFalse(f.step())
        self.assertEqual(f.manhattan(),286)

if __name__=='__main__':
    unittest.main()