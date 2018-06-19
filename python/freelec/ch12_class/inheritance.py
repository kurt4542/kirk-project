#!/usr/bin/python
#-*- coding: utf-8 -*-

class Person:
    def __init__(self, name, phone=None):
        self.name = name
        self.phone = phone

    def __repr__(self):
        return '<Person %s %s>' % (self.name, self.phone)

class Employee(Person):
    def __init__(self, name, phone, position, salary):
        Person.__init__(self, name, phone)
        self.position = position
        self.salary = salary

    def __repr__(self):
        s = Person.__repr__(self)
        return s + ' <Employee %s %s>' %(self.position, self.salary)

#m1 = Employee('James', 5664, 'Manager', 200)
#m2 = Employee('Philfa', 9000, 'Principal', 300)

p1 = Person('gslee', 5893)
m1 = Employee('kslee', 5224, 'President', 500)

print p1
print m1