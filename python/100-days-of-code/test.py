# File for testing small sections of code that are not required as part of a project
def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))
