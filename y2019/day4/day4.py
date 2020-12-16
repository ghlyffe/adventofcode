#!/usr/bin/python3

def digit_split(val):
	"""
	>>> digit_split(1)
	[1]

	>>> digit_split(123)
	[1, 2, 3]
	"""
	return [int(i) for i in str(val)]

def check_pair(digits):
	"""
	>>> check_pair([])
	False

	>>> check_pair([1])
	False

	>>> check_pair([1,2,3])
	False

	>>> check_pair([1,2,2])
	True
	"""
	for i in range(len(digits)-1):
		if digits[i] == digits[i+1]:
			return True
	return False

def check_pair_exact(digits):
	"""
	>>> check_pair_exact([1,1,2,3,4])
	True

	>>> check_pair_exact([1,1,1,3,4])
	False

	>>> check_pair_exact([1,1,1,3,3])
	True
	"""
	if len(digits)==0:
		return False

	cur_digit = digits[0]
	cur_count = 1
	for i in range(1,len(digits)):
		if digits[i] == cur_digit:
			cur_count += 1
		else:
			if cur_count == 2:
				return True
			cur_count = 1
			cur_digit = digits[i]
	return cur_count == 2

def check_increasing(digits):
	"""
	>>> check_increasing([])
	True

	>>> check_increasing([1])
	True

	>>> check_increasing([1,2,3])
	True

	>>> check_increasing([3,2,1])
	False
	"""
	return digits == sorted(digits)

def force_password(lo,hi,checks=[check_pair,check_increasing]):
	"""
	>>> force_password(10,5)
	[]

	>>> force_password(1,10,[])
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

	>>> force_password(111110, 111112)
	[111111, 111112]
	"""
	rets = []
	for i in range(lo,hi+1): #make sure we include hi
		digits = digit_split(i)
		if all([check(digits) for check in checks]):
			rets.append(i)
	return rets

if __name__=='__main__':
	import doctest
	doctest.testmod()

########################

	print(len(force_password(234208,765869)))
	print(len(force_password(234208,765869,[check_pair_exact,check_increasing])))
