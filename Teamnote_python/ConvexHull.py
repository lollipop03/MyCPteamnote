def ccw(x1, y1, x2, y2, x3, y3):
    ccw = x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3
    if ccw < 0:
        return -1
    elif ccw > 0:
        return 1
    else:
        return 0

def graham_scan(Dots):
    start = min(Dots, key=lambda p: (p[1], p[0]))
    
    Dots.sort(key=lambda p: (atan2(p[1] - start[1], p[0] - start[0]), p[0], p[1]))
    
    hull = []
    for dot in Dots:
        while len(hull) >= 2 and cross_product(hull[-2], hull[-1], dot) <= 0:
            hull.pop()
        hull.append(dot)
    
    return {p[2] for p in hull}

def solve():
    N = int(input())
    Dots = []
    
    for i in range(N):
        x, y = isi()
        Dots.append([x, y, i + 1])
    
    result = graham_scan(Dots)
    return " ".join(map(str, sorted(result)))

if __name__ == "__main__":
    print(solve())
