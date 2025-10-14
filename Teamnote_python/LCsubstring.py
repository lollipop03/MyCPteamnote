'Longest Increasing Substring'
def LCstr(string_A, string_B, dp):
    len_A, len_B = len(string_A), len(string_B)

    max_length = 0
    end = 0
    for i in range(1, len_A + 1):
        for j in range(1, len_B + 1):
            if string_A[i - 1] == string_B[j - 1]: # search same or not
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end = i
            else:
                dp[i][j] = 0

    start = end - max_length
    lcs = string_A[start:end] #substring from start to end

    return dp, lcs

string_A = list(input())
string_B = list(input())

dp = [[0 for _ in range(len(string_B))] for _ in range(len(string_A))]
dp, arr = LCstr(string_A, string_B, dp)
print(arr)