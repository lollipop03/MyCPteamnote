INF = float('inf')

def TSP(now, visited):
    if visited == bit_range - 1: # final
        if adjacent[now][0] != 0:
            return adjacent[now][0]
        else:
            return INF

    if (now, visited) in dp: # memo
        return dp[(now, visited)]

    min_cost = INF
    for i in range(n):
        if adjacent[now][i] == 0:
            continue
        if (1<<i) & visited == 0:
            min_cost = min(TSP(i, (visited | 1<<i)) + adjacent[now][i], min_cost)
    dp[(now, visited)] = min_cost
    return min_cost

n = int(input())
adjacent = [list(map(int, input().split())) for _ in range(n)] # adjacent
bit_range = 1 << n
dp = {}

print(TSP(0, 1, adjacent))