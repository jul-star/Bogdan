# print('Bordan')
# print(2+2)
# d: dict = {'a': 1, "b": 2}
# print("D", d)
# print(dir(__builtins__))
# name = input("Input your name: ")
# print(name.capitalize())
# my_list = [1, 2, 2, 2, 3]


# l = 2
# s: str = "Hello"
# n_s: str = s.replace('o', 'a')
# print(n_s)
# print(s.count('l'))
# print(s[:3])
# _base = 10
# _power = 2
# _res = pow(_base, _power)
# print("Power: ", _res, ", type=", type(_res))
# _x = 10_100_000
# print("X=", _x)
# _y: float = pow(_base, _power)
# print("Power: ", _y, ", type=", type(_y))

# complex
# _cm1: complex = 3+5j
# _cm2: complex = 5-7j
# print("c:+ ", _cm1 + _cm2)
# print("c:- ", _cm1 - _cm2)
# print("c:* ", _cm1 * _cm2)
# print("c:/ ", _cm1 / _cm2)

# magic method __add__, __radd__
_a = int(5)+float(5.)
print(_a, type(_a))

_a = float(5.) + int(5)
print(_a, type(_a))

# print("Int: \n", dir(int))
print("Bool: \n", dir(bool))
print("_add__: ", bool.__and__.__doc__)
