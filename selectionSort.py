nums = [1, 2, 7, 4, 7, 4, 3, 2, 8]
n = len(nums)

for i in range(n):

    min_index = i
    for j in range(i + 1, n):
        if nums[j] < nums[min_index]:
            min_index = j

    nums[i], nums[min_index] = nums[min_index], nums[i]

print("Sorted list:", nums)