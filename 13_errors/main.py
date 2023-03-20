def main():
    print('main')


def f1():
    print('f1')
    try:
        print(10/0)
    except ZeroDivisionError:
        print('Error: Division by zero')
    print('Out of f1')


def f2():
    print('f2')
    try:
        print(10/0)
    except ZeroDivisionError as ex:
        print('Exception: ', ex)
    print('Out of f2')


def f3():
    try:
        print('10'/2)
    except Exception as ex:
        print('Exception: ', type(ex), '\n ', ex)


def f4():
    try:
        x = '10'/2
    except Exception as ex:
        print('Exception: ', type(ex), '\n ', ex)
    else:
        print('No error')


def f5():
    try:
        x = '10'/2
    except Exception as ex:
        print('Exception: ', type(ex), '\n ', ex)
    else:
        print('No error')
    finally:
        print('Print anyway')


def f6():
    raise TypeError('Hello Julian')


def f7():
    try:
        f6()
    except TypeError as ex:
        print('Exception: ', ex)


def image_info(arg: dict) -> str:
    try:
        title = arg['image_title']
    except Exception as ex:
        raise TypeError('There is not key "image_title" in given dictionary')
    try:
        id = arg['image_id']
    except Exception as ex:
        raise TypeError('There is not key "image_id" in given dictionary')
    else:
        print(f'Image {title} has id {id}')


def test_image_info_01():
    d1 = {'image_title': 'Title 1'}
    try:
        image_info(d1)
    except Exception as ex:
        print(ex)
    else:
        print('test_image_info_01 - Ok')


def test_image_info_02():
    d1 = {'image_id': 5262}
    try:
        image_info(d1)
    except Exception as ex:
        print(ex)
    else:
        print('test_image_info_02 - Ok')


def test_image_info_03():
    d1 = {'image_title': 'Title 1', 'image_id': 5262}
    try:
        image_info(d1)
    except Exception as ex:
        print(ex)
    else:
        print('test_image_info_03 - Ok')


if __name__ == '__main__':
    print('Start')
    # f7()
    test_image_info_01()
    test_image_info_02()
    test_image_info_03()
    print('Done')
