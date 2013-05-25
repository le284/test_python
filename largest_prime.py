#! /usr/bin/python

def largest_prime(num) :
	re = 0
	i = 3
	while num:
		if num % i == 0:
			re = i
			num = num / i
		i = i + 1
	return re

if __name__ == '__main__' :
	largest_prime(600851475143)
