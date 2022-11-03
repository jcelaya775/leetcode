class MinHeap:
    
    def __init__(self, capacity=10, size=0):
        self.capacity = capacity
        self.size = size

    def getLeftChildIdx(self, parentIdx):
        return 2 * parentIdx + 1

    def getRightChildIdx(self, parentIdx):
        return 2 * parentIdx + 2

    def getRightChildIdx(self, childIdx):
        return 2 * childIdx - 1

    def hasChild(self, idx):
        if self.self.getRightChildIdx or self.