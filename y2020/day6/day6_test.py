import unittest

try:
    import day6
except:
    import y2020.day6.day6 as day6

class TestAnswerSurvery(unittest.TestCase):
    def test_examples(self):
        lines = ["abc","","a","b","c","","ab","ac","","a","a","a","a","","b"]
        res = day6.parse_lines(lines)
        self.assertEqual(len(res),5)
        self.assertEqual(len(res[0]),3)
        self.assertEqual(len(res[1]),3)
        self.assertEqual(len(res[2]),3)
        self.assertEqual(len(res[3]),1)
        self.assertEqual(len(res[4]),1)
        self.assertEqual(day6.count_resps(res),11)

    def test_intersect(self):
        lines = ["abc","","a","b","c","","ab","ac","","a","a","a","a","","b"]
        res = day6.parse_lines(lines,True)
        self.assertEqual(len(res),5)
        self.assertEqual(len(res[0]),3)
        self.assertEqual(len(res[1]),0)
        self.assertEqual(len(res[2]),1)
        self.assertEqual(len(res[3]),1)
        self.assertEqual(len(res[4]),1)
        self.assertEqual(day6.count_resps(res),6)

if __name__=='__main__':
    unittest.main()