class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
        

def makeLinkedList(li):
    if not li:
        return

    head = Node(li[0])
    curr = head
    for i in range(1, len(li) - 1):
        curr.next = Node(li[i])
        curr = curr.next

    return head
    
        
# AAABBCCCBBBBBDD
# ABBACD

# Crush candy if 2 or more consecutive candies
def crushCandy(candy):
    head = dummy.next
    dummy = head

    while candy:
        print(candy.val, candy.next.val)
        start = candy.prev
        counter = 1
        while candy and candy.next and candy.val == candy.next.val:
            candy = candy.next
            counter += 1

        if counter >= 2:
            start.next = candy.next
        
    
    return head


def printCandy(candy):
    while candy:
        print(candy.val, end = " -> ")
        candy = candy.next
    print("None")


def main():
    # Create a linked list (candy)
    candy = makeLinkedList("ABASFSD")
    
    printCandy(candy)
    # Play candy crush
    # newCandy = crushCandy(candy)

main()