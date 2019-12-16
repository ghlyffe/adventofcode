#!/usr/bin/python3

import unittest
import FeedbackMachine
import Interpreter

from Opcode import *

class TestFeedback(unittest.TestCase):
	def test_feedback_opcode(self):
		f = FeedbackMachine.FeedbackOutputFactory()
		i2 = Interpreter.Interpreter([],{},[])
		i = Interpreter.Interpreter([4,3,99,7],{4:f.construct,99:Halt})
		f.set_outerpreter(i2)
		i.run()
		outputs = i2._Interpreter__inputs
		self.assertEqual(outputs, [7])
	
	def test_feedback_and_fork(self):
		f = FeedbackMachine.FeedbackOutputFactory(FeedbackMachine.FeedbackAndFork)
		i = Interpreter.Interpreter([4,3,99,7],{4:f.construct,99:Halt})
		i2 = Interpreter.Interpreter([])
		f.set_outerpreter(i2)
		i.run()
		outputs = i2._Interpreter__inputs
		self.assertEqual(outputs, [7])
		self.assertEqual(i.pop_output(), 7)

	def test_input_opcode(self):
		inputs = []
		tape = [3, 3, 99, 0]
		i = Interpreter.Interpreter(tape,{3:FeedbackMachine.HaltingInput,99:Halt},inputs)
		i.run()
		self.assertEqual(tape, [3, 3, 99, 0])
		inputs.append(7)
		i.run()
		self.assertEqual(tape, [3, 3, 99, 7])

class TestAocInputDay7(unittest.TestCase):
	def setUp(self):
		# Opcode 4 is generated by the FeedbackMachine
		self.ops = {1:Addition,2:Multiplication,3:FeedbackMachine.HaltingInput,5:JumpIfTrue,6:JumpIfFalse,7:LessThan,8:Equal,99:Halt}

	def test_first_code(self):
		tape = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
		fm = FeedbackMachine.FeedbackMachine(tape,self.ops)
		ret = fm.run([9,8,7,6,5])
		self.assertEqual(ret, 139629729)

	def test_second_code(self):
		tape = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
		fm = FeedbackMachine.FeedbackMachine(tape,self.ops)
		ret = fm.run([9,7,8,5,6])
		self.assertEqual(ret, 18216)

if __name__=='__main__':
	unittest.main()
