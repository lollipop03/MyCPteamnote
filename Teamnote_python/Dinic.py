'''Dinic'''
from collections import deque

def addEdge(edge, u, v, cap):
    lu = len(edge[u])
    lv = len(edge[v])
    edge[u].append([cap, v, lv])
    edge[v].append([0, u, lu])

def dinic(edge, s, t): # edge: [remain, next, revIdx]
    
    def bfs(edge, s, t, level):
        for i in range(len(level)):
            level[i] = -1
        
        level[s] = 0
        q = deque()
        q.append(s)
        
        while q:
            x = q.popleft()
            for cap, y, rev_idx in edge[x]:
                if cap > 0 and level[y] < 0:
                    level[y] = level[x] + 1
                    q.append(y)
        
        return level[t] != -1

    def dfs(edge, u, t, pushed, work, level):
        if u == t:
            return pushed
            
        while work[u] < len(edge[u]):
            cap, v, rev_idx = edge[u][work[u]]
            
            if level[v] == level[u] + 1 and cap > 0:
                tr = dfs(edge, v, t, min(pushed, cap), work, level)
                
                if tr > 0:
                    edge[u][work[u]][0] -= tr
                    edge[v][rev_idx][0] += tr
                    return tr
            
            work[u] += 1
        
        return 0

    n = len(edge)
    flow = 0
    
    while True:
        level = [0] * n
        if not bfs(edge, s, t, level):
            break
        
        work = [0] * n
        
        while True:
            pushed = dfs(edge, s, t, float('inf'), work, level)
            if pushed == 0:
                break
            flow += pushed
            
    return flow