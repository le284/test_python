#! /usr/bin/python

def getGYZ(num):
	re = []
	flag = 0
	for i in range(2, num / 2 + 1):
		if not num % i :
			if flag == i:
				break
			re.append(i)
			flag = num / i
			re.append(flag)
	return re
			
def getSumANum(num):
	re = 0
	while  num:
		re += num % 10
		num /= 10
	return re
def getMax(num):
	yinzi = getGYZ(num)
	max = 0
	for i in yinzi:
		sum = 0
		x = num / i
		for j in range(2, x / 2 + 1):
			if not x % j:
				if j > 9:
					j = getSumANum(j)
				sum += j
				x /= j
				j = 1
		if i > 9:
			i = getSumANum(i)
		if x > 9:
			x = getSumANum(x)
		if sum + i + x > max:
			max = sum + i + x
	return max
	
if __name__=='__main__':
	print getMax(24)
