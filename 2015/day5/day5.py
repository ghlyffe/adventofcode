#!/usr/bin/python3

vowels = "aeiou"
bad_seqs = ["ab", "cd", "pq", "xy"]

def check_doubles(instr):
	"""
	>>> check_doubles("abcde")
	False
	>>> check_doubles("aabcd")
	True
	>>> check_doubles("abcdd")
	True
	"""
	for i in range(len(instr)-1):
		if instr[i] == instr[i+1]:
			return True
	return False

def check_doubles_digraph(instr):
	"""
	>>> check_doubles_digraph("xyxy")
	True
	>>> check_doubles_digraph("aabcdefgaa")
	True
	>>> check_doubles_digraph("aaa")
	False
	"""
	for i in range(len(instr)-3):
		dg = instr[i:i+2]
		if dg in instr[i+2:]:
			return True
	return False

def check_spaced_double(instr):
	"""
	>>> check_spaced_double("xyx")
	True
	>>> check_spaced_double("abcdefeghi")
	True
	>>> check_spaced_double("aaa")
	True
	>>> check_spaced_double("uurcxstgmygtbstg")
	False
	"""
	for i in range(len(instr)-2):
		if instr[i] == instr[i+2]:
			return True
	return False

def check_vowels(instr):
	"""
	>>> check_vowels("aei")
	True
	>>> check_vowels("aef")
	False
	>>> check_vowels("aaa")
	True
	"""
	return len([i for i in map(lambda x: x in vowels, instr) if i]) >= 3

def check_bad_seqs(instr):
	"""
	>>> check_bad_seqs("asdfasdf")
	True
	>>> check_bad_seqs("ahjkaboijvs")
	False
	"""
	return not any([i in instr for i in bad_seqs])

def check_string(instr):
	return check_doubles(instr) and check_vowels(instr) and check_bad_seqs(instr)

def check_string_redux(instr):
	return check_doubles_digraph(instr) and check_spaced_double(instr)

if __name__=='__main__':
	import doctest
	doctest.testmod()
	print([check_string(line) for line in open("input.txt","r")].count(True))
	print([check_string_redux(line) for line in open("input.txt","r")].count(True))
