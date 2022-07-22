def decorator1(func):
  def wrapper1(a):
    a = a+"I am in wrapper1"
    return func(a)
  return wrapper1


def decorator2(func):
  """Comment"""
  def wrapper2(a):
    a = a+" and now in wrapper 2"
    return func(a)
  return wrapper2

@decorator1
@decorator2
def func(a):
  print(a)


a = ""
func(a)
