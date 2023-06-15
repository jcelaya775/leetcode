from typing import List

# https://leetcode.com/problems/lru-cache/


class Solution:
    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = self.Node(0)
            self.right = self.Node(0)

    def __init__(self, capacity, left=None, right=None):
        self.cache = {}
        self.left = left
        self.right = right
        self.left.next, self.right.prev = self.right, self.left

    # Removes LRU node from list
    def remove(self):
        prev, next = self.left, self.left.next
        prev.next, next.prev = next, prev

    # Inserts node into MRU position
    def insert(self, key, value):
        node = self.Node(value)
        prev, next = self.right.prev, self.right
        prev.next, next.prev = node, node

    # Gets the MRU node
    # O(1) Time & Space
    def get(self, key):
        if not self.right.prev.prev:
            return -1
        return self.cache[key]

    # Put Node(key, value) into MRU
    # O(1) Time & Space
    def put(self, key, value):
        # Insert node into MRU position
        if key in self.cache:
            self.cache[key] = value
        else:
            self.insert(key, value)

        # If cache is full, remove LRU from cache
        if len(self.cache) + 1 > self.capacity:
            self.remove()
            del self.cache[self.left.key]


def main():
    s = Solution()


main()
