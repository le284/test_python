#! /usr/bin/python

def getMap(num):
	map = {}
	map[1] = 1
	step = 1
	i = 2
	while i <= num:
		map[i] = step
		step += 1
		i *= 2
	for j in range(3, num + 1, 2):
		rmin = map[j - 1] + 1
		for k in range(3, j / 2, 2):
			if j - k in map and k in map:
				x = 1
				if (j - k) < k:
					break
				if not (j - k) % k:
					x = (j - k) / k
				else:
					continue
				if ((x & (x - 1)) == 0) and (rmin > map[j - k] + 1):
					rmin = map[j - k] + 1
		tmp = j
		while tmp <= num:
			map[tmp] = rmin
			rmin += 1
			tmp *= 2
	return map
	
if __name__=='__main__':
	map = getMap(30)
	for i in range(1, 30):
		print '%s -->%s' % (i,  map[i])
