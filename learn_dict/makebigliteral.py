print '{',
for i in range(255):
    print '"a%r": %r,' % (i, i),
print '}'
