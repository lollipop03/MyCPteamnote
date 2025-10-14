#v: pointers
def point_in_convex_polygon(v, pt):
    if ccw(v[0], v[1], pt) < 0:
        return False

    l, r = 1, len(v) - 1
    while l < r:
        m = (l + r + 1) // 2 
        if ccw(v[0], v[m], pt) >= 0:
            l = m
        else:
            r = m - 1
            
    if l == len(v) - 1:
        return ccw(v[0], v[-1], pt) == 0 and \
               (min(v[0][0], v[-1][0]) <= pt[0] <= max(v[0][0], v[-1][0])) and \
               (min(v[0][1], v[-1][1]) <= pt[1] <= max(v[0][1], v[-1][1]))
               
    return ccw(v[0], v[l], pt) >= 0 and \
           ccw(v[l], v[l + 1], pt) >= 0 and \
           ccw(v[l + 1], v[0], pt) >= 0