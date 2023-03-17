from copy import deepcopy
n1 = 10
print('n1=', id(n1))
n2 = 10
print('n2=', id(n2))
n3 = n2
print('n3=', id(n3))
n3 += 5
print('n2=', id(n2))
print('n3=', id(n3))


d1 = {'n': 1, 'm': 2, 'l': []}
print('d1: ', d1)
d2 = d1
d3 = deepcopy(d1)
d2.get('l').append('x')
d3.get('l').append('y')

print('d1: ', d1)
print('d2: ', d2)
print('d3: ', d3)
