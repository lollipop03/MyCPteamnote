from collections import deque

def addEdge(edge, u, v, cap):
    lu = len(edge[u]); lv = len(edge[v])
    edge[u].append([cap, v, lv])
    edge[v].append([0, u, lu])

def edmondKarp(edge, s, t): # edge: [remain, next, revIdx]
    n = len(edge)
    flow = 0
    
    while True:
        visited = [False for _ in range(n)]
        q = deque()
        q.append(s)
        visited[s] = True
        parent = [(-1, -1) for _ in range(n)]
        
        while q:
            x = q.popleft()
            for i in range(len(edge[x])):
                r, y, _ = edge[x][i]
                if not visited[y] and r > 0:
                    q.append(y)
                    parent[y] = (x, i)
                    visited[y] = True
        if not visited[t]:
            break
        
        b = t
        m = float('inf')
        while b != s:
            a, i = parent[b]
            m = min(m, edge[a][i][0])
            b = a
            
        b = t
        while b != s:
            a, i = parent[b]
            edge[a][i][0] -= m
            edge[b][edge[a][i][2]][0] += m
            b = a
        
        flow += m
        
    return flow