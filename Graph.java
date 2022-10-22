import java.util.HashMap;
import java.util.LinkedList;

public class Graph {
    private HashMap<Integer, Node> nodeLookupMap = new HashMap<Integer, Node>();

    public static class Node {
        private int id;
        LinkedList<Node> adjacent = new LinkedList<Node>();

        private Node(int id) {
            this.id = id;
        }
    };
    
    private Node getNode(int id) {
        return nodeLookupMap.get(id);
    }

    public void addEdge(int source, int destination) {
        Node s = getNode(source);
        Node d = getNode(destination);
        s.adjacent.add(d);
    }
}