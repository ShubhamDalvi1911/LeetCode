# -------- Helper Functions --------
def list_to_linkedlist(arr):
    dummy = ListNode(0)
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

def linkedlist_to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
        head = ListNode(0)
        root = head
        carry = 0
        
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry

            carry = total // 10
            head.next = ListNode(total % 10)
            head = head.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            head.next = ListNode(carry)

        return root.next
        
l1 = list_to_linkedlist([2,4,3])
l2 = list_to_linkedlist([5,6,4])
result = Solution().addTwoNumbers(l1, l2)
print(linkedlist_to_list(result))