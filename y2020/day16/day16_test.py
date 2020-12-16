import unittest

try:
    import day16
except:
    import y2020.day16.day16 as day16

class TestTicketChecker(unittest.TestCase):
    def test_apply_rules(self):
        rules = [day16.Rule(i) for i in ["class: 1-3 or 5-7","row: 6-11 or 33-44","seat: 13-40 or 45-50"]]
        tickets = [[7,3,47],[40,4,50],[55,2,20],[38,6,12]]
        self.assertTrue(rules[0].apply(tickets[0][0]))
        self.assertTrue(rules[0].apply(tickets[0][1]))
        self.assertFalse(rules[0].apply(tickets[0][2]))

        self.assertFalse(rules[0].apply(tickets[1][0]))
        self.assertFalse(rules[0].apply(tickets[1][1]))
        self.assertFalse(rules[0].apply(tickets[1][2]))

        self.assertFalse(rules[0].apply(tickets[2][0]))
        self.assertTrue(rules[0].apply(tickets[2][1]))
        self.assertFalse(rules[0].apply(tickets[2][2]))

        self.assertFalse(rules[0].apply(tickets[3][0]))
        self.assertTrue(rules[0].apply(tickets[3][1]))
        self.assertFalse(rules[0].apply(tickets[3][2]))

        self.assertTrue(rules[1].apply(tickets[0][0]))
        self.assertFalse(rules[1].apply(tickets[0][1]))
        self.assertFalse(rules[1].apply(tickets[0][2]))

        self.assertTrue(rules[1].apply(tickets[1][0]))
        self.assertFalse(rules[1].apply(tickets[1][1]))
        self.assertFalse(rules[1].apply(tickets[1][2]))

        self.assertFalse(rules[1].apply(tickets[2][0]))
        self.assertFalse(rules[1].apply(tickets[2][1]))
        self.assertFalse(rules[1].apply(tickets[2][2]))

        self.assertTrue(rules[1].apply(tickets[3][0]))
        self.assertTrue(rules[1].apply(tickets[3][1]))
        self.assertFalse(rules[1].apply(tickets[3][2]))

        self.assertFalse(rules[2].apply(tickets[0][0]))
        self.assertFalse(rules[2].apply(tickets[0][1]))
        self.assertTrue(rules[2].apply(tickets[0][2]))

        self.assertTrue(rules[2].apply(tickets[1][0]))
        self.assertFalse(rules[2].apply(tickets[1][1]))
        self.assertTrue(rules[2].apply(tickets[1][2]))

        self.assertFalse(rules[2].apply(tickets[2][0]))
        self.assertFalse(rules[2].apply(tickets[2][1]))
        self.assertTrue(rules[2].apply(tickets[2][2]))

        self.assertTrue(rules[2].apply(tickets[3][0]))
        self.assertFalse(rules[2].apply(tickets[3][1]))
        self.assertFalse(rules[2].apply(tickets[3][2]))

    def test_checker(self):
        rules = [day16.Rule(i) for i in ["class: 1-3 or 5-7","row: 6-11 or 33-44","seat: 13-40 or 45-50"]]
        tickets = [(7,3,47),(40,4,50),(55,2,20),(38,6,12)]
        checker = day16.Checker(rules)
        out = checker.invalid_tickets(tickets)
        self.assertEqual(out,{(40,4,50):[4],(55,2,20):[55],(38,6,12):[12]})
        self.assertEqual(checker.error_rate(tickets),71)

    def test_example(self):
        lines = ["class: 1-3 or 5-7","row: 6-11 or 33-44","seat: 13-40 or 45-50","","your ticket:","7,1,14","","nearby tickets:","7,3,47","40,4,50","55,2,20","38,6,12"]
        checker,own,others = day16.parse_lines(lines)
        out = checker.invalid_tickets(others)
        self.assertEqual(out,{(40,4,50):[4],(55,2,20):[55],(38,6,12):[12]})
        self.assertEqual(checker.error_rate(others),71)


    def test_possible(self):
        lines = ["class: 0-1 or 4-19","row: 0-5 or 8-19","seat: 0-13 or 16-19","","your ticket:","11,12,13","","nearby tickets:","3,9,18","15,1,5","5,14,9"]
        checker,own,others = day16.parse_lines(lines)
        out = checker.find_fields(others)
        expect = {0:"row",1:"class",2:"seat"}
        self.assertEqual(out,expect)
        self.assertEqual(day16.field_product(own,out,'r'),11)
        self.assertEqual(day16.field_product(own,out,'c'),12)
        self.assertEqual(day16.field_product(own,out,'s'),13)

if __name__=='__main__':
    unittest.main()