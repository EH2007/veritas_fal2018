class Solution(object):
    def reverseString(self, s):
        s = s[::-1]
        return s

s = Solution()
ss = ["h", 'e', 'l', 'l', 'o']
print(s.reverseString(ss))