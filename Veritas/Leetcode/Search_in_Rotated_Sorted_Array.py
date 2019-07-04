class Solution(object):
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1
        if len(nums) == 0:
            return -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] != target:
                if target < nums[mid] < nums[high]:
                    high = mid - 1
                elif nums[mid] > nums[high]:
                    
                else:
                    low = mid + 1
        return -1
sol = Solution()
print(sol.search([3, 5, 1], 3))