#!/usr/bin/python3

import hashlib

def check_hashes(key,lead=5):
	val = 1
	while True:
		m = hashlib.md5()
		m.update(key)
		m.update(str(val).encode("UTF-8"))
		d = m.hexdigest()
		if d[:lead] == "0"*lead:
			return val
		val += 1

if __name__=='__main__':
	print(check_hashes(b"iwrupvqb"))
	print(check_hashes(b"iwrupvqb",6))
