def minSubArrayLen(target: int, nums: list[int]) -> int:
    start = 0
    end = 0
    min_length = float('inf')
    current_sum = 0

    while end < len(nums):
        current_sum += nums[end]

        while current_sum >= target:

            min_length = min(min_length, end - start + 1)

            current_sum -= nums[start]
            start += 1

        end += 1

    if min_length == float('inf'):
        return 0
    return min_length
