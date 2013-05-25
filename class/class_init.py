#! /usr/bin/python
#coding:utf-8
class Person:
	def __init__(self, name):
		self.name = name
	def sayHi(self):
		print '我爱你,',self.name

if __name__ == '__main__':
	p = Person('云洁～')
	p.sayHi()
