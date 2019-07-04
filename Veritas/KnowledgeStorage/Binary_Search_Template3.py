def find_last_occur( nums , target):
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] > target:
            high = mid 
        else:
            low = mid + 1
    return low - 1 

nums = [2, 2]
print(find_last_occur(nums, 2))