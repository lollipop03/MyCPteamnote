'''Kruskal Algorithm N>=M'''
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    
    def find(self, index1):
        if self.parent[index1] != index1:
            self.parent[index1] = self.find(self.parent[index1])
        return self.parent[index1]

    def union(self, index1, index2):
        root1 = self.find(index1)
        root2 = self.find(index2)
        if root1 != root2:
            if root1 < root2:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2

    def is_union(self, index1, index2):
        return self.find(index1) == self.find(index2)

def kruskal(n, edges):
    ds = DisjointSet(n)
    w = 0
    e = []

    edges.sort(key=lambda x:x[2])

    for weight, u, v in edges:
        if not ds.is_union(u, v):
            ds.union(u, v)
            w += weight
            e.append((u, v, weight))

    return w, e

N, M = map(int, input().split())
edges = []

for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

w, e = kruskal(N, edges)