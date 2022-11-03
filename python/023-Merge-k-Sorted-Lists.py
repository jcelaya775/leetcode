from typing import List, Optional

class Solution:
    class ListNode:
        def __init__(self, val=None, next=None):
            self.val = val
            self.next = next 

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.merge(l1, l2))
            lists = mergedLists
        return lists[0]


    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = self.ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
        
    def listToNode(self, arr):
        dummy = self.ListNode()
        curr = dummy
        for num in arr:
            curr.next = self.ListNode(num)
            curr = curr.next
        return dummy.next


    def printLinkedList(self, head):
        curr = head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")


def main():
    s = Solution()
    l1 = s.listToNode([1, 2, 5, 7, 100])
    l2 = s.listToNode([100, 102, 104])
    l3 = s.listToNode([3, 5, 5, 6])
    l4 = s.listToNode([45, 47, 49, 50])
    s.printLinkedList(s.mergeKLists([l1, l2, l3, l4]))


main()