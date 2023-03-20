
def f1():
    """unpack list
    """
    fruits = ['a', 'b', 'c']
    x, y, z = fruits
    print(f'{x}, {y}, {z}')


def f2():
    """unpack tuple
    """
    fruits = ('a', 'b', 'c')
    x, y, z = fruits
    print(f'{x}, {y}, {z}')


def f3():
    """unpack with *
    """
    fruits = ('a', 'b', 'c')
    x, *remains = fruits
    print('x: ', type(x), ' remains: ', type(remains))
    print(f'{x}, {remains}')


if __name__ == '__main__':
    f3()
