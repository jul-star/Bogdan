
def main():
    f1()


def f1():
    """Prints the first line of the script .
    """
    print(1)


def f2() -> int:
    """F2 s2 function

    Returns:
        int: [description]
    """
    print(2)
    s = 0
    for _ in range(100):
        s = s*s
    return s


def f3(i: int) -> range:
    """AI is creating summary for f3

    Args:
        i (int): [description]

    Returns:
        range: [description]
    """
    print(2)
    return range(i)


c = 10


def f4(a, b):
    print(dir())
    print('a=', a)
    print('b=', b)


def f5():
    a = set(('a', 'b', 'c'))
    b = set(('a', 'b', 'c'))
    print(id(a))
    print(id(b))
    print('a is b', a is b)
    print('a == b', a == b)
    print('a in b', a in b)
    print('a in a', 'a' in a)
    print(a.intersection(b))
    print(a.difference(b))
    print(a.issubset(b))
    print(not not a)
    print(len(a) > 0)


if __name__ == '__main__':
    f5()

    print('done')
