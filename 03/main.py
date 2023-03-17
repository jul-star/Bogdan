disk = {}

print(id(disk))
print(type(disk))

d2 = disk
print(id(d2))
del d2
# print(id(d2))
# print(disk.__doc__)
disk['a'] = 1
disk['b'] = 2
print(disk)
print(disk.items())
print(list(disk.keys()))
d2 = disk.copy()
print(id(d2), " / ", id(disk))
