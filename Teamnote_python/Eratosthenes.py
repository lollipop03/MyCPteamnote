'''Sieve of Eratosthenes'''

MN = 4*10**5
Target = 6*10**6
check = [True] * (Target + 1)
check[0] = False
check[1] = False
prime = []
for i in range(2, Target + 1):
    if check[i]:
        prime.append(i)
        if len(prime) >= MN:
            break
        for j in range(i * i, Target + 1, i):
            check[j] = False