def main():
    val = 'Hello' if True else 'Buy'
    print(val)
    print('Hello' if True else 'Buy')
    print(f1() if False else f2())


def f1():
    return 'A'


def f2():
    return 'B'


def test_filter():
    l = [1, 3, 4, 5, 6, 9]
    print('l: ', l)
    res = list(filter(check_val, l))
    print('res', res)


def check_val(item):
    return item > 4


if __name__ == '__main__':
    # main()
    test_filter()
