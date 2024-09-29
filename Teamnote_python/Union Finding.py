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

# Example
n = int(input())
ds = DisjointSet(n)
ds.union(0, 3)

if ds.is_union(0, 3):
    print('YES')
else:
    print('NO')
