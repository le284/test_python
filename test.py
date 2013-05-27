#! /usr/bin/python

def max_test(num):
	min_num = 10 ** (num - 1)
	max_num = 10 ** num
	max_palindrome = 0
	re=(0,0,0)
	for i in range(min_num, max_num):
		for j in range(min_num, max_num):
			p = i * j
			if is_palindrome(p):
				if p > max_palindrome:
					max_palindrome = p;
					re=(i, j, max_palindrome)
	return re
			
def is_palindrome(num):
	s = str(num)
	for i in range(len(s)/2):
		if s[i] != s[-i - 1]:
			return False
	return True
if __name__ == '__main__':
	print max_test(2)
	print max_test(3)
