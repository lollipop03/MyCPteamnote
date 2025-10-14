isi = lambda: map(int, input().rstrip().split())
ii = lambda: int(input().rstrip())
''' Segment Tree '''
class SegmentTreeSum:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build_tree(data)
    
    def build_tree(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, index, value):
        pos = index + self.n
        self.tree[pos] = value
        while pos > 1:
            self.tree[pos >> 1] = self.tree[pos] + self.tree[pos ^ 1]
            pos >>= 1

    def range_sum(self, left, right):
        result = 0
        left += self.n
        right += self.n+1
        while left < right:
            if left % 2:
                result += self.tree[left]
                left += 1
            if right % 2:
                right -= 1
                result += self.tree[right]
            left >>= 1
            right >>= 1
        return result
    
class LazySegmentTreeSum:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        self.tree = [0] * (2 * self.size)
        self.lazy = [0] * (2 * self.size)
        self.build_tree(data)
    
    def build_tree(self, data):
        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
    
    def push(self, node, node_left, node_right): #lazy to main
        if self.lazy[node] != 0:
            self.tree[node] += self.lazy[node] * (node_right - node_left + 1)
            if node < self.size:
                self.lazy[2 * node] += self.lazy[node]
                self.lazy[2 * node + 1] += self.lazy[node]
            self.lazy[node] = 0

    def range_update(self, left, right, value):
        self._range_update(1, 0, self.size - 1, left, right, value)
    
    def _range_update(self, node, node_left, node_right, left, right, value):
        self.push(node, node_left, node_right)
        
        if right < node_left or node_right < left:
            return
        
        if left <= node_left and node_right <= right:
            self.lazy[node] += value
            self.push(node, node_left, node_right)
            return
        
        mid = (node_left + node_right) // 2
        self._range_update(2 * node, node_left, mid, left, right, value)
        self._range_update(2 * node + 1, mid + 1, node_right, left, right, value)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def range_sum(self, left, right):
        return self._range_sum(1, 0, self.size - 1, left, right)
    
    def _range_sum(self, node, node_left, node_right, left, right):
        self.push(node, node_left, node_right)
        
        if right < node_left or node_right < left:
            return 0
        
        if left <= node_left and node_right <= right:
            return self.tree[node]
        
        mid = (node_left + node_right) // 2
        left_sum = self._range_sum(2 * node, node_left, mid, left, right)
        right_sum = self._range_sum(2 * node + 1, mid + 1, node_right, left, right)
        return left_sum + right_sum
    
N, M, K = isi()
data = [ii() for _ in range(N)]
seg_tree = LazySegmentTreeSum(data)
seg_tree.update_range(1,4,5)