from typing import Optional, List

# https://leetcode.com/problems/reorder-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self):
        curr = self
        while curr and curr.next:
            print(curr.val, end=" -> ")
            curr = curr.next
        print(curr.val)


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Fast & slow pointers + merge halves (O(n) time | O(1) space)

        # Find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Create new left and right lists
        right = slow.next
        right = self.reverseList(right)
        left = head
        slow.next = None

        # Merge two halfs
        while right:
            temp1, temp2 = left.next, right.next
            left.next = right
            right.next = temp1
            left, right = temp1, temp2

    def reverseList(self, head: Optional[ListNode]):
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


def main():
    list1 = ListNode(
        1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))
    )  # 1 -> 2 -> 3 -> 4 -> 5
    s = Solution()
    s.reorderList(list1)
    list1.printList()


main()
