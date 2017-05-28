#!/usr/bin/python
#-*- coding: utf-8 -*-

class Fourcal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result


calc = Fourcal()
calc.setdata(5, 3)


