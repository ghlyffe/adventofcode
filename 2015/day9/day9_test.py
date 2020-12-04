import day9
import unittest

class TestTSP(unittest.TestCase):
    def test_example(self):
        lines = ["London to Dublin = 464","London to Belfast = 518","Dublin to Belfast = 141"]
        g = day9.Graph()
        for l in lines:
            g.parse_line(l)
        self.assertEqual(g._Graph__nodes,["London","Dublin","Belfast"])
        self.assertEqual(g.sorted_perms()[0],("London","Dublin","Belfast"))
        self.assertEqual(g.length_for_perm(g.sorted_perms()[0]),605)

if __name__=='__main__':
    unittest.main()