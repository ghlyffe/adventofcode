import unittest
try:
    import day8
except:
    import y2015.day8.day8 as day8

class TestReprs(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(day8.count_diff_escape('""'),4)
        self.assertEqual(day8.count_diff_escape('"abc"'),4)
        self.assertEqual(day8.count_diff_escape('"aaa\\"aaa"'),6)
        self.assertEqual(day8.count_diff_escape('"\\x27"'),5)

if __name__=='__main__':
    unittest.main()