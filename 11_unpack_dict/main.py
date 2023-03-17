def t1():
    b = {'a': 200, 't': '2'}
    red_b = {**b, 'h': 'red'}
    print('red_b=', red_b)
    blue_b = {'h': 'blue', **red_b}
    print('blue_b=', blue_b)


def t2():
    b = {'a': 200, 't': '2'}
    red_b = {**b, 'h': 'red', 's': 500}
    blue_b = {**b, 'h': 'blue', 'z': 300}
    result_b = red_b | blue_b
    print('result_b=', result_b)


if __name__ == '__main__':
    t2()
