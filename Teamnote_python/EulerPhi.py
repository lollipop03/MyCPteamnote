def phi(M): #MloglogM
    phi = list(range(M + 1))
    for i in range(2, M + 1):
        if phi[i] == i: # i is prime
            for j in range(i, M + 1, i):
                phi[j] = phi[j] // i * (i - 1)
    return phi[1:]