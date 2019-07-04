class Solution(object):
    def search(self, nums, target):
        first = 0
        last = len(nums) - 1
        while first <= last:
            mid = (first + last) // 2
            if nums[mid] < target:
                first = mid + 1
            elif nums[mid] > target:
                last = mid - 1
            else:
                return mid
        return -1
