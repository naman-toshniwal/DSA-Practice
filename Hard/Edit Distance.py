"""
Given two strings s and t. Return the minimum number of operations required to convert s to t.
The possible operations are permitted:

Insert a character at any position of the string.
Remove any character from the string.
Replace any character from the string with any other character.
"""

class Solution:
    def editDistance(self, s, t):
        m=len(s)
        n=len(t)
        dp=[[0]*(n+1) for i in range(m+1)]
       
        for i in range(m+1):
            dp[i][0]=i
        
        for j in range(n+1):
            dp[0][j]=j
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=1+min(dp[i-1][j-1],dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        s, t = input().split()
        ob = Solution();
        ans = ob.editDistance(s, t)
        print(ans)
