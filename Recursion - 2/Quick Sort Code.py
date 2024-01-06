"""
	The function is called with the parameters:
	quickSort(input, 0, size - 1);

"""
from typing import List

def quickSort(arr: List[int], startIndex: int, endIndex: int):
    def partitionArray(arr: List[int], startIndex: int, endIndex: int) -> int:
        pivot = arr[startIndex]
        count = 0
        for i in range(startIndex + 1, endIndex + 1):
            if arr[i] <= pivot:
                count += 1
        pivotIndex = startIndex + count
        temp = arr[startIndex]
        arr[startIndex] = arr[pivotIndex]
        arr[pivotIndex] = temp

        i = startIndex
        j = endIndex
        while i <= pivotIndex and j >= pivotIndex:
            while i <= pivotIndex and arr[i] <= pivot:
                i += 1
            while j >= pivotIndex and arr[j] > pivot:
                j -= 1
            if i < pivotIndex and j > pivotIndex:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                i += 1
                j -= 1
        return pivotIndex
    
    if startIndex < endIndex:
        pivotIndex = partitionArray(arr, startIndex, endIndex)
        quickSort(arr, startIndex, pivotIndex - 1)
        quickSort(arr, pivotIndex + 1, endIndex)