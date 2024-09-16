'Longest Increasing Sequence'
def LCseq(string_A, string_B, dp):
    arr = []
    len_A, len_B = len(string_A), len(string_B)
    
    for i in range(1, len_A + 1): # edge skip due to no word
        for j in range(1, len_B + 1):
            if string_A[i - 1] == string_B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    cnt = dp[len_A][len_B] # max length fix

    while cnt != 0: # arr finking: search up or right is same
        if dp[len_A - 1][len_B] == cnt:
            len_A -= 1
        elif dp[len_A][len_B - 1] == cnt:
            len_B -= 1
        else: # else append self
            arr.append(string_A[len_A-1])
            cnt -= 1
            len_A -= 1
            len_B -= 1
    
    lcs = ''.join(reversed(arr))

    return dp, lcs
	

string_A = list(input())
string_B = list(input())

dp = [[0 for _ in range(len(string_B) + 1)] for _ in range(len(string_A) + 1)] # initialize to 0
dp, arr = LCseq(string_A, string_B, dp)

print(arr)