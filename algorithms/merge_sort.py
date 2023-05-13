from typing import List
import random


def merge_sort(array: List[int]):
    return merge_sort_helper(array, [0 for _ in range(len(array))], 0, len(array) - 1)


def merge_sort_helper(array: List[int], temp: List[int], leftStart: int, rightEnd: int):
    if leftStart >= rightEnd:
        return

    middle = (leftStart + rightEnd) // 2
    merge_sort_helper(array, temp, leftStart, middle)  # merge left half
    merge_sort_helper(array, temp, middle + 1, rightEnd)  # merge right half
    merge_halves(array, temp, leftStart, rightEnd)


def merge_halves(array: List[int], temp: List[int], leftStart: int, rightEnd: int):
    leftEnd = (leftStart + rightEnd) // 2
    rightStart = leftEnd + 1

    leftPtr = leftStart
    rightPtr = rightStart
    index = leftStart

    while leftPtr <= leftEnd and rightPtr <= rightEnd:
        if array[leftPtr] < array[rightPtr]:
            temp[index] = array[leftPtr]
            leftPtr += 1
        else:
            temp[index] = array[rightPtr]
            rightPtr += 1
        index += 1
    while leftPtr <= leftEnd:  # add remaining elements
        temp[index] = array[leftPtr]
        leftPtr += 1
        index += 1
    while rightPtr <= rightEnd:  # add remaining elements
        temp[index] = array[rightPtr]
        rightPtr += 1
        index += 1

    # Copy sorted portion to main array
    for i in range(leftStart, rightEnd + 1):
        array[i] = temp[i]


def generate_random_array(n: int, min_val: int = 0, max_val: int = 100) -> List[int]:
    return [random.randrange(min_val, max_val) for _ in range(n)]


def main():
    # Test merge sort on 10 random arrays
    for _ in range(10):
        arr = generate_random_array(20)
        merge_sort(arr)
        print(f"sorted array: {arr}")


main()
