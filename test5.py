#! /usr/bin/python

def test5(num):
	re = 1
	for i in range(1, num + 1):
		if re % i:
			p = i / max_common_divisor(re, i)
			re = re * p
	return re		

def max_common_divisor(num1, num2):
	while num1 % num2:
		tmp = num1 % num2
		num1 = num2
		num2 = tmp
	return num2
if __name__=='__main__':
	print test5(10)
	print test5(20)
	print test5(30)
