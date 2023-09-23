

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        number1List = []
        number2List = []

        while l1:
            number1List.append(l1.val)
            l1 = l1.next

        while l2:
            number2List.append(l2.val)
            l2 = l2.next

        sum1 = int(''.join(map(str, reversed(number1List))))
        sum2 = int(''.join(map(str, reversed(number2List))))

        finalSum = sum1 + sum2
        result = [int(digit) for digit in str(finalSum)]

        dummy = ListNode()
        current = dummy
        for num in reversed(result):
            current.next = ListNode(num)
            current = current.next

        return dummy.next
