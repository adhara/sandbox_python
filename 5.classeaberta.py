#!/usr/bin/env python
# -*- coding: utf-8 -*-

class User(object):
    
    def __init__(self, name):
        self.name = name


def set_password(self, password):
    self.password = password

User.set_password = set_password
user = User('guest')
user.set_password('guest')
for campo in dir(user):
    print campo
print user.password