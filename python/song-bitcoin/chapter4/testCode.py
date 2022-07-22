def decorator1(func):
    a = a+"I am in wrapper1"
    return func(a)


def decorator2(func):
    """Comment"""
    a = a+" and now in wrapper 2"
    return func(a)

@decorator1
@decorator2
def func(a):
    print(a)


a = ""
func(a)
