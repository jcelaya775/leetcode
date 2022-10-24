from collections import defaultdict

class Graph:
    nodeMap = defaultdict(lambda: None)
    
    class Node:
        def __init__(self, id, adjacent=None):
            self.id = id
            self.adjacent = adjacent

    def getNode(self, id):
        return self.nodeMap[id]
    
    def addEdge(self, source, target):
        n = self.getNode(source)
        s = self.getNode(target)
        s.adjacent.add(s)
    
    def hasPathDFS(self, source, target):
        n = self.getNode(source)
        s = self.getNode(target)
        visited = set()
        return self.hasPathDFS(source, target, visited)

    def hasPathDFS(self, source, target, visited):
        if source in visited:
            return False

        
def main():
    graph = Graph()


main()