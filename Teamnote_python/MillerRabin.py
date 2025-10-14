''' Miller-Rabin Prime verdict '''
A = [2,3,5,7,11,13,17,19,23,29,31,37,41] # for "upper ll" range

def millerRabin(n, a):
  k = n - 1 # k = m*2^n
  while k % 2 == 0:
    mod = pow(a, k, n)
    if (mod == n-1):
      return True
    k = k >> 1
  # last odd number(k = m)
  mod = pow(a, k, n)  
  return mod == n-1 or mod == 1

def isPrime(n):
  for i in A:
    if n == i:
      return True
    if n % i == 0:
      return False
    if not millerRabin(n, i):
      return False
  return True