import day7
import unittest

class TestCircuits(unittest.TestCase):
    def test_small_example(self):
        c = day7.Circuit()
        input_lines = ["123 -> x","456 -> y","x AND y -> d","x OR y -> e","x LSHIFT 2 -> f","y RSHIFT 2 -> g","NOT x -> h","NOT y -> i"]
        for l in input_lines:
            c.parse_line(l)
        self.assertEqual(c.get_output_for("d"),72)
        self.assertEqual(c.get_output_for("e"),507)
        self.assertEqual(c.get_output_for("f"),492)
        self.assertEqual(c.get_output_for("g"),114)
        self.assertEqual(c.get_output_for("h"),65412)
        self.assertEqual(c.get_output_for("i"),65079)
        self.assertEqual(c.get_output_for("x"),123)
        self.assertEqual(c.get_output_for("y"),456)

    def test_lazy(self):
        c = day7.Circuit()
        input_lines = ["b AND c -> a", "9 -> b", "3 -> c"]
        for l in input_lines:
            c.parse_line(l)
        self.assertEqual(c.get_output_for("a"), 9&3)
        self.assertEqual(c.get_output_for("b"), 9)
        self.assertEqual(c.get_output_for("c"), 3)

    def test_specific_string(self):
        c = day7.Circuit()
        input_lines = ["lx -> a", "9 -> lx"]
        for l in input_lines:
            c.parse_line(l)
        self.assertEqual(c.get_output_for("a"), 9)
        self.assertEqual(c.get_output_for("lx"), 9)

    def test_override(self):
        c = day7.Circuit()
        input_lines = ["123 -> x","456 -> y","x AND y -> d","x OR y -> e","x LSHIFT 2 -> f","y RSHIFT 2 -> g","NOT x -> h","NOT y -> i"]
        for l in input_lines:
            c.parse_line(l)
        c.get_output_for("d")
        c.get_output_for("e")
        c.get_output_for("f")
        c.get_output_for("g")
        c.get_output_for("h")
        c.get_output_for("i")
        c.get_output_for("x")
        c.get_output_for("y")
        c.override_wire("x",234)
        self.assertEqual(c.get_output_for("d"),234&456)
        self.assertEqual(c.get_output_for("e"),234|456)
        self.assertEqual(c.get_output_for("f"),(234<<2)&0xFFFF)
        self.assertEqual(c.get_output_for("g"),114)
        self.assertEqual(c.get_output_for("h"),(~234)&0xFFFF)
        self.assertEqual(c.get_output_for("i"),65079)
        self.assertEqual(c.get_output_for("x"),234)
        self.assertEqual(c.get_output_for("y"),456)


if __name__=='__main__':
    unittest.main()