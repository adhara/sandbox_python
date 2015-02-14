#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ListaSemRep(list):

    def removeReps(self):
        l2 = self[:]
        for item in l2:
            if l2.count(item) > 1:
                l2.remove(item)
        return l2


if __name__ == '__main__':
    ml = ListaSemRep(['a', 'a', 'b', 'c', 'b'])
    print ml.removeReps()