class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def cross(self, other):
        return self.x * other.y - self.y * other.x
    
    def to_tuple(self):
        return (self.x, self.y)

def dist_sq(p1, p2):
    return (p1.x - p2.x)**2 + (p1.y - p2.y)**2

def calipers(hull):
    point = [Point(x, y) for x, y in hull]
    n = len(point)
    if n < 2:
        return None
    maxi = 0
    pA, pB = point[0], point[1]

    j = 1
    for i in range(n):
        i_next = (i + 1) % n

        while True:
            j_next = (j + 1) % n
            
            vi = point[i_next] - point[i]
            vj = point[j_next] - point[j]
            
            if vi.cross(vj) < 0:
                break

            cur = dist_sq(point[i], point[j])
            if cur > maxi:
                maxi = cur
                pA, pB = point[i], point[j]
            
            j = j_next

        cur = dist_sq(point[i], point[j])
        if cur > maxi:
            maxi = cur
            pA, pB = point[i], point[j]

    return pA.to_tuple(), pB.to_tuple()