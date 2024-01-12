class Solution:
  def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    if len(text1) == 0 or len(text2) == 0: return 0
    dp = [[0 for j in range(len(text2))] for i in range(len(text1))]

    for i in range(len(text1)):
      if text2[0] in text1[:i + 1]: dp[i][0] = 1
    
    for j in range(len(text2)):
      if text1[0] in text2[:j + 1]: dp[0][j] = 1
    
    for i in range(1, len(text1)):
      for j in range(1, len(text2)):
        if text1[i] == text2[j]: dp[i][j] = dp[i - 1][j - 1] + 1
        else: dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    print(dp)
    return dp[len(text1) - 1][len(text2) - 1]
