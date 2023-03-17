def mult(a, b):
    return a*b


def my_mult(a, b):
    return (lambda n, m: n*m+a*b)


if __name__ == '__main__':
    print('mult=', mult(2, 5))
    print('my_mult=', my_mult(a=3, b=5)(n=4, m=6))
    #  print('my_mult2=', my_mult(n=10, m=6)(a=4, b=5)) Doesn't work!!!
