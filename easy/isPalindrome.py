class Solution:
    def isPalindrome(self, x: int) -> bool:
        output = [char for char in str(x)]
        rev_list = output[::-1]
        return (output == rev_list)
