#!/usr/bin/python
# -*- coding: utf-8 -*-

class AA:
    def test(self):
        a = 1

        return a

    def mytest(self, AA_a):
        b = 2
        c = AA_a + b
        return c


class BB(AA):
    def test(self):
        a = 100

        return a


aa = AA()
bb = BB()

AA_a = aa.test()
BB_a = bb.test()
print AA_a
print BB_a

print aa.mytest(AA_a)
print bb.mytest(BB_a)
#print bb.test()

#print aa.mytest(1)
