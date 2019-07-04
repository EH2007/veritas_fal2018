class Solution(object):
    def searchRange(self, nums, target):
        low = 0
        high = len(nums) - 1
        if len(nums) == 0:
            return [-1, -1]
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        first = low
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid
            else:
                low = mid + 1
        if nums[len(nums) - 1] == target:
            last = len(nums) - 1
        else:
            last = low - 1
        if first == last:
            return [first, last]
        elif nums[first] != target:
            return [-1, -1]
        elif nums[first] == target and last < 0:
            return [0, 0]
        else:
            return [first, last]

sol = Solution()
print(sol.searchRange([2,2], 2))