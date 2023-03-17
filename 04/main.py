a = 'Hello'
b = 345
c = [1, 2, 3]
c1 = (a, b, c)
print(c1)
c.append(4)
print(c1)
print(c1.count('Hello'))
l = list(range(1, 5))
t = tuple(l)
print(type(t))
print(t)
print(t.count(5))
print(t.count(4))
idx = t.index(4)
print(idx)
