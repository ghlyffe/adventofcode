import unittest
try:
    import day7
except:
    import y2020.day7.day7 as day7

class TestBagOfHolding(unittest.TestCase):
    def test_parse_example(self):
        lines = ["light red bags contain 1 bright white bag, 2 muted yellow bags.","dark orange bags contain 3 bright white bags, 4 muted yellow bags.","bright white bags contain 1 shiny gold bag.","muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.","shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.","dark olive bags contain 3 faded blue bags, 4 dotted black bags.","vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.","faded blue bags contain no other bags.","dotted black bags contain no other bags."]
        bags,contains,contained_by = day7.parse_lines(lines)
        self.assertEqual(len(bags),9)
        self.assertEqual(contains['light red'],{'bright white':1,'muted yellow':2})
        self.assertEqual(contains['dark orange'],{'bright white':3,'muted yellow':4})
        self.assertEqual(contains['bright white'],{'shiny gold':1})
        self.assertEqual(contains['muted yellow'],{'shiny gold':2,'faded blue':9})
        self.assertEqual(contains['shiny gold'],{'dark olive':1,'vibrant plum':2})
        self.assertEqual(contains['dark olive'],{'faded blue':3,'dotted black':4})
        self.assertEqual(contains['vibrant plum'],{'faded blue':5,'dotted black':6})
        self.assertEqual(contains['faded blue'],{})
        self.assertEqual(contains['dotted black'],{})
        self.assertEqual(len(contained_by['light red']),0)
        self.assertEqual(len(contained_by['dark orange']),0)
        self.assertEqual(contained_by['bright white'],set(['light red','dark orange']))
        self.assertEqual(contained_by['muted yellow'],set(['light red','dark orange']))
        self.assertEqual(contained_by['shiny gold'],set(['bright white','muted yellow']))
        self.assertEqual(contained_by['dark olive'],set(['shiny gold']))
        self.assertEqual(contained_by['vibrant plum'],set(['shiny gold']))
        self.assertEqual(contained_by['faded blue'],set(['muted yellow','dark olive','vibrant plum']))
        self.assertEqual(contained_by['dotted black'],set(['vibrant plum','dark olive']))

    def test_find_contains(self):
        lines = ["light red bags contain 1 bright white bag, 2 muted yellow bags.","dark orange bags contain 3 bright white bags, 4 muted yellow bags.","bright white bags contain 1 shiny gold bag.","muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.","shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.","dark olive bags contain 3 faded blue bags, 4 dotted black bags.","vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.","faded blue bags contain no other bags.","dotted black bags contain no other bags."]
        bags,contains,contained_by = day7.parse_lines(lines)
        res = day7.find_contains('shiny gold',contained_by)
        self.assertEqual(res,set(['light red','dark orange','bright white','muted yellow']))

    def test_must_contain_first(self):
        lines = ["light red bags contain 1 bright white bag, 2 muted yellow bags.","dark orange bags contain 3 bright white bags, 4 muted yellow bags.","bright white bags contain 1 shiny gold bag.","muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.","shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.","dark olive bags contain 3 faded blue bags, 4 dotted black bags.","vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.","faded blue bags contain no other bags.","dotted black bags contain no other bags."]
        bags,contains,contained_by = day7.parse_lines(lines)
        res = day7.must_contain('shiny gold', contains)
        self.assertEqual(res,32)

    def test_must_contain_second(self):
        lines = ["shiny gold bags contain 2 dark red bags.","dark red bags contain 2 dark orange bags.","dark orange bags contain 2 dark yellow bags.","dark yellow bags contain 2 dark green bags.","dark green bags contain 2 dark blue bags.","dark blue bags contain 2 dark violet bags.","dark violet bags contain no other bags."]
        bags,contains,contained_by = day7.parse_lines(lines)
        res = day7.must_contain('shiny gold', contains)
        self.assertEqual(res,126)

if __name__=='__main__':
    unittest.main()