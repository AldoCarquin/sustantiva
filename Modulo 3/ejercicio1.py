from itertools import chain

a = [5, 1, 4, 9, 0]
b = list(chain(range(3, 10), range(20, 23)))
c = [[1,2], [3,4,5],[6,7]]
d = ['perro','gato','jirafa', 'elefante']
e = ['a', a, 2 * a]


print('a2 es ' + str(a[2]))
print('b9 es ' + str(b[9]))
print('c1 es ' + str(c[1][2]))
print('la igualdad es ' + str(e[0] == e[1]))
print('len c es ' + str(len(c)))
print('len c0 es ' + str(len (c[0])))
print('len e es ' + str(len(e)))
print('len c-1 es ' + str(c[-1]))
print('len c-1 +1 es ' + str(c[-1][+1]))
print('c2:+d2: es ' + str(c[2:]+d[2:]))
print('a3:10 es ' + str(a[3:10]))
print('a3:10:2 es ' + str(a[3:10:2]))
print('d index jirafa es ' + str(d.index('jirafa')))
print('ec01 count5 es ' + str(e[c[0][1]].count(5)))
print('sorted a2 es ' + str(sorted(a)[2]))
print('complex b0, b1 es ' + str(complex(b[0], b[1])))