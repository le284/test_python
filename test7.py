#! /usr/bin/python

import math

def prim_num(num):
	n, i = 1, 1
	while True:
		i += 1
		if is_prim(i):
			if n >= num:
				return i
			n += 1
	return 0			

def is_prim(num):
	n =int(math.sqrt(num))
	while n > 1:
		if num % n == 0:
			return False
		n -= 1
	return True

if __name__=='__main__':
	print prim_num(6)
	print prim_num(10001)
#	for i in range(2,10):
#		print is_prim(i)
