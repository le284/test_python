import math
def get_num_array(base, num):
	length = int(num * math.log10(base)) + 1
	re=[0 for i in range(length)]
	re[0] = 1
	for i in range(num):
		for j in range(length):
			re[j] *= base
		for k in range(length):
			if re[k] > 9:
				re[k+1] += re[k]/10
				re[k] %= 10
	return re
if __name__=='__main__':
	x = get_num_array(2,1000)
	sum = 0
	for i in x:
		sum += i
	print sum
