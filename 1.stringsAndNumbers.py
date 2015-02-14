#!/usr/bin/env python
# -*- coding: utf-8 -*-

#convertendo entre real e inteiro
print int(3.14)
print float (5)
print 5.0 / 2 + 3

#Convertendo números de outras bases
print "int('42', 7) = ", int('42', 7)
print "int('42', 8) = ", int('42', 8)
print "int('42', 10) = ", int('42', 10)
print "int('42', 16) = ", int('42', 16)

#Números complexos
print ((3 + 4j) * 2.0).conjugate()

#multiline
print """\
triple 
double \
quotes \
"""
print '''\
triple 
simple \
quotes \
'''
#slices
st =  'Juliana, Ronald'
print st[:7] + ' ama ' + st[-6:]
print st[-6:] + ' ama ' + st[:7]
print 3 * st[-6:3:-1]
ts1 = st[0] + st[-1]
print ts1

#printf
print 'Percentagem: %02.1f%%, Exponencial:%.2e' % (5.333, 0.00314)
print 'O tamanho de "%s" é %d' %(st, len(st))

#string template
musicos = [('Sharon', 'violinista', 'The Corrs'),
                ('Bono', 'vocalista', 'U2'),
                ('Paul', 'baixista', 'Beatles')]
msg = '{0} é {1} do {2}'
for nome, funcao, banda in musicos:
    print (msg.format(nome, funcao, banda))

#parâmetros identificados pelo nome
msg = '{saudacao}, são {hora:02d}:{minuto:02d}'
print msg.format(saudacao='Bom dia', hora=7, minuto=30)

#unicode
u = u'Hüsker dü'
s = u.encode('utf-8')
print s
s = 'Hüsker Dü'
u = s.decode('utf-8')
print type(u)
print s
print len(s), len(u) #na string comum, o acetno conta 2x na len

#building from substrings
colors = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple']
print ''.join(colors)