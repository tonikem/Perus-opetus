import functools


def validate(f):
    @functools.wraps(f)
    def decor(*args, **kwargs):
        x, y = args
        print('validated value x:', x)
        print('validated value y:', y)
        x = x+2
        y = y+1
        res = f(x, y, **kwargs)
        return res
    return decor


@validate
def child(x, y):
    print('child got value x:', x)
    print('child got value y:', y)
    return x, y


child(3, 6)
#child(2, 1)


