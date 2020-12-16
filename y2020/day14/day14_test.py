import unittest

try:
    import day14
except:
    import y2020.day14.day14 as day14

class TestMasks(unittest.TestCase):
    def test_example_mask_only(self):
        mask = day14.Mask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")
        mem = {}
        mask.apply(mem,8,11)
        self.assertEqual(mem[8],73)
        mask.apply(mem,7,101)
        self.assertEqual(mem[7],101)
        mask.apply(mem,8,0)
        self.assertEqual(mem[8],64)
        mask.apply(mem,9,2)
        self.assertEqual(mem[9],64)

    def test_example(self):
        lines = ["mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X","mem[8] = 11","mem[7] = 101","mem[8] = 0"]
        pgm = day14.parse_lines(lines)
        pgm.run()
        self.assertEqual(pgm.total(),165)

    def test_memmask_masking(self):
        mem = {}
        mask1 = day14.MemMask("000000000000000000000000000000X1001X")
        mask1.apply(mem,42,100)
        self.assertEqual(mem[26],100)
        self.assertEqual(mem[27],100)
        self.assertEqual(mem[58],100)
        self.assertEqual(mem[59],100)
        mask2 = day14.MemMask("00000000000000000000000000000000X0XX")
        mask2.apply(mem,26,1)
        self.assertEqual(mem[16],1)
        self.assertEqual(mem[17],1)
        self.assertEqual(mem[18],1)
        self.assertEqual(mem[19],1)
        self.assertEqual(mem[24],1)
        self.assertEqual(mem[25],1)
        self.assertEqual(mem[26],1)
        self.assertEqual(mem[27],1)

    def test_memmask_example(self):
        lines = ["mask = 000000000000000000000000000000X1001X","mem[42] = 100","mask = 00000000000000000000000000000000X0XX","mem[26] = 1"]
        pgm = day14.parse_lines(lines,day14.MemMask)
        pgm.run()
        self.assertEqual(pgm.total(),208)



if __name__=='__main__':
    unittest.main()