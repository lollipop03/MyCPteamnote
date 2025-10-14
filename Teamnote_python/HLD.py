class HLD:
    def __init__(self, n, edges, initial_values):
        self.N = n
        self.Top = [0] * (n + 1)
        self.Par = [0] * (n + 1)
        self.Dep = [0] * (n + 1)
        self.Sz = [0] * (n + 1)
        self.In = [0] * (n + 1)
        
        self.inp_graph = [[] for _ in range(n + 1)]
        self.tree_graph = [[] for _ in range(n + 1)]
        
        for u, v in edges:
            self.connect(u, v)
        
        self.dfs0(1, 0)
        self.dfs1(1)
        
        self.pv = 0
        self.Top[1] = 1
        self.dfs2(1)

        linearized_values = [0] * n
        for i in range(1, n + 1):
            linearized_values[self.In[i]] = initial_values[i-1]
        # self.seg_tree = SegmentTreeSum(linearized_values)


    def connect(self, u, v):
        self.inp_graph[u].append(v)
        self.inp_graph[v].append(u)

    def dfs0(self, v, b=-1):
        self.Par[v] = b
        self.Dep[v] = self.Dep[b] + 1 if b != 0 else 0
        for i in self.inp_graph[v]:
            if i != b:
                self.tree_graph[v].append(i)
                self.dfs0(i, v)

    def dfs1(self, v):
        self.Sz[v] = 1
        for i, child in enumerate(self.tree_graph[v]):
            self.dfs1(child)
            self.Sz[v] += self.Sz[child]
            if self.Sz[child] > self.Sz[self.tree_graph[v][0]]:
                self.tree_graph[v][i], self.tree_graph[v][0] = self.tree_graph[v][0], self.tree_graph[v][i]

    def dfs2(self, v):
        self.In[v] = self.pv
        self.pv += 1
        for i, child in enumerate(self.tree_graph[v]):
            self.Top[child] = self.Top[v] if i == 0 else child
            self.dfs2(child)

    def vertex_update(self, x, v):
        # self.seg_tree.update(self.In[x], v)


    def path_query(self, u, v):
        res = 0
        while self.Top[u] != self.Top[v]:
            if self.Dep[self.Top[u]] < self.Dep[self.Top[v]]:
                u, v = v, u
            
            start_idx, end_idx = self.In[self.Top[u]], self.In[u]
            # res += self.seg_tree.range_sum(start_idx, end_idx)
            
            u = self.Par[self.Top[u]]
            
        start_idx, end_idx = self.In[u], self.In[v]
        if start_idx > end_idx:
            start_idx, end_idx = end_idx, start_idx

        
        return res