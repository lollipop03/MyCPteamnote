def de_bruijn(k, n):
    if k == 1:
        return [0]

    res = []
    aux = [0] * (n + 1)

    def _dfs(t, p):
        if t > n:
            if n % p == 0:
                res.extend(aux[1 : p + 1])
        else:
            aux[t] = aux[t - p]
            _dfs(t + 1, p)
            for i in range(aux[t - p] + 1, k):
                aux[t] = i
                _dfs(t + 1, t)

    _dfs(1, 1)
    
    return res