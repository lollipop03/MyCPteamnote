import math
import random
EPS = 1e-9

#class point 먼저 작성
# __Sub__, dot, cross, dist, __repr__
#p: point
def cnt2p(p1, p2):
    return Point((p1.x + p2.x) / 2.0, (p1.y + p2.y) / 2.0)

def cnt3p(p1, p2, p3):
    vA = p2 - p1
    vB = p3 - p1

    c1 = vA.dot(vA) * 0.5
    c2 = vB.dot(vB) * 0.5
    d = vA.cross(vB)

    if abs(d) < EPS:
        dists = {(p1.dist(p2), (p1, p2)),
                     (p1.dist(p3), (p1, p3)),
                     (p2.dist(p3), (p2, p3))}
        max_dist_pnts = max(dists)[1]
        return cnt2p(max_dist_pnts[0], max_dist_pnts[1])

    x = p1.x + (c1 * vB.y - c2 * vA.y) / d
    y = p1.y + (c2 * vA.x - c1 * vB.x) / d

    return Point(x, y)

def enclosingCircle(pnts):
    random.shuffle(pnts)
    
    n = len(pnts)
    if n == 0:
        return Point(0, 0), 0
    elif n == 1:
        return pnts[0], 0

    cnt = cnt2p(pnts[0], pnts[1])
    r = cnt.dist(pnts[0])

    for i in range(2, n):
        if cnt.dist(pnts[i]) > r + EPS:
            cnt = cnt2p(pnts[0], pnts[i])
            r = cnt.dist(pnts[0])
            
            for j in range(1, i):
                if cnt.dist(pnts[j]) > r + EPS:
                    cnt = cnt2p(pnts[i], pnts[j])
                    r = cnt.dist(pnts[i])

                    for k in range(j):
                        if cnt.dist(pnts[k]) > r + EPS:
                            cnt = cnt3p(pnts[i], pnts[j], pnts[k])
                            r = cnt.dist(pnts[i])
                            
    return cnt, r