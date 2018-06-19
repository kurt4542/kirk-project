#!/usr/bin/python
#-*- coding: utf-8 -*-

class MyClass2:
    def set(self, v):
        self.value = v
    def incr(self):
        self.set(self.value + 1)
    def put(self):
        print self.value

a = MyClass2()
b = MyClass2()

a.set(2)
a.put()

b.set(3)
b.incr()
b.put()
