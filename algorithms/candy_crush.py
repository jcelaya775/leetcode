class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


def makeLinkedList(arr):
    if not arr:
        return

    prev = None
    curr = None
    head = None
    for i in range(len(arr)):
        curr = Node(arr[i], prev)
        if not head:
            head = curr
        else:
            prev.next = curr
        prev = curr

    curr.next = None
    return head


# Crush candy if 2 or more consecutive candies
def crushCandy(candy, k):
    dummy = Node(0, None, candy)
    candy.prev = dummy

    while candy:
        left, right = candy, candy
        count = 1

        while left.prev.val == left.val:  # explore left
            left = left.prev
            count += 1
        while right.next and right.val == right.next.val:  # explore right
            right = right.next
            count += 1
        if count >= k:  # perform crush
            left.prev.next = right.next
            if right.next:
                right.next.prev = left.prev

        candy = right.next

    return dummy.next


def printCandyForwards(candy):
    while candy:
        print(candy.val, end=" -> ")
        candy = candy.next
    print("None")


def main():
    # Create a linked list (candy)
    candy = makeLinkedList("BBBAAAAA")

    # Play candy crush
    newCandy = crushCandy(candy, 4)
    printCandyForwards(newCandy)


main()
