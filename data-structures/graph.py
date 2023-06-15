from collections import defaultdict
from collections import deque


class Graph:
    nodeMap = defaultdict(lambda: None)

    class Node:
        def __init__(self, id):
            self.id = id
            self.adjacent = deque()

    def initVertices(self, vertexList):
        for id in vertexList:
            self.nodeMap[id] = self.Node(id)

    def getNode(self, id):
        return self.nodeMap[id]

    def addEdge(self, source, target):
        s = self.getNode(source)
        t = self.getNode(target)
        if s is None or t is None:
            return False
        s.adjacent.append(t)

    def hasPathDFS(self, source, target):
        s = self.getNode(source)
        t = self.getNode(target)
        if s is None or t is None:
            return False
        visited = set()
        return self.hasPathDFSHelper(s, t, visited)

    def hasPathDFSHelper(self, source, target, visited):
        if source.id in visited:
            return False

        visited.add(source.id)
        if source == target:
            return True

        for neighbor in source.adjacent:
            if self.hasPathDFSHelper(neighbor, target, visited):
                return True

        return False

    def hasPathBFS(self, source, target):
        queue = deque()
        queue.append(source)
        visited = set()
        while queue:
            node = queue.popleft()
            if node == target:
                return True
            if node.id in visited:
                continue
            for neighbor in node.adjacent:
                queue.appendleft(neighbor)

            visited.add(node.id)
        return False


def main():
    graph = Graph()
    graph.initVertices([1, 2, 6, 8])
    graph.addEdge(2, 8)
    graph.addEdge(2, 1)
    graph.addEdge(1, 2)

    print(graph.hasPathBFS(graph.getNode(1), graph.getNode(2)))
    print(graph.hasPathBFS(graph.getNode(2), graph.getNode(1)))
    print(graph.hasPathBFS(graph.getNode(1), graph.getNode(6)))


main()
