def f1(*args, **kwargs):
    print("Positional: ", args)

f1(100, 50, 25)


def f2(*args, **kwargs):
    print("Named: ", kwargs)

f2(gold=100, silver=50, copper=25)

def print(*object, sep)