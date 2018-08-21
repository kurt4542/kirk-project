#!/usr/bin/python
# -*- coding: utf-8 -*-

dash = 'se-test-log-elb'
underscore = 's3_test'

print dash.find('-')
print underscore.find('-')

if dash.find('-') == -1:
    print 'a'