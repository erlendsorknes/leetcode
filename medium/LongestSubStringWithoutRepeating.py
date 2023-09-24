def lengthOfLongestSubstring(self, s: str) -> int:
    start = 0
    end = 0
    max_length = 0

    tracking = set()

    while end < len(s):
        if s[end] not in tracking:
            tracking.add(s[end])
            max_length = max(max_length, end - start + 1)
            end += 1
        else:
            tracking.remove(s[start])
            start += 1
    return max_length
