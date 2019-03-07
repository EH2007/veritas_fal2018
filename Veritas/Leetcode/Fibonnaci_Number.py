class Solution(object):
    def fib(self, N):
        if N == 1:
            return 1
        elif N == 0:
            return 0
        else:
            return self.fib(N - 1) + self.fib(N - 2)

s = Solution()
print(s.fib(4))
