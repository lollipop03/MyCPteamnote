def factinv(p):
    fact = [1] * p
    inv = [1] * p
    for i in range(1, p):
        fact[i] = (fact[i-1] * i) % p

    inv[p-1] = pow(fact[p-1], p - 2, p)

    for i in range(p-2, -1, -1):
        inv[i] = (inv[i+1] * (i + 1)) % p
        
    return fact, inv

def lucas(n, k, p, fact, inv):
    def comb_mod(n, k, p, fact, inv):
        if k < 0 or k > n:
            return 0
        return fact[n] * inv[k] % p * inv[n-k] % p
    
    cnt = 1
    while n or k:
        n, dn = divmod(n, p)
        k, dk = divmod(k, p)
        
        cnt = (cnt * comb_mod(dn, dk, p, fact, inv)) % p
        if cnt == 0:
            break
    return cnt