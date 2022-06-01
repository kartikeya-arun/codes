import math
def polysum(n,s):
    ar=(0.25*n*s**2)/math.tan(math.pi/n)
    pr=n*s
    return round(ar+pr**2,4)
