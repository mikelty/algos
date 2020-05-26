#solves https://leetcode.com/problems/longest-common-subsequence/
class Solution:
    def longestCommonSubsequence(self, s1, s2):
        l1, l2 = len(s1), len(s2)
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        for i,x in enumerate(s1):
            for j,y in enumerate(s2):
                if x==y:
                    dp[i+1][j+1]=dp[i][j]+1
                else:
                    dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])
        return dp[-1][-1]
