from collections import deque

def addEdge(edge, u, v, cap, cost):
    lu = len(edge[u]); lv = len(edge[v])
    edge[u].append([cap, cost, v, lv])
    edge[v].append([0, -cost, u, lu])

def MCMF(edge, s, t): # edge: [remain, cost, next, revIdx]
    n = len(edge)
    flow = 0
    minCost = 0
    
    while True:
        dist = [float('inf') for _ in range(n)]
        visited = [False for _ in range(n)]
        q = deque()
        q.append(s)
        dist[s] = 0
        visited[s] = True
        parent = [-1 for _ in range(n)]
        
        while q:
            x = q.popleft()
            visited[x] = False
            
            for i in range(len(edge[x])):
                r, c, y, _ = edge[x][i]
                if r > 0 and dist[y] > dist[x] + c:
                    dist[y] = dist[x] + c
                    parent[y] = (x, i)
                    if not visited[y]:
                        q.append(y)
                        visited[y] = True
                        
        if parent[t] == -1: break
        
        b = t
        m = float('inf')
        while b != s:
            a, i = parent[b]
            m = min(m, edge[a][i][0])
            b = a
        
        curCost = 0
        b = t
        while b != s:
            a, i = parent[b]
            edge[a][i][0] -= m
            edge[b][edge[a][i][3]][0] += m
            curCost += edge[a][i][1]
            b = a
        
        flow += m
        minCost += m*curCost
        
    return flow, minCost