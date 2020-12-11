import unittest

import day11

class TestCA(unittest.TestCase):
    def test_example(self):
        rules = day11.part_1_rules()
        start = ["L.LL.LL.LL","LLLLLLL.LL","L.L.L..L..","LLLL.LL.LL","L.LL.LL.LL","L.LLLLL.LL","..L.L.....","LLLLLLLLLL","L.LLLLLL.L","L.LLLLL.LL"]
        ca = day11.Automaton(day11.lines_to_grid(start),rules)
        expect = day11.lines_to_grid(["#.##.##.##","#######.##","#.#.#..#..","####.##.##","#.##.##.##","#.#####.##","..#.#.....","##########","#.######.#","#.#####.##"])
        ca.generation()
        self.assertEqual(expect,ca.grid())
        expect = day11.lines_to_grid(["#.LL.L#.##","#LLLLLL.L#","L.L.L..L..","#LLL.LL.L#","#.LL.LL.LL","#.LLLL#.##","..L.L.....","#LLLLLLLL#","#.LLLLLL.L","#.#LLLL.##"])
        ca.generation()
        self.assertEqual(expect,ca.grid())
        expect = day11.lines_to_grid(["#.##.L#.##","#L###LL.L#","L.#.#..#..","#L##.##.L#","#.##.LL.LL","#.###L#.##","..#.#.....","#L######L#","#.LL###L.L","#.#L###.##"])
        ca.generation()
        self.assertEqual(expect,ca.grid())
        expect = day11.lines_to_grid(["#.#L.L#.##","#LLL#LL.L#","L.L.L..#..","#LLL.##.L#","#.LL.LL.LL","#.LL#L#.##","..L.L.....","#L#LLLL#L#","#.LLLLLL.L","#.#L#L#.##"])
        ca.generation()
        self.assertEqual(expect,ca.grid())
        expect = day11.lines_to_grid(["#.#L.L#.##","#LLL#LL.L#","L.#.L..#..","#L##.##.L#","#.#L.LL.LL","#.#L#L#.##","..L.L.....","#L#L##L#L#","#.LLLLLL.L","#.#L#L#.##"])
        ca.generation()
        self.assertEqual(expect,ca.grid())
        self.assertEqual(37,ca.count_occupied())

    def test_run_to_stable(self):
        rules = day11.part_1_rules()
        start = ["L.LL.LL.LL","LLLLLLL.LL","L.L.L..L..","LLLL.LL.LL","L.LL.LL.LL","L.LLLLL.LL","..L.L.....","LLLLLLLLLL","L.LLLLLL.L","L.LLLLL.LL"]
        ca = day11.Automaton(day11.lines_to_grid(start),rules)
        ca.run_to_stable()
        expect = day11.lines_to_grid(["#.#L.L#.##","#LLL#LL.L#","L.#.L..#..","#L##.##.L#","#.#L.LL.LL","#.#L#L#.##","..L.L.....","#L#L##L#L#","#.LLLLLL.L","#.#L#L#.##"])
        self.assertEqual(expect,ca.grid())
        self.assertEqual(37,ca.count_occupied())

    def test_visibility_stepwise(self):
        rules = day11.part_2_rules()
        start = ["L.LL.LL.LL","LLLLLLL.LL","L.L.L..L..","LLLL.LL.LL","L.LL.LL.LL","L.LLLLL.LL","..L.L.....","LLLLLLLLLL","L.LLLLLL.L","L.LLLLL.LL"]
        ca = day11.Automaton(day11.lines_to_grid(start),rules,day11.visibility_neighbourhood)
        expect = day11.lines_to_grid(["#.##.##.##","#######.##","#.#.#..#..","####.##.##","#.##.##.##","#.#####.##","..#.#.....","##########","#.######.#","#.#####.##"])
        ca.generation()
        self.assertEqual(expect,ca.grid())
        expect = day11.lines_to_grid(["#.LL.LL.L#","#LLLLLL.LL","L.L.L..L..","LLLL.LL.LL","L.LL.LL.LL","L.LLLLL.LL","..L.L.....","LLLLLLLLL#","#.LLLLLL.L","#.LLLLL.L#"])
        ca.generation()
        self.assertEqual(expect,ca.grid())
        expect = day11.lines_to_grid(["#.L#.##.L#","#L#####.LL","L.#.#..#..","##L#.##.##","#.##.#L.##","#.#####.#L","..#.#.....","LLL####LL#","#.L#####.L","#.L####.L#"])
        ca.generation()
        self.assertEqual(expect,ca.grid())
        expect = day11.lines_to_grid(["#.L#.L#.L#","#LLLLLL.LL","L.L.L..#..","##LL.LL.L#","L.LL.LL.L#","#.LLLLL.LL","..L.L.....","LLLLLLLLL#","#.LLLLL#.L","#.L#LL#.L#"])
        ca.generation()
        self.assertEqual(expect,ca.grid())
        expect = day11.lines_to_grid(["#.L#.L#.L#","#LLLLLL.LL","L.L.L..#..","##L#.#L.L#","L.L#.#L.L#","#.L####.LL","..#.#.....","LLL###LLL#","#.LLLLL#.L","#.L#LL#.L#"])
        ca.generation()
        self.assertEqual(expect,ca.grid())
        expect = day11.lines_to_grid(["#.L#.L#.L#","#LLLLLL.LL","L.L.L..#..","##L#.#L.L#","L.L#.LL.L#","#.LLLL#.LL","..#.L.....","LLL###LLL#","#.LLLLL#.L","#.L#LL#.L#"])
        ca.generation()
        self.assertEqual(expect,ca.grid())
        self.assertEqual(26,ca.count_occupied())

    def test_visibility(self):
        rules = day11.part_2_rules()
        start = ["L.LL.LL.LL","LLLLLLL.LL","L.L.L..L..","LLLL.LL.LL","L.LL.LL.LL","L.LLLLL.LL","..L.L.....","LLLLLLLLLL","L.LLLLLL.L","L.LLLLL.LL"]
        ca = day11.Automaton(day11.lines_to_grid(start),rules,day11.visibility_neighbourhood)
        ca.run_to_stable()
        expect = day11.lines_to_grid(["#.L#.L#.L#","#LLLLLL.LL","L.L.L..#..","##L#.#L.L#","L.L#.LL.L#","#.LLLL#.LL","..#.L.....","LLL###LLL#","#.LLLLL#.L","#.L#LL#.L#"])
        self.assertEqual(expect,ca.grid())
        self.assertEqual(26,ca.count_occupied())

    def test_glider(self):
        rules = day11.gol_rules()
        start = ["..........", \
                 "..........", \
                 "..........", \
                 "....#.....", \
                 ".....#....", \
                 "...###....", \
                 "..........", \
                 "..........", \
                 "..........", \
                 ".........." ]
        expet = ["..........", \
                 "..........", \
                 "..........", \
                 "..........", \
                 ".....#....", \
                 "......#...", \
                 "....###...", \
                 "..........", \
                 "..........", \
                 ".........." ]
        ca = day11.Automaton(day11.lines_to_grid(start),rules)
        ca.run(4)
        self.assertEqual(ca.grid(),day11.lines_to_grid(expet))

if __name__=='__main__':
    unittest.main()