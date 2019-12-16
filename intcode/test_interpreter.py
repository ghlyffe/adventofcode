#!/usr/bin/python3
import unittest

import Interpreter, Opcode

class AdditionTests(unittest.TestCase):
	def setUp(self):
		self.ops = {1: Opcode.Addition, 99: Opcode.Halt}

	def test_addition_positional(self):
		tape = [1, 1, 1, 3, 99]
		i = Interpreter.Interpreter(tape, self.ops)
		i.run()
		self.assertEqual(tape, [1,1,1,2,99])

	def test_addition_immediate(self):
		tape = [1101, 7, 9, 5, 99, 0]
		i = Interpreter.Interpreter(tape, self.ops)
		i.run()
		self.assertEqual(tape, [1101,7,9,5,99,16])

class MultiplicationTests(unittest.TestCase):
	def setUp(self):
		self.ops = {2: Opcode.Multiplication, 99: Opcode.Halt}

	def test_multiplication_positional(self):
		tape = [2, 1, 1, 3, 99]
		i = Interpreter.Interpreter(tape, self.ops)
		i.run()
		self.assertEqual(tape, [2,1,1,1,99])

	def test_multiplication_immediate(self):
		tape = [1102, 7, 9, 5, 99, 0]
		i = Interpreter.Interpreter(tape, self.ops)
		i.run()
		self.assertEqual(tape, [1102,7,9,5,99,63])

class TestInputOutput(unittest.TestCase):
	def setUp(self):
		self.ops = {1: Opcode.Addition, 3: Opcode.Input, 4: Opcode.Output, 99: Opcode.Halt}

	def test_input(self):
		tape = [3, 9, 3, 10, 1, 9, 10, 0, 99, 0, 0]
		i = Interpreter.Interpreter(tape, self.ops, [30, 4])
		i.run()
		self.assertEqual(tape, [34, 9, 3, 10, 1, 9, 10, 0, 99, 30, 4])

	def test_output(self):
		tape = [3, 5, 4, 5, 99, 0]
		i = Interpreter.Interpreter(tape, self.ops, [30])
		i.run()
		self.assertEqual(tape, [3, 5, 4, 5, 99, 30])
		self.assertEqual(i.pop_output(), 30)

class TestAocCodeDay2(unittest.TestCase):
	def setUp(self):
		self.ops = {1: Opcode.Addition, 2: Opcode.Multiplication, 99: Opcode.Halt}
	
	def test_first_code(self):
		tape = [1,9,10,3,2,3,11,0,99,30,40,50]
		i = Interpreter.Interpreter(tape, self.ops)
		i.run()
		self.assertEqual(tape, [3500,9,10,70,2,3,11,0,99,30,40,50])

	def test_second_code(self):
		tape = [1,0,0,0,99]
		i = Interpreter.Interpreter(tape, self.ops)
		i.run()
		self.assertEqual(tape, [2,0,0,0,99])

	def test_third_code(self):
		tape = [2,3,0,3,99]
		i = Interpreter.Interpreter(tape, self.ops)
		i.run()
		self.assertEqual(tape, [2,3,0,6,99])

	def test_fourth_code(self):
		tape = [2,4,4,5,99,0]
		i = Interpreter.Interpreter(tape, self.ops)
		i.run()
		self.assertEqual(tape, [2,4,4,5,99,9801])

	def test_fifth_code(self):
		tape = [1,1,1,4,99,5,6,0,99]
		i = Interpreter.Interpreter(tape, self.ops)
		i.run()
		self.assertEqual(tape, [30,1,1,4,2,5,6,0,99])

class TestAocDay5(unittest.TestCase):
	def setUp(self):
		self.ops = {1: Opcode.Addition, 2: Opcode.Multiplication, 3: Opcode.Input, 4: Opcode.Output, 5: Opcode.JumpIfTrue, 6: Opcode.JumpIfFalse, 7: Opcode.LessThan, 8: Opcode.Equal, 99: Opcode.Halt}

	def test_first_code(self):
		tape = [3,9,8,9,10,9,4,9,99,-1,8]
		i = Interpreter.Interpreter(tape, self.ops, [8])
		i.run()
		self.assertEqual(i.pop_output(), 1)

		tape = [3,9,8,9,10,9,4,9,99,-1,8]
		i = Interpreter.Interpreter(tape, self.ops, [4])
		i.run()
		self.assertEqual(i.pop_output(), 0)

	def test_second_code(self):
		tape = [3,9,7,9,10,9,4,9,99,-1,8]
		i = Interpreter.Interpreter(tape, self.ops, [4])
		i.run()
		self.assertEqual(i.pop_output(), 1)

		tape = [3,9,7,9,10,9,4,9,99,-1,8]
		i = Interpreter.Interpreter(tape, self.ops, [8])
		i.run()
		self.assertEqual(i.pop_output(), 0)

	def test_third_code(self):
		tape = [3,3,1108,-1,8,3,4,3,99]
		i = Interpreter.Interpreter(tape, self.ops, [8])
		i.run()
		self.assertEqual(i.pop_output(), 1)

		tape = [3,3,1108,-1,8,3,4,3,99]
		i = Interpreter.Interpreter(tape, self.ops, [4])
		i.run()
		self.assertEqual(i.pop_output(), 0)

	def test_fourth_code(self):
		tape = [3,3,1107,-1,8,3,4,3,99]
		i = Interpreter.Interpreter(tape, self.ops, [4])
		i.run()
		self.assertEqual(i.pop_output(), 1)

		tape = [3,3,1107,-1,8,3,4,3,99]
		i = Interpreter.Interpreter(tape, self.ops, [9])
		i.run()
		self.assertEqual(i.pop_output(), 0)

	def test_fifth_code(self):
		tape = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
		i = Interpreter.Interpreter(tape, self.ops, [4])
		i.run()
		self.assertEqual(i.pop_output(), 1)

		tape = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
		i = Interpreter.Interpreter(tape, self.ops, [0])
		i.run()
		self.assertEqual(i.pop_output(), 0)

	def test_sixth_code(self):
		tape = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
		i = Interpreter.Interpreter(tape, self.ops, [4])
		i.run()
		self.assertEqual(i.pop_output(), 1)

		tape = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
		i = Interpreter.Interpreter(tape, self.ops, [0])
		i.run()
		self.assertEqual(i.pop_output(), 0)

	def test_seventh_code(self):
		tape = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,	999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
		i = Interpreter.Interpreter(tape, self.ops, [4])
		i.run()
		self.assertEqual(i.pop_output(), 999)

		tape = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,	999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
		i = Interpreter.Interpreter(tape, self.ops, [8])
		i.run()
		self.assertEqual(i.pop_output(), 1000)

		i = Interpreter.Interpreter(tape, self.ops, [13])
		i.run()
		self.assertEqual(i.pop_output(), 1001)

if __name__=='__main__':
	unittest.main()
