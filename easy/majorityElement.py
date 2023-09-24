def majorityElement(nums: list[int]) -> int:
    my_dict = {}

    for i in range(len(nums)):
        my_dict[nums[i]] = my_dict.get(nums[i], 1) + 1

    return max(my_dict, key=my_dict.get)


print(majorityElement([3, 2, 3]))
