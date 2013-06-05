#! /usr/bin/python

def is_frindly(num):
	sum1 = yueshu_sum(num)
	sum2 = yueshu_sum(sum1)
	if sum2 == num and sum1 != num :
		return True
	else:
		return False
		
def yueshu_sum(num):
	sum = 0
	for i in range(1, num/2 + 1):
		if num % i:
			continue
		else:
			sum += i
	return sum
if __name__=='__main__':
	for i in range(2, 10000):
		if is_frindly(i):
			print i
