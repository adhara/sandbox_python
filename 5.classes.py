#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Pendrive(object):     #new style, deriva de object, auto no py3

    def __init__(self, size, usb='2.0'):
        self.size = size
        self.usb = usb


class MP3Player(Pendrive):

    def __init__(self, size, usb='2.0', turner=False):
        self.turner = turner
        Pendrive.__init__(self, size, usb)


mp3 = MP3Player(1024)
print '%s\n%s\n%s' % (mp3.size, mp3.usb, mp3.turner)