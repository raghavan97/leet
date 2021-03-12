from pprint import pprint

class Solution(object):
    def palindrome(self, s):
        p1 = 0
        n = len(s)
        p2 = n-1

        # [a,b,c,b,a]  len=5 , p1 <= len/2
        # [a,b,b,a]  len=4 , p1 <= len/2 - 1
        midpoint = n/2
        while p1 <= midpoint:
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 = n-1-p1
        return True


    def longestPalindrome(self, s):

        n = len(s)
        dp = arr = []
        for i in range(n):
            col = [] 
            for j in range(n): 
                col.append(0) 
            arr.append(col) 


        i=0
        while i<n:
            dp[i][i] = 1
            i += 1

        pprint(dp)


if __name__ == "__main__":
    s = Solution()
    # s.checkPalindromes([5,12,34,56,78])
    res = s.longestPalindrome("abcba")
    import sys
    sys.exit(0)
    print(res)
    res = s.longestPalindrome("A")
    print(res)
    res = s.longestPalindrome("abcba")
    print("result='{}'".format(res))



