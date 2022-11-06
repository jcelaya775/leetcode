import java.util.Arrays;

public class MinPriorityHeap {
    private int capacity = 10;
    private int size = 0;

    int[] items = new int[capacity];
    
    private int getLeftChildIndex(int parentIndex) { return 2 * parentIndex + 1; } 
    private int getRightChildIndex(int parentIndex) { return 2 * parentIndex + 2; }
    private int getParentIndex(int childIndex) { return (childIndex - 1) / 2; }
    
    private boolean hasLeftChild(int index) { return getLeftChildIndex(index) < size; }
    private boolean hasRightChild(int index) { return getRightChildIndex(index) < size; }
    private boolean hasParent(int index) { return getParentIndex(index) >= 0; }

    private int leftChild(int index) { return items[getLeftChildIndex(index)]; }
    private int rightChild(int index) { return items[getRightChildIndex(index)]; }
    private int parent(int index) { return items[getParentIndex(index)]; }

    private void swap(int indexOne, int indexTwo) {
        int temp = items[indexOne];
        items[indexOne] = items[indexTwo];
        items[indexTwo] = temp;
    }

    private void ensureExtraCapacity() {
        if (size == capacity) {
            items = Arrays.copyOf(items, capacity * 2);
            capacity *= 2;
        }
    }

    public boolean empty() { return size == 0; }

    public int peak() {
        if (size == 0) throw new IllegalArgumentException();
        return items[0];
    }

    // Replaces root element with last child and heapifies down
    public int poll() {
        if (size == 0) throw new IllegalArgumentException();
        int item = items[0];
        items[0] = items[size - 1];
        size--;
        heapifyDown();
        return item;
    }

    public void add(int item) {
        ensureExtraCapacity();
        items[size] = item;
        size++;
        heapifyUp();
    }

    public void heapifyUp() {
        int index = size - 1;
        while (hasParent(index) && parent(index) > items[index]) {
            swap(getParentIndex(index), index);
            index = getParentIndex(index);
        }
    }

    public void heapifyDown() {
        int index = 0;
        while (hasLeftChild(index)) {
            int smallerChildIndex = getLeftChildIndex(index);
            if (hasRightChild(index) && rightChild(index) < items[smallerChildIndex]) {
            smallerChildIndex = getRightChildIndex(index);
            }
            
            if (items[index] > items[smallerChildIndex]) {
                swap(index, smallerChildIndex);
            } else {
                break;
            }
            index = smallerChildIndex;
        }
    }

    public static void main(String[] args) {
        MinPriorityHeap heap = new MinPriorityHeap();

        int[] input = { 3, 6, 2, 6, 1, 3, 4, 6, 7, 3, 4, 84, 54, 54, 42 };
        for (int num : input) heap.add(num);
        
        System.out.println("Heap items:");
        while (!heap.empty()) {
            System.out.println(heap.peak());
            heap.poll();
        }
    }
}