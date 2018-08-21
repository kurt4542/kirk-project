#!/usr/bin/python
#-*- coding: utf-8 -*-
from ..sound.echo import echo_test
import sys

sys.path.append('../sound')

def render_test():
    print("render")
    echo_test()

render_test()
#print sys.path