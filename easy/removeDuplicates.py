def removeDuplicates(self, nums: List[int]) -> int:
    x = (list(set(nums)))
    x.sort()
    k = len(x)
    for i in range(len(x)):
        nums[i] = x[i]
    return k
