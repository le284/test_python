#! /usr/bin/python

import os
import time

def bak(paths, target_dir) :
	target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
	zip_command = "zip -qr '%s' %s" % (target, ''.join(source))
	if os.system(zip_command) == 0:
		print 'Successful backup to', target
	else:
		print 'Backup FAILED'
if __name__ == '__main__':
	source = ['/home/fanwenbin/wordspace/python']
	target_dir = '/home/fanwenbin/wordspace/'
	bak(source, target_dir) 
	
