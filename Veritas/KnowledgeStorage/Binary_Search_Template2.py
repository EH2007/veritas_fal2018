def find_first_occur(nums, target):
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid
    if nums[low] == target:
        return low
    else:
        return "This value is not in the list."

nums = [5, 5, 7, 7, 8, 8, 10]
print(find_first_occur(nums, 6))