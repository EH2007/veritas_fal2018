class Solution(object):
    cache = {}
    def fib(self, N):
        if N in self.cache:
          return self.cache[N]
        if (N == 0):
            return 0
        elif N == 1: 
            return 1
        else:
            result = self.fib(N-1) + self.fib(N-2) 
            self.cache[N] = result
            return result

s = Solution()
print(s.fib(4))
