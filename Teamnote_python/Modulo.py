'''Modular Multiplicative Inverse (ax = 1 mod M)'''

def xGCD(a, b):
    # (g, x, y) such that a*x + b*y = g = gcd(a, b)
    if b == 0:
        return (a, 1, 0)
    else:
        g, x, y = xGCD(b, a % b)
        return (g, y, x - (a // b) * y)

def mod_inverse(a, m): # if M is not prime
    g, x, _ = xGCD(a, m)
    if g != 1:
        return None
    else:
        return x % m
    
def mod_pow(a, b, m):
    result = 1
    a %= m
    while b > 0:
        if b & 1:
            result = (result * a) % m
        a = (a**2) % m
        b //= 2
    return result

def mod_inverse_fermat(a, m): # if M is prime
    return mod_pow(a, m - 2, m)

def mod_divide(a, b, m):
    inv_b = mod_inverse(b, m) # if M is prime, use mod_inverse_fermat instead.
    return (a * inv_b) % m

def mod_factorial(a, m):
    fact = 1
    for i in range(2, a+1):
        fact *= i
        fact %= m
    return fact
