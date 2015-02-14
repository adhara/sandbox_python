#!/usr/bin/env python
# -*- coding: utf-8 -*-

#soma todos - o for é diferente do C...
s = 0

for x in range(1, 200, 2):
    s = s + x
print s

#else roda quando o loop vai até o fim (não para em break)
for n in range(2, 1000):
    for x in range(2, (n/2 + 1)):

        if not n % x:
            print n, ' = ', x, '*', n/x
            break

    else:   # loop acabou
        print n, ' é primo'

#adivinhe o numero 
print 'Guess my number...'

guess = 0
correct = 42

while guess != correct:
    guess = int(raw_input())
    if guess > correct:
        print 'menos'
    elif guess < correct:
        print 'mais'
print 'got it!'