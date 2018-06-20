#!/usr/bin/python
#-*- coding: utf-8 -*-

class Animal:
    pass

class Dog(Animal):
    def Cry(self):
        print '멍멍'

class Duck(Animal):
    def Cry(self):
        print '꽥꽥'

class Fish(Animal):
    def Cry(self):
        pass

a = Dog()
b = Duck()
c = Fish()

a.Cry()
b.Cry()
c.Cry()

for i in Dog(), Duck(), Fish():
    i.Cry()





