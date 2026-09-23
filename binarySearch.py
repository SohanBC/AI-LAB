nums = [1, 2, 7, 4, 7, 4, 3, 2, 8]
target = 8

nums.sort()  # nums becomes [1, 2, 2, 3, 4, 4, 7, 7, 8]

low = 0
high = len(nums) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if nums[mid] == target:
        print(f"Found {target} at index {mid}!")
        found = True
        break  
    elif nums[mid] < target:
        low = mid + 1  
    else:
        high = mid - 1 

if not found:
    print(f"{target} not found in the list.")