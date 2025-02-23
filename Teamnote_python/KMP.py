def KMP_table(pattern):
    LP = len(pattern)
    table = [0 for _ in range(LP)]
    
    Pidx = 0
    for idx in range(1, LP):
        while Pidx > 0 and pattern[Pidx] != pattern[idx]:
            Pidx = table[Pidx-1]
        
        if pattern[idx] == pattern[Pidx] :
            Pidx += 1
            table[idx] = Pidx
    
    return table

def KMP(word, pattern, table):
    results = [] #start idx
    Pidx = 0
    
    for idx in range(len(word)):
        while Pidx > 0 and word[idx] != pattern[Pidx] :
            Pidx = table[Pidx-1]
        if word[idx] == pattern[Pidx]:
            if Pidx == len(pattern)-1 :
                results.append(idx-len(pattern)+1)
                Pidx = table[Pidx]
            else:
                Pidx += 1
    
    return results

P = input().strip()
LP = len(P)
table = KMP_table(P)

word = input().strip()
result = KMP(word, P, table)