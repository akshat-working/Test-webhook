def add(x, y):
    if y == 0:
        return x
    elif y > 0:
        return add(x + 1, y - 1)
    else:
        return add(x - 1, y + 1)
a = -2
b = 7
print(add(a,b))
