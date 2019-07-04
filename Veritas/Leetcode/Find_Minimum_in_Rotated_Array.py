class Solution(object):
    def findMin(self, nums):
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]
sol = Solution()
print(sol.findMin([3,4,5,1,2]))