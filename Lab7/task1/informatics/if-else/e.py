def isBigger(a, b):
    if a > b: return 1
    elif b > a: return 2
    return 0
print(isBigger(int(input()), int(input())))