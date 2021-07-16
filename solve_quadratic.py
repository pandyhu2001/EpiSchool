import math

def solve_quadratic(a, b, c): 
    d = b**2 - 4*a*c
    if d < 0: 
        return None
    elif d == 0 : 
        return -b/(2 * a)
    else: 
        sol1 = -b/(2 * a) - math.sqrt(d)/ (2 * a)
        sol2 = -b/(2 * a) + math.sqrt(d)/ (2 * a)
        return (sol1, sol2)
