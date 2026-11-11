nums = [1, 2, 7, 4, 7, 4, 3, 2, 8]
n = len(nums)


for i in range(n):
    swapped = False

    for j in range(0, n - i - 1):

        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            swapped = True

    if not swapped:
        break
print(nums)