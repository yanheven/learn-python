from functools import reduce

start = '693375992'
for i in range(1000):
    midle = ''
    if i < 100:
        midle += '0'
    if i < 10:
        midle += '0'
    midle += str(i)
    c1 = reduce(lambda x, y: x+y,
               [int(start[j]) for j in range(len(start)) if j%2==0])
    c1 += int(midle[1])
    c2 = reduce(lambda x, y: x+y,
               [int(start[j]) for j in range(len(start)) if j%2==1])
    c2 += int(midle[0]) + int(midle[2])
    c = 10 - (c1 + 3*c2) % 10
    if c == 10:
        c = 0
    upc = '{}{}{}'.format(start, midle, str(c))
    print(upc)
