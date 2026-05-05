'''Fast Fourier Transform'''

import math

def FFT(y, invert):
    length = len(y)
    bLength = 1
    while 2 ** bLength < length:
        bLength += 1
    N = 2 ** bLength
    y.extend([0] * (N - length))

    order = [0] * N
    for i in range(1, N):
        order[i] = order[i >> 1] >> 1
        if i & 1:
            order[i] = order[i] | (N >> 1)
        if i < order[i]:
            y[i], y[order[i]] = y[order[i]], y[i]

    for i in range(1, bLength + 1):
        loop_size = 2 ** i
        half_size = loop_size // 2
        
        angle = 2 * math.pi / loop_size * invert
        u = complex(math.cos(angle), -math.sin(angle))
        
        for j in range(0, N, loop_size):
            w = complex(1, 0)
            for k in range(half_size):
                val1 = y[j + k]
                val2 = y[j + k + half_size] * w
                
                y[j + k] = val1 + val2
                y[j + k + half_size] = val1 - val2
                
                w *= u

    if invert == -1:
        return [x / N for x in y] 
    else:
        return y