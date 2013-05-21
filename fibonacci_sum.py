#! /usr/bin/python
'''
Fibonacci 数列，求偶数值的和
'''
def f_even_sum(num):
	a = 1
	b = 1
	sum = 0
	while a < num :
		c = a + b
		a = b
		b = c
		if b % 2 == 0 :
			sum += b
	return sum
print f_even_sum(100000000)
