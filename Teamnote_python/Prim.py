'''Prim algorithm N<<M'''
import heapq

def prim(start, adj_list):
    visited = [False] * (N + 1)
    min_heap = [(0, start)]
    mst_edges = []

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True

        for v, w in adj_list[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))
                mst_edges.append((u, v, w))

    return mst_edges

N, M = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    adj_list[u].append((v, w))
    adj_list[v].append((u, w))

edges = prim(1, adj_list)

