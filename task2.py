def remove_zeros(nums):
    current_len = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[current_len] = nums[i]
            current_len += 1

    return nums[:current_len]


array = [0, 1, 0, 0, 4, 5, 6, 7, 0, 8, -4, 0]
result = remove_zeros(array)
print(result)
