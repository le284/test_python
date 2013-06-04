#! /usr/bin/python
import math
def is_prim(num):
	n = int(math.sqrt(num))
	if n < 2:
		return True
	for i in range(2, n + 1):
		if num % i == 0:
			return False
	return True
def prim_sum(num):
	sum = 2
	for i in range(3, num, 2):
		if is_prim(i):
			sum += i
	return sum

if __name__=='__main__':
	print prim_sum(10)
	print prim_sum(2000000)
