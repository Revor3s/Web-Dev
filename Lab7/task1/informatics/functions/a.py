a,b,c,d=map(int,input().split())
def minFour(a, b, c, d):
    if a > b: a = b
    if c > d: c = d
    if a < c: return a
    return c

print(minFour(a,b,c,d))