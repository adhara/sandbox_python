rate   = 1.01

print "[USP]"

amount = 195000
allow  = 8800
months = 27

for i in xrange(months):
    print '[',  i, ']', amount
    amount = amount * rate - allow
    if ( i == 15 ) :
        allow = allow * (rate**12) - 1500 # - 2000
    
print "[final] ", amount

print "-----------------------------------------------"

print "[City London]"

months = 11
fee = 15000
exchange = 5.2
allow = 11700
amount = 190000 - fee * exchange

for i in xrange(months):
    print '[',  i, ']', amount
    amount = amount * rate - allow
    
print "[final] ", amount

print "-----------------------------------------------"

print "[Guelph]"

months = 16
fee = 6700
exchange = 2.76
allow = 10700
amount = 190000 - 8800*3

for i in xrange(months):
    print '[',  i, ']', amount
    amount = amount * rate - allow
    if (i in [0, 6, 12]):
        amount = amount - fee * exchange
    
print "[final] ", amount

print "-----------------------------------------------"
