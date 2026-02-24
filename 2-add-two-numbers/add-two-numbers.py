# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0                      # carry value
        head = ListNode(0)             # starting node
        temp = head                    # pointer to build result

        while l1 != None or l2 != None:

            sum = carry                # start with previous carry

            if l1 != None:
                sum = sum + l1.val
                l1 = l1.next

            if l2 != None:
                sum = sum + l2.val
                l2 = l2.next

            carry = sum // 10          # get new carry
            digit = sum % 10           # get single digit

            temp.next = ListNode(digit)   # create new node
            temp = temp.next              # move pointer

        # if carry left after loop
        if carry > 0:
            temp.next = ListNode(carry)

        return head.next
        