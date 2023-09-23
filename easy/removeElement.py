def removeElement(nums: list[int], val: int) -> int:
    k = 0
    nums.sort()
    nums.reverse()
    for i in range(len(nums) - 1, - 1, - 1):
        if nums[i] == val:
            nums.pop(i)
            k += 1
    return k, nums


print(removeElement([3, 2, 2, 3], 3))
