class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int.
        :rtype: List[int]
        """
        #value_list = []
        for i in range(len(nums)):
            a = nums[i]
            new_nums = nums[i + 1:]
            for i2 in range(len(new_nums)):
                b = new_nums[i2]
                if a + b == target:
                    #value_list.append(i)
                    #value_list.append(i + i2 + 1)
                    return [i, i+i2+1]
                else:
                    pass
        

nums = [3, 2, 4]
target = 6
sol = Solution()
result = sol.twoSum(nums, target)
print(result)