from typing import Optional

# https://leetcode.com/problems/merge-two-sorted-lists/


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
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy.next


def main():
    list1 = ListNode(1, ListNode(2, ListNode(4)))  # 1 -> 2 -> 4
    list2 = ListNode(1, ListNode(3, ListNode(4)))  # 1 -> 3 -> 4
    s = Solution()
    mergedList = s.mergeTwoLists(list1, list2)
    mergedList.printList()


main()
