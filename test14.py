#! /usr/bin/python

def get_step(num):
	re = 1
	while num != 1:
		if num % 2:
			num = 3 * num + 1
		else:
			num /= 2
		re += 1
	return re
def get_value(num):
	re_max = 0
	re = 0
	for i in range(1, num + 1, 2):
		temp = get_step(i)
		if temp > re_max :
			re_max = temp
			re = i
	return (re, re_max)
if __name__=='__main__':
	print get_value(1000000)		
