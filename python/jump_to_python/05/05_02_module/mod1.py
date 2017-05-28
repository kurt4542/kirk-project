#!/usr/bin/python
#-*- coding: utf-8 -*-

def safe_mul(a, b):
    if type(a) != type(b):
        print ("곱할 수 있는 것이 없습니다.")
        return
    else:
        result = a * b

    return result

def safe_sum(a, b):
    if type(a) != type(b):
        print ("더할 수 있는 것이 없습니다.")
        return
    else:
        result = a + b

    return result

if __name__ == "__main__":
    print(safe_sum('a', 1))
    print(safe_sum(1, 4))
    print(sum(10, 10.4))

