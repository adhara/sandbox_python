#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
from sqlalchemy import *



# Torna acessíveis os metadados
metadata = MetaData(db)
metadata.bind.echo = True

# Tabela Prog
prog_table = Table('progs', metadata,
    Column('prog_id', Integer, primary_key=True),
    Column('name', String(80))
)

# Cria a tabela
prog_table.create()
# Carrega a definição da tabela - autoload = True -> mapeia o que já tem no banco
prog_table = Table('progs', metadata, autoload=True)

# Insere dados
i = prog_table.insert()
i.execute(
    {'name': 'Yes'}, 
    {'name': 'Genesis'}, 
    {'name': 'Pink Floyd'}, 
    {'name': 'King Crimson'})
    
# Seleciona
s = prog_table.select()
r = s.execute()
for row in r.fetchall():
    print row