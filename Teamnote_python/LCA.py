'''LCA(VlogV)'''
from collections import deque

def bfs(N, edges, start): # parent check
    tree = [[] for _ in range(N+1)]
    visited = [False]*(N+1)
    q = deque()
    q.append((start,0)) # now, depth
    visited[start]=True
    tree[start] = (-1, 0) # parent, depth
    
    while q:
        x, d = q.popleft()
        for i in edges[x]:
            if not visited[i]:
                q.append((i,d+1))
                visited[i] = True
                tree[i] = (x, d+1)
    
    return tree

def LCA(V, tree, a, b):
    lgV = V.bit_length()
    
    dp = [[-1 for _ in range(V+1)] for _ in range(lgV)] # dp table
    for i in range(1, V+1):
        dp[0][i] = tree[i][0]
    for i in range(1, lgV):
        for j in range(1, V+1):
            if dp[i-1][j] != -1:
                dp[i][j] = dp[i-1][dp[i-1][j]]
                
    if tree[a][1] < tree[b][1]: a, b= b,a
    diff = tree[a][1]-tree[b][1]
    
    cnt = 0
    while diff > 0:
        if diff%2:
            a = dp[cnt][a]
        diff //=2
        cnt += 1
    
    if a != b:
        for i in range(lgV-1, -1, -1):
            if dp[i][a] != -1 and dp[i][a] != dp[i][b]:
                a = dp[i][a]
                b = dp[i][b]
        a = dp[0][a]
    return a
    
    

N = int(input())
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
start = 1
tree = bfs(N, edges, start)

a, b = map(int, input().split())
ans = LCA(N, tree, a, b)