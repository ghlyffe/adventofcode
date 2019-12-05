#!/usr/bin/python3
from math import floor

def fuel_for_masses(masses):
	return int(sum([max(0,floor(int(i)/3)-2) for i in masses]))

def fuel_for_masses_file(fname):
	return int(sum([max(0,floor(int(i)/3)-2) for i in open(fname,"r")]))

def fuel_for_module(mass):
	masses = [mass]
	res = fuel_for_masses(masses)
	while res > 0:
		masses.append(res)
		res = fuel_for_masses([res])
	return sum(masses[1:])	#Don't add the module mass, but everything else is an amount of fuel

def corrected_fuel_for_masses_file(fname):
	return sum([fuel_for_module(int(i)) for i in open(fname,"r")])


if __name__=='__main__':
	print(fuel_for_masses_file("day1_input.txt"))
	print(corrected_fuel_for_masses_file("day1_input.txt"))
