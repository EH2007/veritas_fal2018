cache = {}
class Solution(object):
    def climbStairs(self, n):
        if n in cache:
            return cache[n]
        if n == 1 or n == 0:
            return 1
        else:
            result = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            cache[n] = result
            return result

sol = Solution()
print(sol.climbStairs(2))