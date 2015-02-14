#!/usr/bin/env python
# -*- coding: utf-8 -*-

def media(lst):
    return float(sum(lst)) / len(lst)
    
if __name__ == '__main__':
    print media([1, 2, 3, 4, 5, 6, 7])