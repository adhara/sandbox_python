# -*- coding: utf-8 -*-

import sqlite3

# Cria uma conexão e um cursor
con = sqlite3.connect('data/emails.db')
cur = con.cursor()

sql = 'create table emails '\
        '(id integer primary key, '\
        ' nome varchar(100), '\
        ' email varchar(100))'
cur.execute(sql)

sql = 'insert into emails values (null, ?, ?)'
recset = [
        ('jane doe', 'jane@nowhere.org'),
        ('rock', 'rock@hardplace.com')
]
for rec in recset:
    cur.execute(sql, rec)
con.commit()


cur.execute('select * from emails')
recset = cur.fetchall()
for rec in recset:
    print '%d: %s(%s)' % rec
