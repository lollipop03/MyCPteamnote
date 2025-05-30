isi = lambda: map(int, input().rstrip().split())
ii = lambda: int(input().rstrip())

def ccw(x1, y1, x2, y2, x3, y3):
    ccw = x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3
    if ccw < 0:
        return -1
    elif ccw > 0:
        return 1
    else:
        return 0

def main():
    ans = 0
    x1, y1, x2, y2 = isi()
    x3, y3, x4, y4 = isi()
    if ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) <= 0\
    and ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) <= 0: #normal
        if ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) == 0\
            and ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) == 0:
            if (min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and\
            min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2)):
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0