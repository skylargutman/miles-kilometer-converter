def add(*args):
    total = 0
    for n in args:
        total += n
    return total

print(add(3,4,5,6,7))