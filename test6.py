#! /usr/bin/python

def test6(num):
	re = 0;
	for i in range(1, num + 1):
		for j in range(1, num + 1):
			if i == j:
				continue;
			re += i*j
	return re
if __name__=='__main__':
	print test6(10)
	print test6(100)		
