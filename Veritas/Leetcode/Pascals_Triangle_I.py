class Solution(object):
    def getRow(self, rowIndex): # rowIndex 3
        if rowIndex == 1:
          return [[1]]
        elif rowIndex == 2:
          return [ [1], [1, 1] ]
        else:
          prev_all = self.getRow(rowIndex - 1) # [ [1], [1, 1], [1 , 2, 1] ]
          prev = prev_all[-1] # [ 1, 2, 1]
          result = [1] + [prev[i] + prev[i + 1] for i in range(len(prev) - 1) ] + [1]
          # [ 1, 3, 3, 1]
          prev_all.append(result)
        return prev_all # [ [1], [1, 1], [1 , 2, 1] , [1, 3, 3, 1] ]
sol = Solution()
print(sol.getRow(10))