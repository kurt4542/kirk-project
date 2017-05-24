#!/usr/bin/python

f = open('t.txt')
for line in f:
    print line

line = f.readline()
while line:
    print line,
    line = f.readline()
