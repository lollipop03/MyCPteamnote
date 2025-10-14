INF = float('inf')

def TSP(now, visited):
    if visited == alll:
        if cost[now][0] != 0:
            return cost[now][0]
        else:
            return INF

    if (now, visited) in dp:
        return dp[(now, visited)]

    min_cost = INF
    for next in range(n):
        if cost[now][next] == 0 or (visited & (1 << next)):
            continue
        cost = TSP(next, visited | (1 << next)) + cost[now][next]
        
        min_cost = min(min_cost, cost)

    dp[(now, visited)] = min_cost
    return min_cost

n = ii()
cost = [list(isi()) for _ in range(n)]

alll = (1 << n) - 1
dp = {}
result = TSP(0, 1)