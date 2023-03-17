# set
# ids = {1, 2, 3, 4, 5, 5, 5, 5}
# print(ids)
# n_ids = {5, 6, 7}
# print(len(n_ids))
# minus = n_ids - ids
# print(minus)
# intersect = n_ids.intersection(ids)
# print(intersect)
# s2 = {(1, 2, 3), (3, 4, 5)}  # tuple
# print(len(s2))

s1 = {1, 2, 3}
s1.add(4)
print("s1: ", s1)
s2 = {1, 3, 5, 6}
print("s2: ", s2)
s3 = s1 & s2
print("s3: ", s3)
l1 = list(s3)
print("l1: ", type(l1), l1)
