#! /usr/bin/python
#ab=(1000**2)/2 -1000c
def test9(num):
	for i in range(1,num):
		for j in range(i + 1, num):
#			for k in range(num - i - j, num):
			k = num - i -j
#			if k < j:
#				return (0, 0, 0)
			if i*j == (num**2)/2 - num * k:
				return (i, j, k)
	return (0, 0, 0)

if __name__=='__main__':
	print test9(1000)
