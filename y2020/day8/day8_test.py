import unittest
try:
    import day8
except:
    import y2020.day8.day8 as day8

class TestInterpreter(unittest.TestCase):
    def test_first_example(self):
        lines = ["nop +0","acc +1","jmp +4","acc +3","jmp -3","acc -99","acc +1","jmp -4","acc +6"]
        interpreter = day8.parse_lines(lines)
        self.assertEqual(interpreter.run(),5)
        self.assertEqual(interpreter._Interpreter__history,[0,1,2,6,7,3,4,1])

    def test_self_fix(self):
        lines = ["nop +0","acc +1","jmp +4","acc +3","jmp -3","acc -99","acc +1","jmp -4","acc +6"]
        interpreter = day8.parse_lines(lines)
        acc = interpreter.fix_self()
        self.assertEqual(interpreter._Interpreter__history,[0,1,2,6,7,8,9])
        self.assertEqual(acc,8)

if __name__=='__main__':
    unittest.main()