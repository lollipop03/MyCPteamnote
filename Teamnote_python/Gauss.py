from decimal import Decimal

def is_zero_decimal(val):
    return val == Decimal('0')

def Gauss(a, square=True):
    n = len(a)
    m = len(a[0]) if n > 0 else 0
    rank = 0
    
    rref_matrix = [row[:] for row in a]
    
    inv_matrix = [[Decimal('0')] * n for _ in range(n)]
    if square:
        for i in range(n):
            inv_matrix[i][i] = Decimal('1')

    det = Decimal('1')

    for i in range(m):
        if rank == n:
            break

        if is_zero_decimal(rref_matrix[rank][i]): # row exchange
            mx = Decimal('0')
            idx = -1
            for j in range(rank + 1, n):
                if mx < abs(rref_matrix[j][i]):
                    mx = abs(rref_matrix[j][i])
                    idx = j
            
            if idx == -1 or is_zero_decimal(rref_matrix[idx][i]): # linearly dependent
                det = Decimal('0')
                continue
            
            rref_matrix[rank], rref_matrix[idx] = rref_matrix[idx], rref_matrix[rank]
            if square:
                inv_matrix[rank], inv_matrix[idx] = inv_matrix[idx], inv_matrix[rank]
            
            det *= Decimal('-1')
        
        det *= rref_matrix[rank][i]
        
        coeff = Decimal('1') / rref_matrix[rank][i]
        for j in range(m):
            rref_matrix[rank][j] *= coeff
        if square:
            for j in range(n):
                inv_matrix[rank][j] *= coeff
        
        for j in range(n):
            if rank == j:
                continue
            
            t = rref_matrix[j][i]
            for k in range(m):
                rref_matrix[j][k] -= rref_matrix[rank][k] * t
            if square:
                for k in range(n):
                    inv_matrix[j][k] -= inv_matrix[rank][k] * t
        
        rank += 1
    
    if square and rank < n:
        det = Decimal('0')

    return rref_matrix, rank, det, inv_matrix