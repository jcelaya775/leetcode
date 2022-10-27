from typing import Optional, ListNode

# https://leetcode.com/problems/count-the-number-of-consistent-strings/

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    # O(n) Time | O(1) Space
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end = head
        count = 1
        while end and count <= n:
            end = end.next
            count += 1
            
        nodeToRemove = head
        while end and end.next:
            nodeToRemove = nodeToRemove.next
            end = end.next
            
        if nodeToRemove:
            removeNode(nodeToRemove)
        return head

            
def removeNode(node):
    if node and node.next:
        node.next = node.next.next


def printLinkedList(head):
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next


def main():
    input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    print(input)